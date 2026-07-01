---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/easy-onchain/modify-position
api_type: REST
updated_at: 2026-07-01 19:28:44.984935
---

# Get Yield History

You can get the past 3 months data

info

API key needs "Earn" permission

### HTTP Request

GET`/v5/earn/yield`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`  
productId| false| string| Product ID. **Not supported when`category=OnChain`**; passing this parameter will result in an error.  
startTime| false| integer| The start timestamp (ms).

  * 1\. If both are not provided, the default is to return data from the last 7 days.
  * 2\. If both are provided, the difference between the endTime and startTime must be less than or equal to 7 days. 

  
endTime| false| integer| The endTime timestamp (ms)  
limit| false| integer| Limit for data size per page. Range: [1, 100]. Default: 50  
cursor| false| string| Cursor, use the returned `nextPageCursor` to query data for the next page.  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
nextPageCursor| string| Refer to the `cursor` request parameter  
list| array| Object  
> productId| string| Product ID  
> coin| string| Coin name: "BTC", "ETH"  
> id| string| Unique key (guaranteed to be unique only under the same user)  
> amount| string| Yield Amount.Example: 10  
> yieldType| string| Yield type: `Normal`, `Bonus` (Flexible saving only supports `Normal`)  
> distributionMode| string| Distribution type: `Auto`, `Manual`, `Reinvest`

  * `Auto`: Automatically distributed daily 
  * `Manual`: Distributed when the user redeems 
  * `Reinvest`: Reinvestment (not yet available)

  
> effectiveStakingAmount| string| Effective staking amount, e.g., 1000.00  
> orderId| string| Redemption order UUID ,For `FlexibleSaving`,Only returns order ID if `distribution_mode` is `Manual`  
> status| string| Order status: `Pending`, `Success`, `Fail`  
> createdAt| string| Order creation time in milliseconds, e.g., 1684738540561  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/yield?category=FlexibleSaving HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739937044221  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_yield(  
        category="FlexibleSaving"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "yield": [  
                {  
                    "productId": "428",  
                    "coin": "USDT",  
                    "id": "1002096",  
                    "amount": "0.0608",  
                    "yieldType": "Normal",  
                    "distributionMode": "Manual",  
                    "effectiveStakingAmount": "1000",  
                    "orderId": "05a7012d-c4d6-493a-8c6b-023a1038944a",  
                    "status": "Success",  
                    "createdAt": "1759993805000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1759993815641  
    }

---

# 查詢收益歷史

您可以獲取過去3個月的收益歷史

信息

API key需要"理財""權限

### HTTP 請求

GET`/v5/earn/yield`

### 請求參數

參數名稱| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`,`OnChain`  
productId| false| string| 產品 ID。**當`category=OnChain` 時不支持傳入此參數**，否則會報錯。  
startTime| false| integer| 開始時間戳 (ms)

  * 如果未提供 startTime 和 endTime，默認返回最近 7 天的數據。
  * 如果提供了 startTime 和 endTime，則結束時間與開始時間的差值必須小於或等於 7 天。

  
endTime| false| integer| 結束時間戳 (ms)  
limit| false| integer| 每頁數據大小限制. 範圍：[1, 100]。默認值：50  
cursor| false| string| 游標，使用返回的 `nextPageCursor` 查詢下一頁的數據。  
  
### 響應參數

參數名稱| 類型| 說明  
---|---|---  
nextPageCursor| string| 游標，用於翻頁  
list| array|   
> productId| string| 產品 ID  
> coin| string| 幣種名稱："BTC", "ETH"  
> id| string| 唯一鍵（僅在同一用戶下保證唯一）  
> amount| string| 收益金額。例如：10  
> yieldType| string| 收益類型：`Normal`，`Bonus`（靈活僅支援 `Normal`）  
> distributionMode| string| 分配類型：`Auto`，`Manual`，`Reinvest`

  * `Auto`：每日自動分配 
  * `Manual`：用戶贖回時分配 
  * `Reinvest`：复投（尚不可用）

  
>effectiveStakingAmount| string| 有效持倉金額，例如：1000.00  
> orderId| string| 贖回訂單 UUID，对于`FlexibleSaving`,僅當 `distribution_mode` 為 `Manual` 時返回訂單 ID  
> status| string| 訂單狀態：`Pending`，`Success`，`Fail`  
> createdAt| string| 訂單創建時間 (ms)，例如：1684738540561  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/yield?category=FlexibleSaving HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1739937044221  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "yield": [  
                {  
                    "productId": "428",  
                    "coin": "USDT",  
                    "id": "1002096",  
                    "amount": "0.0608",  
                    "yieldType": "Normal",  
                    "distributionMode": "Manual",  
                    "effectiveStakingAmount": "1000",  
                    "orderId": "05a7012d-c4d6-493a-8c6b-023a1038944a",  
                    "status": "Success",  
                    "createdAt": "1759993805000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1759993815641  
    }