---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/repayment-available-amount
api_type: REST
updated_at: 2026-07-09 19:12:20.761454
---

# Set Auto Repay Mode

Set spot automatic repayment mode

info

  1. If `currency` is not passed, spot automatic repayment will be enabled for all currencies.
  2. If `autoRepayMode` of a currency is set to 1, the system will automatically make repayments without asset conversion to that currency at 0 and 30 minutes every hour.
  3. The amount of repayments without asset conversion is the minimum of available spot balance in that currency and liability of that currency. 
  4. If you missed the automatic repayment batches for 0 and 30 minutes every hour, you can manually make the repayment via the API. Please refer to [Manual Repay Without Asset Conversion](/docs/v5/account/no-convert-repay)



### HTTP Request

POST`/v5/spot-margin-trade/set-auto-repay-mode`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| Coin name, uppercase only. If `currency` is not passed, spot automatic repayment will be enabled for all currencies.  
autoRepayMode| **true**|  string| 

  * `1`: On
  * `0`: Off

  
  
* * *

### Response Parameters

Parameter| Type| Comments  
---|---|---  
data| array| Object  
> currency| string| Coin name, uppercase only.  
> autoRepayMode| string| 

  * `1`: On
  * `0`: Off

  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/set-auto-repay-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672299806626  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "currency": "ETH",  
        "autoRepayMode":"1"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_auto_repay_mode(  
        currency="ETH",  
        autoRepayMode="1"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "data": [  
                {  
                    "currency": "ETH",  
                    "autoRepayMode": "1"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1766976677678  
    }

---

# 設定現貨自動還款模式

設定現貨自動還款模式

信息

  1. 若未指定`currency`參數，則所有幣種均啟用自動還款。
  2. 如果將某幣種的`autoRepayMode`設定為 1，系統將每小時 0 分鐘和 30 分鐘自動以該幣種進行非資產轉換還款。
  3. 無損還款金額為該貨幣的現貨可用餘額與該貨幣的負債中的較小者。
  4. 如果你錯過了0分和30分的自動還款批次，你可以手動調接口進行還款。



### HTTP 請求

POST`/v5/spot-margin-trade/set-auto-repay-mode`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| 幣名稱，僅限大寫. 若未指定`currency`參數，則所有幣種均啟用自動還款。  
autoRepayMode| **true**|  string| 

  * `1`: 開啟
  * `0`: 關閉

  
  
* * *

### 響應參數

參數| 類型| 說明  
---|---|---  
data| array| Object  
> currency| string| 幣名稱，僅限大寫.  
> autoRepayMode| string| 

  * `1`: 開啟
  * `0`: 關閉

  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/spot-margin-trade/set-auto-repay-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672299806626  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "currency": "ETH",  
        "autoRepayMode":"1"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "data": [  
                {  
                    "currency": "ETH",  
                    "autoRepayMode": "1"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1766976677678  
    }