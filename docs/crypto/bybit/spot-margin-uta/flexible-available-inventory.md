---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/flexible-available-inventory
api_type: REST
updated_at: 2026-10-21 18:49:56.213059
---

# Get Auto Repay Mode

Get spot automatic repayment mode

### HTTP Request

GET`/v5/spot-margin-trade/get-auto-repay-mode`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
currency| false| string| Coin name, uppercase only. If `currency` is not passed, automatic repay mode for all currencies will be returned.  
  
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


    
    
    GET /v5/spot-margin-trade/get-auto-repay-mode?currency=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672299806626  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_auto_repay_mode(  
        currency="ETH"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "data": [  
                {  
                    "autoRepayMode": "1",  
                    "currency": "ETH"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1766977353904  
    }

---

# 獲取現貨自動還款模式

獲取現貨自動還款模式

### HTTP 請求

GET`/v5/spot-margin-trade/get-auto-repay-mode`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
currency| false| string| 幣名稱，僅限大寫. 如果沒有指定 `currency` 參數，則返回所有貨幣自動還款模式。  
  
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


    
    
    GET /v5/spot-margin-trade/get-auto-repay-mode?currency=ETH HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672299806626  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "data": [  
                {  
                    "autoRepayMode": "1",  
                    "currency": "ETH"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1766977353904  
    }