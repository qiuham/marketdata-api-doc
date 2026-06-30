---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/position/auto-add-margin
api_type: Position
updated_at: 2026-06-30 19:29:24.436764
---

# Get Futures Leverage

Query isolated leverage setting for futures symbols. Unlike [Get Position Info](/docs/v5/position/v5/position), this endpoint does not require an open position to retrieve the leverage setting.

### HTTP Request

GET`/v5/position/symbol-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`(USDT Contract, USDC Contract), `inverse`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#category)| string| Product type  
list| array| Object  
> symbol| string| Symbol name  
> leverage| string| Leverage  
> side| string| Meaningless field, pls ignore. `Buy`, `Sell`, `""`  
> positionIdx| integer| Position mode. `0`: one-way; `1`: two-way Buy; `2`: two-way Sell  
  
info

Under Portfolio Margin mode, this endpoint returns an error.

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/position/symbol-info?category=linear&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672284128523  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "MNTUSDT",  
                    "leverage": "10",  
                    "side": "Sell",  
                    "positionIdx": 2  
                },  
                {  
                    "symbol": "MNTUSDT",  
                    "leverage": "10",  
                    "side": "Sell",  
                    "positionIdx": 1  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1781518340920  
    }

---

# 查詢合約槓桿

查詢合約交易對的逐倉槓桿設置。與[查詢持倉](/docs/zh-TW/v5/position/v5/position)不同，此接口無需持有倉位即可查詢槓桿設置。

### HTTP 請求

GET`/v5/position/symbol-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`(USDT合約, USDC合約), `inverse`  
symbol| false| string| 合約名稱，如 `BTCUSDT`，僅支持大寫  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#category)| string| 產品類型  
list| array| Object  
> symbol| string| 合約名稱  
> leverage| string| 槓桿倍數  
> side| string| 無意義, 可以忽略 `Buy`, `Sell`, `""`  
> positionIdx| integer| 持倉模式。`0`: 單向持倉；`1`: 雙向持倉-多頭；`2`: 雙向持倉-空頭  
  
信息

在組合保證金模式下，此接口會返回錯誤。

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/position/symbol-info?category=linear&symbol=BTCUSDT HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672284128523  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "linear",  
            "list": [  
                {  
                    "symbol": "MNTUSDT",  
                    "leverage": "10",  
                    "side": "Sell",  
                    "positionIdx": 2  
                },  
                {  
                    "symbol": "MNTUSDT",  
                    "leverage": "10",  
                    "side": "Sell",  
                    "positionIdx": 1  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1781518340920  
    }