---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/position-tiers
api_type: REST
updated_at: 2026-07-04 19:10:53.221397
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

# Unicorn! · GitHub