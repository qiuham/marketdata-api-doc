---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/easy-onchain/coupons
api_type: REST
updated_at: 2026-06-30 19:26:41.466133
---

# Get Hourly Yield History

info

API key needs "Earn" permission

### HTTP Request

GET`/v5/earn/hourly-yield`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`  
productId| false| string| Product ID  
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
> amount| string| Yield Amount. Example: 10  
> effectiveStakingAmount| string| Effective staking amount, e.g., 1000.00  
> status| string| Order status: `Pending`, `Success`, `Fail`  
> hourlyDate| string| Hourly yield time(ms) eg: 1755478800000  
> createdAt| string| Order creation time in milliseconds, e.g., 1684738540561  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/hourly-yield?category=FlexibleSaving HTTP/1.1  
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
    print(session.get_hourly_yield(  
        category="FlexibleSaving"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "productId": "428",  
                    "coin": "USDT",  
                    "amount": "0.060810502283105022",  
                    "effectiveStakingAmount": "1000",  
                    "hourlyDate": "1759989600000",  
                    "status": "Success",  
                    "createdAt": "1759989603000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1759993045287  
    }

---

# 查詢每小時收益歷史

信息

API key需要"理財""權限

### HTTP 請求

GET`/v5/earn/hourly-yield`

### 請求參數

參數名稱| 必填| 類型| 說明  
---|---|---|---  
category| **true**|  string| `FlexibleSaving`  
productId| false| string| 產品 ID  
startTime| false| integer| 開始時間戳 (ms)。

  * 1\. 如果未提供 startTime 和 endTime，默認返回最近 7 天的數據。
  * 2\. 如果提供了 startTime 和 endTime，則結束時間與開始時間的差值必須小於或等於 7 天。

  
endTime| false| integer| 結束時間戳 (ms)  
limit| false| integer| 每頁數據大小限制。範圍：[1, 100]。默認值：50  
cursor| false| string| 游標，使用返回的 `nextPageCursor` 查詢下一頁的數據。  
  
### 響應參數

參數名稱| 類型| 說明  
---|---|---  
nextPageCursor| string| 游標，用於翻頁  
list| array|   
> productId| string| 產品 ID  
> coin| string| 幣種名稱："BTC", "ETH"  
> id| string| 唯一鍵（僅在同一用戶下保證唯一）  
> amount| string| 收益金額  
>effectiveStakingAmount| string| 有效持倉金額，例如：1000.00  
> status| string| 訂單狀態：`Pending`，`Success`，`Fail`  
> hourlyDate| string| 每小時收益時間 (ms)，例如：1755478800000  
> createdAt| string| 訂單創建時間 (ms)，例如：1684738540561  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/earn/hourly-yield?category=FlexibleSaving HTTP/1.1  
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
            "list": [  
                {  
                    "productId": "428",  
                    "coin": "USDT",  
                    "amount": "0.060810502283105022",  
                    "effectiveStakingAmount": "1000",  
                    "hourlyDate": "1759989600000",  
                    "status": "Success",  
                    "createdAt": "1759989603000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1759993045287  
    }