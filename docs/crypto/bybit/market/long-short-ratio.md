---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/long-short-ratio
api_type: Market Data
updated_at: 2026-08-19 18:44:07.433903
---

# Get Order Price Limit

For derivative trading order price limit, refer to [announcement](https://announcements.bybit.com/en/article/update-contract-price-limit-enhancement-bltf9ebdcebe3089641/)  
For spot trading order price limit, refer to [announcement](https://announcements.bybit.com/en/article/title-adjustments-to-bybit-s-spot-trading-limit-order-mechanism-blt786c0c5abf865983/)  


### HTTP Request

GET`/v5/market/price-limit`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| false| string| Product type. `spot`,`linear`,`inverse`

  * When `category` is not passed, use `linear` by default

  
[symbol](/docs/v5/enum#symbol)| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
symbol| string| Symbol name  
buyLmt| string| Highest Bid Price  
sellLmt| string| Lowest Ask Price  
ts| string| timestamp in milliseconds  
  
### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/price-limit?category=linear&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_price_limit(  
        category="linear",  
        symbol="BTCUSDT",  
    ))  
    
    
    
      
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "symbol": "BTCUSDT",  
            "buyLmt": "105878.10",  
            "sellLmt": "103781.60",  
            "ts": "1750302284491"  
        },  
        "retExtInfo": {},  
        "time": 1750302285376  
    }

---

# 查詢訂單價格限制

衍生性商品交易訂單價格限制，請參考[公告](https://announcements.bybit.com/en/article/update-contract-price-limit-enhancement-bltf9ebdcebe3089641/)  
現貨交易訂單價格限制，請參考[公告](https://announcements.bybit.com/en/article/title-adjustments-to-bybit-s-spot-trading-limit-order-mechanism-blt786c0c5abf865983/)  


### HTTP請求

GET`/v5/market/price-limit`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| false| string| 產品類型. `spot`,`linear`,`inverse`

  * 當`category`不指定時, 默認是`linear`

  
[symbol](/docs/zh-TW/v5/enum#symbol)| **true**|  string| 合約名稱  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
symbol| string| 合約名稱  
buyLmt| string| 最高買價  
sellLmt| string| 最低賣價  
ts| string| 時間戳（以毫秒為單位）  
  
### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/price-limit?category=linear&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
    )  
    print(session.get_price_limit(  
        category="linear",  
        symbol="BTCUSDT",  
    ))  
    
    
    
      
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "symbol": "BTCUSDT",  
            "buyLmt": "105878.10",  
            "sellLmt": "103781.60",  
            "ts": "1750302284491"  
        },  
        "retExtInfo": {},  
        "time": 1750302285376  
    }