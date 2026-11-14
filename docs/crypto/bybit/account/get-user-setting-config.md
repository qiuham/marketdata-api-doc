---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config
api_type: Account
updated_at: 2026-11-13 19:20:49.242269
---

# Get Trade Behaviour Config

You can get configuration how the system behaves when your limit order price exceeds the highest bid or lowest ask price. The response also includes whether [Delta Neutral mode](/docs/v5/account/set-delta-mode) is enabled.

* * *

Where x% is [priceLimitRatioX](/docs/v5/market/instrument); and y% is the [priceLimitRatioY](/docs/v5/market/instrument):

Spot

  * **Maximum buy price** : _Min[Max(Index Price, Index Price × (1 + x%) + 2-Minute Average Premium), Index Price × (1 + y%)]_
  * **Minimum sell price** : _Max[Min(Index Price, Index Price × (1 – x%) + 2-Minute Average Premium), Index Price × (1 – y%)]_



Futures

  * **Maximum buy price** : _Min (Max (Index Price, Mark Price × (1 + x%)), Mark Price × (1 + y%))_
  * **Minimum sell price** : _Max (Min (Index Price, Mark Price × (1 - x%)), Mark Price × (1 - y%))_



Default Setting

  * Spot: **lpaSpot = false.** If the order price exceeds the limit, the system rejects the request.

  * Futures: **lpaPerp = false.** If the order price exceeds the limit, the system will automatically adjust the price to the nearest allowed price (i.e., highest bid or lowest ask).




### HTTP Request

GET`/v5/account/user-setting-config`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Object  
> lpaSpot| boolean| 

  * `true`: If the order price exceeds the limit, the system will automatically adjust the price to the nearest allowed price
  * `false`: If the order price exceeds the limit, the system rejects the request.

  
> lpaPerp| boolean| 

  * `true`: If the order price exceeds the limit, the system rejects the request.
  * `false`: If the order price exceeds the limit, the system will automatically adjust the price to the nearest allowed price.

  
> deltaEnable| boolean| Whether [Delta Neutral mode](/docs/v5/account/set-delta-mode) is enabled. `true`: enabled; `false`: disabled  
> smsef| boolean| Whether Spot MNT fee deduction is enabled. `true`: enabled; `false`: disabled  
> fmsef| boolean| Whether Futures MNT fee deduction is enabled. `true`: enabled; `false`: disabled  
> smpType| integer| User SMP (Self-Match Prevention) type configuration. `0`: Default, does not trigger self-match prevention; `1`: Cancel Taker order when self-match detected; `2`: Cancel Maker order when self-match detected; `3`: Cancel both Maker and Taker orders when self-match detected  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/user-setting-config HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1753255927950  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_user_setting_config())  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "lpaSpot": false,  
            "lpaPerp": false,  
            "smsef": false,  
            "fmsef": false,  
            "smpType": 0  
        },  
        "retExtInfo": {},  
        "time": 1773234932707  
    }

---

# 查詢交易行為設置

您可以查詢當限價單價格超過最高買價或最低賣價時，系統的行為方式。回傳結果同時包含 [Delta 中性模式](/docs/zh-TW/v5/account/set-delta-mode) 的開啟狀態。

現貨

  * **最高買入價格** : _Min[Max(指數價格, 指數價格 × (1 + y%) + 2分鐘平均溢價), 指數價格 × (1 + z%)]_
  * **最低賣出價格** : _Max[Min(指數價格, 指數價格 × (1 - y%) + 2分鐘平均溢價), 指數價格 × (1 - z%)]_



合約

  * **最高買入價格** : _min( max( 指數價格 , 標記價格 × (1 + x%) ), 標記價格 × (1 + y%) )_
  * **最低賣出價格** : *max( min( 指數價格 , 標記價格 × (1 - x%) ), 標記價格 × (1 - y%) )



預設設定

  * 現貨: **lpaSpot = false.** 若下單價格超出限制範圍，系統將拒絕該請求

  * 合約: **lpaPerp = false.** 若下單價格超出限制範圍，系統會自動將價格調整至允許的最近邊界（即最高買價或最低賣價）。




### HTTP 請求

GET`/v5/account/user-setting-config`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| Object  
> lpaSpot| boolean| 

  * `true`: 若下單價格超出限制範圍，系統會自動將價格調整至允許的最近邊界
  * `false`: 若下單價格超出限制範圍，系統將拒絕該請求

  
> lpaPerp| boolean| 

  * `true`: 若下單價格超出限制範圍，系統將拒絕該請求 
  * `false`: 若下單價格超出限制範圍，系統會自動將價格調整至允許的最近邊界

  
> deltaEnable| boolean| [Delta 中性模式](/docs/zh-TW/v5/account/set-delta-mode) 是否已開啟。`true`: 已開啟；`false`: 已關閉  
> smsef| boolean| 現貨MNT手續費抵扣開關。`true`: 已開啟；`false`: 已關閉  
> fmsef| boolean| 合約MNT手續費抵扣開關。`true`: 已開啟；`false`: 已關閉  
> smpType| integer| 用戶 SMP（自成交攔截）類型配置。`0`: 默認，不觸發自成交攔截；`1`: 自成交時取消 Taker 訂單；`2`: 自成交時取消 Maker 訂單；`3`: 自成交時同時取消 Maker 和 Taker 訂單  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/user-setting-config HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1753255927950  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_user_setting_config())  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "lpaSpot": false,  
            "lpaPerp": false,  
            "smsef": false,  
            "fmsef": false,  
            "smpType": 0  
        },  
        "retExtInfo": {},  
        "time": 1773234932707  
    }