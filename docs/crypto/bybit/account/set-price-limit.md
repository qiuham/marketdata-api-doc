---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/set-price-limit
api_type: Account
updated_at: 2026-11-13 19:20:55.403242
---

# Set Price Limit Behaviour

You can configure how the system behaves when your limit order price exceeds the highest bid or lowest ask price. You can query your current configuration with [Get Trade Behaviour Setting](/docs/v5/account/get-user-setting-config). Learn more about the price limit for [spot](https://www.bybit.com/en/help-center/article/Bybit-Spot-Trading-Rules#A) and [futures](https://www.bybit.com/en/help-center/article?id=000002177#D) in the help centre.

* * *

Where x% is [priceLimitRatioX](/docs/v5/market/instrument); and y% is the [priceLimitRatioY](/docs/v5/market/instrument):

Spot

  * **Maximum buy price** : _Min[Max(Index Price, Index Price × (1 + x%) + 2-Minute Average Premium), Index Price × (1 + y%)]_
  * **Minimum sell price** : _Max[Min(Index Price, Index Price × (1 – x%) + 2-Minute Average Premium), Index Price × (1 – y%)]_



Futures

  * **Maximum Buy Price** = _min(Mark × (1 + Y), max(Index, Mark × (1 + X) + α × max(0, Premium_avg)))_
  * **Minimum Sell Price** = _max(Mark × (1 - Y), min(Index, Mark × (1 - X) + α × min(0, Premium_avg)))_



Where:

  * **Premium_avg** : Average order book premium over the past 30 seconds, calculated every second: _avg((Best Ask Price + Best Bid Price) / 2 − Mark Price)_
  * **α** : Weighting factor applied to the premium average. The default value is `1`. Bybit may dynamically adjust this parameter based on market conditions.



Default Setting

  * Spot: **modifyEnable = false.** If the order price exceeds the limit, the system rejects the request.   
Corresponds to [Get Limit Price Behaviour](https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config), where **lpaSpot = false, lpaPerp = true**

  * Futures: **modifyEnable = true.** If the order price exceeds the limit, the system will automatically adjust the price to the nearest allowed price (i.e., highest bid or lowest ask).  
Corresponds to [Get Limit Price Behaviour](https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config), where **lpaSpot = true, lpaPerp = false**

  * Setting either `linear` or `inverse` will set the behaviour for **all futures**.




### HTTP Request

POST`/v5/account/set-limit-px-action`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| `linear`, `inverse`, `spot`  
modifyEnable| **true**|  boolean| `true`: allow the system to modify the order price  
`false`: reject your order request  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-limit-px-action HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1753255927950  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
        "category": "spot",  
        "modifyEnable": true  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_limit_price_action(  
        category="spot",  
        modifyEnable=True,  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1753255927952  
    }

---

# 設置限價單行為

您可以設定當限價單價格超過最高買價或最低賣價時，系統的行為方式。 您可以使用[查詢交易行為設置](/docs/zh-TW/v5/account/get-user-setting-config)接口查詢限價單行為

現貨

  * **最高買入價格** : _Min[Max(指數價格, 指數價格 × (1 + y%) + 2分鐘平均溢價), 指數價格 × (1 + z%)]_
  * **最低賣出價格** : _Max[Min(指數價格, 指數價格 × (1 - y%) + 2分鐘平均溢價), 指數價格 × (1 - z%)]_



合約

  * **最高買入價格** = _min(標記價格 × (1 + Y), max(指數價格, 標記價格 × (1 + X) + α × max(0, Premium_avg)))_
  * **最低賣出價格** = _max(標記價格 × (1 - Y), min(指數價格, 標記價格 × (1 - X) + α × min(0, Premium_avg)))_



其中：

  * **Premium_avg** ：過去 30 秒訂單簿溢價的平均值，每秒計算一次： _avg((最優賣價 + 最優買價) / 2 − 標記價格)_
  * **α** ：溢價均值的加權因子，預設值為 `1`，Bybit 可能根據市場情況動態調整此參數。



預設設定

  * 現貨: **modifyEnable = false.** 若下單價格超出限制範圍，系統將拒絕該請求   
對應[Get Limit Price Behaviour](https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config)接口返回值：**lpaSpot = false , lpaPerp = true**

  * 合約: **modifyEnable = true.** 若下單價格超出限制範圍，系統會自動將價格調整至允許的最近邊界（即最高買價或最低賣價）。   
對應[Get Limit Price Behaviour](https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config)接口返回值：**lpaSpot = true , lpaPerp = false**

  * 設定 `linear` 或 `inverse` 會對整個**合約** 生效  





### HTTP 請求

POST`/v5/account/set-limit-px-action`

### 請求參數

參數| 類型| 說明| 默認值  
---|---|---|---  
category| **true**|  string| `linear`, `inverse`, `spot`  
modifyEnable| **true**|  boolean| `true`: 允許系統自動修改價格  
`false`: 拒絕請求  
  
### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-limit-px-action HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1753255927950  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
        "category": "spot",  
        "modifyEnable": true  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.set_limit_price_action(  
        category="spot",  
        modifyEnable=True,  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1753255927952  
    }