---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/option-asset-info
api_type: Account
updated_at: 2026-11-13 19:20:49.333105
---

# Get Option Asset Info

Query the option asset profit and loss information for each coin under the account.

### HTTP Request

GET`/v5/account/option-asset-info`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array<object>| Asset P&L info list  
> coin| string| Coin name  
> totalDelta| string| Total delta. Only includes delta from option **positions**  
> totalRPL| string| Total realised P&L  
> totalUPL| string| Total unrealised P&L  
> assetIM| string| Asset initial margin. Includes IM occupied by option **open orders**  
> assetMM| string| Asset maintenance margin. Includes MM occupied by option **open orders**  
> sendTime| number| Snapshot timestamp (ms)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/option-asset-info HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773230920000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "result": [  
                {  
                    "totalDelta": "0.0118",  
                    "assetIM": "0.0000",  
                    "totalUPL": "-47.6318",  
                    "totalRPL": "-0.2790",  
                    "assetMM": "0.0000",  
                    "coin": "BTC",  
                    "sendTime": 1773230923530  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1773230923533  
    }

---

# 查詢期權資產信息

查詢帳戶下各幣種的期權資產盈虧信息。

### HTTP 請求

GET`/v5/account/option-asset-info`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
result| array<object>| 資產盈虧信息列表  
> coin| string| 幣種  
> totalDelta| string| 總Delta。僅包含期權**持倉** 的總Delta  
> totalRPL| string| 總已實現盈虧  
> totalUPL| string| 總未實現盈虧  
> assetIM| string| 資產初始保證金。包含期權**掛單** 所占用的IM  
> assetMM| string| 資產維持保證金。包含期權**掛單** 所占用的MM  
> sendTime| number| 快照時間戳（毫秒）  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/option-asset-info HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773230920000  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "result": [  
                {  
                    "totalDelta": "0.0118",  
                    "assetIM": "0.0000",  
                    "totalUPL": "-47.6318",  
                    "totalRPL": "-0.2790",  
                    "assetMM": "0.0000",  
                    "coin": "BTC",  
                    "sendTime": 1773230923530  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1773230923533  
    }