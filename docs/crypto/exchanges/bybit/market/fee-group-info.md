---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/fee-group-info
api_type: Market Data
updated_at: 2026-05-27 19:18:16.333390
---

# Get Index Price Components

### HTTP Request

GET`/v5/market/index-price-components`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
indexName| **true**|  string| Index name, like `BTCUSDT`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
indexName| string| Name of the index (e.g., BTCUSDT)  
lastPrice| string| Last price of the index  
updateTime| string| Timestamp of the last update in milliseconds  
components| array| List of components contributing to the index price  
> exchange| string| Name of the exchange  
> spotPair| string| Spot trading pair on the exchange (e.g., BTCUSDT)  
> equivalentPrice| string| Equivalent price  
> multiplier| string| Multiplier used for the component price  
> price| string| Actual price  
> weight| string| Weight in the index calculation  
  
### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/index-price-components?indexName=1000BTTUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_index_price_components(  
        indexName="1000BTTUSDT"  
    ))  
    
    
    
      
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
      "retCode": 0,  
      "retMsg": "",  
      "result": {  
        "indexName": "1000BTTUSDT",  
        "lastPrice": "0.0006496",  
        "updateTime": "1758182745072",  
        "components": [  
          {  
            "exchange": "GateIO",  
            "spotPair": "BTT_USDT",  
            "equivalentPrice": "0.0006485",  
            "multiplier": "1000",  
            "price": "0.0006485",  
            "weight": "0.1383220862762299"  
          },  
          {  
            "exchange": "Bybit",  
            "spotPair": "BTTUSDT",  
            "equivalentPrice": "0.0006502",  
            "multiplier": "1000",  
            "price": "0.0006502",  
            "weight": "0.0407528429737999"  
          },  
          {  
            "exchange": "Bitget",  
            "spotPair": "BTTUSDT",  
            "equivalentPrice": "0.000648",  
            "multiplier": "1000",  
            "price": "0.000648",  
            "weight": "0.1629044859431618"  
          },  
          {  
            "exchange": "BitMart",  
            "spotPair": "BTT_USDT",  
            "equivalentPrice": "0.000649",  
            "multiplier": "1000",  
            "price": "0.000649",  
            "weight": "0.0432327388538453"  
          },  
          {  
            "exchange": "Binance",  
            "spotPair": "BTTCUSDT",  
            "equivalentPrice": "0.00065",  
            "multiplier": "1000",  
            "price": "0.00065",  
            "weight": "0.5322401401714303"  
          },  
          {  
            "exchange": "Mexc",  
            "spotPair": "BTTUSDT",  
            "equivalentPrice": "0.0006517",  
            "multiplier": "1000",  
            "price": "0.0006517",  
            "weight": "0.0825477057815328"  
          }  
        ]  
      },  
      "retExtInfo": {},  
      "time": 1758182745621  
    }

---

# 獲取指數價格組成

### HTTP 請求

GET`/v5/market/index-price-components`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
indexName| **true**|  string| 指數名稱，例如 `BTCUSDT`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
indexName| string| 指數名稱（例如 BTCUSDT）  
lastPrice| string| 指數的最新價格  
updateTime| string| 最近更新的時間戳，單位為毫秒  
components| array| 構成指數價格的組成部分列表  
> exchange| string| 交易所名稱  
> spotPair| string| 交易所的現貨交易對（例如 BTCUSDT）  
> equivalentPrice| string| 等效價格  
> multiplier| string| 用於計算價格的乘數  
> price| string| 實際價格  
> weight| string| 指數計算中的權重  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/index-price-components?indexName=1000BTTUSDT HTTP/1.1    
    Host: api-testnet.bybit.com    
    
    
    
      
    
    
    
      
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {    
      "retCode": 0,    
      "retMsg": "",    
      "result": {    
        "indexName": "1000BTTUSDT",    
        "lastPrice": "0.0006496",    
        "updateTime": "1758182745072",    
        "components": [    
          {    
            "exchange": "GateIO",    
            "spotPair": "BTT_USDT",    
            "equivalentPrice": "0.0006485",    
            "multiplier": "1000",    
            "price": "0.0006485",    
            "weight": "0.1383220862762299"    
          },    
          {    
            "exchange": "Bybit",    
            "spotPair": "BTTUSDT",    
            "equivalentPrice": "0.0006502",    
            "multiplier": "1000",    
            "price": "0.0006502",    
            "weight": "0.0407528429737999"    
          },    
          {    
            "exchange": "Bitget",    
            "spotPair": "BTTUSDT",    
            "equivalentPrice": "0.000648",    
            "multiplier": "1000",    
            "price": "0.000648",    
            "weight": "0.1629044859431618"    
          },    
          {    
            "exchange": "BitMart",    
            "spotPair": "BTT_USDT",    
            "equivalentPrice": "0.000649",    
            "multiplier": "1000",    
            "price": "0.000649",    
            "weight": "0.0432327388538453"    
          },    
          {    
            "exchange": "Binance",    
            "spotPair": "BTTCUSDT",    
            "equivalentPrice": "0.00065",    
            "multiplier": "1000",    
            "price": "0.00065",    
            "weight": "0.5322401401714303"    
          },    
          {    
            "exchange": "Mexc",    
            "spotPair": "BTTUSDT",    
            "equivalentPrice": "0.0006517",    
            "multiplier": "1000",    
            "price": "0.0006517",    
            "weight": "0.0825477057815328"    
          }    
        ]    
      },    
      "retExtInfo": {},    
      "time": 1758182745621    
    }