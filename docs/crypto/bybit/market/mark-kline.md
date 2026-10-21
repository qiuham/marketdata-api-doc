---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/mark-kline
api_type: Market Data
updated_at: 2026-10-21 18:47:16.176981
---

# Get New Delivery Price

Get historical option delivery prices.

> **Covers: Option**

info

  * It is recommended to query this endpoint 1 minute after settlement is completed, because the data returned by this endpoint may be delayed by 1 minute.
  * By default, the most recent 50 records are returned in reverse order of "deliveryTime".



### HTTP Request

GET`/v5/market/new-delivery-price`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. _Valid for`option` only_  
baseCoin| **true**|  string| Base coin, uppercase only. _Valid for`option` only_  
settleCoin| false| string| Settle coin, uppercase only. Default: `USDT`.  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> deliveryPrice| string| Delivery price  
> deliveryTime| string| Delivery timestamp (ms)  
  
* * *

### Request Example

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/new-delivery-price?category=option&baseCoin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_new_delivery_price(  
        category="option",  
        baseCoin="BTC"  
    ))  
    
    
    
      
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "option",  
            "list": [  
                {  
                    "deliveryPrice": "111675.89830854",  
                    "deliveryTime": "1756080000000"  
                },  
                {  
                    "deliveryPrice": "114990.41430239",  
                    "deliveryTime": "1755993600000"  
                },  
                {  
                    "deliveryPrice": "115792.27557281",  
                    "deliveryTime": "1755907200000"  
                },  
                {  
                    "deliveryPrice": "113162.32041387",  
                    "deliveryTime": "1755820800000"  
                },  
                {  
                    "deliveryPrice": "113852.00497157",  
                    "deliveryTime": "1755734400000"  
                },  
                {  
                    "deliveryPrice": "113604.53226162",  
                    "deliveryTime": "1755648000000"  
                },  
                {  
                    "deliveryPrice": "114828.99222851",  
                    "deliveryTime": "1755561600000"  
                },  
                {  
                    "deliveryPrice": "115321.04746356",  
                    "deliveryTime": "1755475200000"  
                },  
                {  
                    "deliveryPrice": "117969.66726839",  
                    "deliveryTime": "1755388800000"  
                },  
                {  
                    "deliveryPrice": "117622.21555318",  
                    "deliveryTime": "1755302400000"  
                },  
                {  
                    "deliveryPrice": "118846.72206411",  
                    "deliveryTime": "1755216000000"  
                },  
                {  
                    "deliveryPrice": "121778.983223",  
                    "deliveryTime": "1755129600000"  
                },  
                {  
                    "deliveryPrice": "119383.31934289",  
                    "deliveryTime": "1755043200000"  
                },  
                {  
                    "deliveryPrice": "119030.19489407",  
                    "deliveryTime": "1754956800000"  
                },  
                {  
                    "deliveryPrice": "121725.4933271",  
                    "deliveryTime": "1754870400000"  
                },  
                {  
                    "deliveryPrice": "117780.91332268",  
                    "deliveryTime": "1754784000000"  
                },  
                {  
                    "deliveryPrice": "116795.39864682",  
                    "deliveryTime": "1754697600000"  
                },  
                {  
                    "deliveryPrice": "116880.31622213",  
                    "deliveryTime": "1754611200000"  
                },  
                {  
                    "deliveryPrice": "114782.09402227",  
                    "deliveryTime": "1754524800000"  
                },  
                {  
                    "deliveryPrice": "114212.80688625",  
                    "deliveryTime": "1754438400000"  
                },  
                {  
                    "deliveryPrice": "114046.80650192",  
                    "deliveryTime": "1754352000000"  
                },  
                {  
                    "deliveryPrice": "114668.76736223",  
                    "deliveryTime": "1754265600000"  
                },  
                {  
                    "deliveryPrice": "113691.29780823",  
                    "deliveryTime": "1754179200000"  
                },  
                {  
                    "deliveryPrice": "113947.55450439",  
                    "deliveryTime": "1754092800000"  
                },  
                {  
                    "deliveryPrice": "114786.86096974",  
                    "deliveryTime": "1754006400000"  
                },  
                {  
                    "deliveryPrice": "118693.64929462",  
                    "deliveryTime": "1753920000000"  
                },  
                {  
                    "deliveryPrice": "118218.22353841",  
                    "deliveryTime": "1753833600000"  
                },  
                {  
                    "deliveryPrice": "118953.66791589",  
                    "deliveryTime": "1753747200000"  
                },  
                {  
                    "deliveryPrice": "118894.70314174",  
                    "deliveryTime": "1753660800000"  
                },  
                {  
                    "deliveryPrice": "118137.86446229",  
                    "deliveryTime": "1753574400000"  
                },  
                {  
                    "deliveryPrice": "117344.01937262",  
                    "deliveryTime": "1753488000000"  
                },  
                {  
                    "deliveryPrice": "115166.35343924",  
                    "deliveryTime": "1753401600000"  
                },  
                {  
                    "deliveryPrice": "118217.70562761",  
                    "deliveryTime": "1753315200000"  
                },  
                {  
                    "deliveryPrice": "118444.57154255",  
                    "deliveryTime": "1753228800000"  
                },  
                {  
                    "deliveryPrice": "118155.53638794",  
                    "deliveryTime": "1753142400000"  
                },  
                {  
                    "deliveryPrice": "119370.88939816",  
                    "deliveryTime": "1753056000000"  
                },  
                {  
                    "deliveryPrice": "118080.35649338",  
                    "deliveryTime": "1752969600000"  
                },  
                {  
                    "deliveryPrice": "118197.36884665",  
                    "deliveryTime": "1752883200000"  
                },  
                {  
                    "deliveryPrice": "119644.49252705",  
                    "deliveryTime": "1752796800000"  
                },  
                {  
                    "deliveryPrice": "118316.40871555",  
                    "deliveryTime": "1752710400000"  
                },  
                {  
                    "deliveryPrice": "118216.19126195",  
                    "deliveryTime": "1752624000000"  
                },  
                {  
                    "deliveryPrice": "116746.02994227",  
                    "deliveryTime": "1752537600000"  
                },  
                {  
                    "deliveryPrice": "122778.73513717",  
                    "deliveryTime": "1752451200000"  
                },  
                {  
                    "deliveryPrice": "117973.83741111",  
                    "deliveryTime": "1752364800000"  
                },  
                {  
                    "deliveryPrice": "117741.30111399",  
                    "deliveryTime": "1752278400000"  
                },  
                {  
                    "deliveryPrice": "117851.19238216",  
                    "deliveryTime": "1752192000000"  
                },  
                {  
                    "deliveryPrice": "111263.21196833",  
                    "deliveryTime": "1752105600000"  
                },  
                {  
                    "deliveryPrice": "108721.62176788",  
                    "deliveryTime": "1752019200000"  
                },  
                {  
                    "deliveryPrice": "108410.57999842",  
                    "deliveryTime": "1751932800000"  
                },  
                {  
                    "deliveryPrice": "108969.06709828",  
                    "deliveryTime": "1751846400000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1756110714178  
    }

---

# 查詢期權歷史交割價格

查詢平台期權歷史交割價格，支持期權

> **覆蓋範圍: 期權**

信息

  * 建議結算完成後1分鐘後查詢此接口，因為此接口返回的資料可能會延遲1分鐘。
  * 默認返回最近50筆記錄，以"deliveryTime"倒序排列。



### HTTP請求

GET`/v5/market/new-delivery-price`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. 僅支持`option`  
baseCoin| **true**|  string| 交易貨幣. 默認: `BTC`. 僅支持`option`  
settleCoin| false| string| 結算貨幣，僅限大寫。默認：`USDT`。  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> deliveryPrice| string| 交割價格  
> deliveryTime| string| 交割時間戳 (毫秒)  
  
* * *

### 請求示例

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/new-delivery-price?category=option&baseCoin=BTC HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
      
    
    
    
      
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "option",  
            "list": [  
                {  
                    "deliveryPrice": "111675.89830854",  
                    "deliveryTime": "1756080000000"  
                },  
                {  
                    "deliveryPrice": "114990.41430239",  
                    "deliveryTime": "1755993600000"  
                },  
                {  
                    "deliveryPrice": "115792.27557281",  
                    "deliveryTime": "1755907200000"  
                },  
                {  
                    "deliveryPrice": "113162.32041387",  
                    "deliveryTime": "1755820800000"  
                },  
                {  
                    "deliveryPrice": "113852.00497157",  
                    "deliveryTime": "1755734400000"  
                },  
                {  
                    "deliveryPrice": "113604.53226162",  
                    "deliveryTime": "1755648000000"  
                },  
                {  
                    "deliveryPrice": "114828.99222851",  
                    "deliveryTime": "1755561600000"  
                },  
                {  
                    "deliveryPrice": "115321.04746356",  
                    "deliveryTime": "1755475200000"  
                },  
                {  
                    "deliveryPrice": "117969.66726839",  
                    "deliveryTime": "1755388800000"  
                },  
                {  
                    "deliveryPrice": "117622.21555318",  
                    "deliveryTime": "1755302400000"  
                },  
                {  
                    "deliveryPrice": "118846.72206411",  
                    "deliveryTime": "1755216000000"  
                },  
                {  
                    "deliveryPrice": "121778.983223",  
                    "deliveryTime": "1755129600000"  
                },  
                {  
                    "deliveryPrice": "119383.31934289",  
                    "deliveryTime": "1755043200000"  
                },  
                {  
                    "deliveryPrice": "119030.19489407",  
                    "deliveryTime": "1754956800000"  
                },  
                {  
                    "deliveryPrice": "121725.4933271",  
                    "deliveryTime": "1754870400000"  
                },  
                {  
                    "deliveryPrice": "117780.91332268",  
                    "deliveryTime": "1754784000000"  
                },  
                {  
                    "deliveryPrice": "116795.39864682",  
                    "deliveryTime": "1754697600000"  
                },  
                {  
                    "deliveryPrice": "116880.31622213",  
                    "deliveryTime": "1754611200000"  
                },  
                {  
                    "deliveryPrice": "114782.09402227",  
                    "deliveryTime": "1754524800000"  
                },  
                {  
                    "deliveryPrice": "114212.80688625",  
                    "deliveryTime": "1754438400000"  
                },  
                {  
                    "deliveryPrice": "114046.80650192",  
                    "deliveryTime": "1754352000000"  
                },  
                {  
                    "deliveryPrice": "114668.76736223",  
                    "deliveryTime": "1754265600000"  
                },  
                {  
                    "deliveryPrice": "113691.29780823",  
                    "deliveryTime": "1754179200000"  
                },  
                {  
                    "deliveryPrice": "113947.55450439",  
                    "deliveryTime": "1754092800000"  
                },  
                {  
                    "deliveryPrice": "114786.86096974",  
                    "deliveryTime": "1754006400000"  
                },  
                {  
                    "deliveryPrice": "118693.64929462",  
                    "deliveryTime": "1753920000000"  
                },  
                {  
                    "deliveryPrice": "118218.22353841",  
                    "deliveryTime": "1753833600000"  
                },  
                {  
                    "deliveryPrice": "118953.66791589",  
                    "deliveryTime": "1753747200000"  
                },  
                {  
                    "deliveryPrice": "118894.70314174",  
                    "deliveryTime": "1753660800000"  
                },  
                {  
                    "deliveryPrice": "118137.86446229",  
                    "deliveryTime": "1753574400000"  
                },  
                {  
                    "deliveryPrice": "117344.01937262",  
                    "deliveryTime": "1753488000000"  
                },  
                {  
                    "deliveryPrice": "115166.35343924",  
                    "deliveryTime": "1753401600000"  
                },  
                {  
                    "deliveryPrice": "118217.70562761",  
                    "deliveryTime": "1753315200000"  
                },  
                {  
                    "deliveryPrice": "118444.57154255",  
                    "deliveryTime": "1753228800000"  
                },  
                {  
                    "deliveryPrice": "118155.53638794",  
                    "deliveryTime": "1753142400000"  
                },  
                {  
                    "deliveryPrice": "119370.88939816",  
                    "deliveryTime": "1753056000000"  
                },  
                {  
                    "deliveryPrice": "118080.35649338",  
                    "deliveryTime": "1752969600000"  
                },  
                {  
                    "deliveryPrice": "118197.36884665",  
                    "deliveryTime": "1752883200000"  
                },  
                {  
                    "deliveryPrice": "119644.49252705",  
                    "deliveryTime": "1752796800000"  
                },  
                {  
                    "deliveryPrice": "118316.40871555",  
                    "deliveryTime": "1752710400000"  
                },  
                {  
                    "deliveryPrice": "118216.19126195",  
                    "deliveryTime": "1752624000000"  
                },  
                {  
                    "deliveryPrice": "116746.02994227",  
                    "deliveryTime": "1752537600000"  
                },  
                {  
                    "deliveryPrice": "122778.73513717",  
                    "deliveryTime": "1752451200000"  
                },  
                {  
                    "deliveryPrice": "117973.83741111",  
                    "deliveryTime": "1752364800000"  
                },  
                {  
                    "deliveryPrice": "117741.30111399",  
                    "deliveryTime": "1752278400000"  
                },  
                {  
                    "deliveryPrice": "117851.19238216",  
                    "deliveryTime": "1752192000000"  
                },  
                {  
                    "deliveryPrice": "111263.21196833",  
                    "deliveryTime": "1752105600000"  
                },  
                {  
                    "deliveryPrice": "108721.62176788",  
                    "deliveryTime": "1752019200000"  
                },  
                {  
                    "deliveryPrice": "108410.57999842",  
                    "deliveryTime": "1751932800000"  
                },  
                {  
                    "deliveryPrice": "108969.06709828",  
                    "deliveryTime": "1751846400000"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1756110714178  
    }