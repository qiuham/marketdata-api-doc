---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/repay
api_type: Account
updated_at: 2026-06-28 19:07:35.224806
---

# Set Delta Neutral Mode

Delta Neutral Mode is designed to enhance the trading experience for users running delta-neutral strategies. When enabled, positions that meet the Delta Neutral criteria are ranked lower in the ADL (Auto-Deleveraging) queue, reducing the risk of being auto-deleveraged during extreme market conditions. For more details, refer to the [Delta Neutral Mode](https://www.bybit.com/en/help-center/article?id=1772092051700) help article.

You can turn on/off the Delta Neutral mode. To query the current status, use the [Get Trade Behaviour Config](/docs/v5/account/get-user-setting-config) endpoint and check the `deltaEnable` field in the response.

### HTTP Request

POST`/v5/account/set-delta-mode`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
deltaEnable| **true**|  string| `1`: Enable; `0`: Disable  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
resultStatus| integer| `success`;`failed`  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-delta-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773113846000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 20  
      
    {  
        "deltaEnable": "1"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_delta_mode(  
        deltaEnable="1"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1773113846355  
    }

---

# 設置Delta中性模式

Delta 中性模式旨在為執行 Delta 中性策略的用戶，提升交易體驗。啟用後，符合 Delta 中性標準的倉位在 ADL (自動減倉) 佇列中的排名會較低，從而降低在極端市場條件下被自動減倉的風險。 詳情請參考 [Delta 中性模式](https://www.bybit.com/en/help-center/article?id=1772092051700)幫助文章。

您可以開啟或關閉 Delta 中性模式。如需查詢當前狀態，請使用 [查詢交易行為設置](/docs/zh-TW/v5/account/get-user-setting-config) 接口，並查看響應中的 `deltaEnable` 字段。

### HTTP 請求

POST`/v5/account/set-delta-mode`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
deltaEnable| **true**|  string| `1`: 開啟；`0`: 關閉  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
resultStatus| integer| `success`;`failed`  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-delta-mode HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1773113846000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 20  
      
    {  
        "deltaEnable": "1"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1773113846355  
    }