---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/position-list
api_type: REST
updated_at: 2026-07-21 18:54:25.994956
---

# Execute LP Redeem

Redeem (withdraw) liquidity from a pool position.

info

  * Must call Get LP Position List to get a valid `positionId` before redeeming
  * Must display redemption details (amount, expected tokens, fees) to user and obtain explicit confirmation before calling this endpoint
  * `200` response is only an ACK — use [Get Order List](/docs/v5/alpha/trade/order-list) to check redemption status
  * Redeemed tokens are returned to user's wallet after on-chain confirmation (typically 10–60 seconds)
  * Partial or full redemption supported via `dercRatio`
  * **Rate Limit:** 1 req/s (per user), 2000 req/s (global)



### HTTP Request

POST`/v5/alpha/lp/redeem`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
positionId| **true**|  integer| Position ID (from Get LP Position List)  
poolAddress| **true**|  string| Pool contract address  
dercRatio| **true**|  string| Reduction ratio (0–1). `"0.25"` = redeem 25%, `"0.5"` = redeem 50%, `"1"` = close entire position  
receiveTokenCode| false| string| Token code for receiving the redeemed amount  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderNo| string| Order number for this redemption operation. Use this to track status via [Get Order List](/docs/v5/alpha/trade/order-list)  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/redeem HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "positionId": 12345,  
        "poolAddress": "0x1234567890abcdef",  
        "dercRatio": "0.5"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderNo": "LP_REDEEM_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 執行 LP 贖回

從流動性礦池倉位中贖回（提取）流動性。

信息

  * 贖回前必須先調用查詢 LP 倉位列表接口獲取有效的 `positionId`
  * 必須向用戶展示贖回詳情（金額、預期代幣、費用）並獲得明確確認後，才能調用此接口
  * `200` 響應僅為確認回執 — 請使用 [查詢訂單列表](/docs/zh-TW/v5/alpha/trade/order-list) 確認最終贖回狀態
  * 鏈上確認後代幣將返回至用戶錢包（通常需要 10–60 秒）
  * 支持部分或全部倉位贖回（通過 `dercRatio` 指定比例）
  * **頻率限制：** 1 次/秒（用戶），2000 次/秒（全局）



### HTTP 請求

POST`/v5/alpha/lp/redeem`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
positionId| **true**|  integer| 倉位ID（從查詢 LP 倉位列表接口獲取）  
poolAddress| **true**|  string| 礦池合約地址  
dercRatio| **true**|  string| 減倉比例（0–1）。`"0.25"` = 贖回 25%，`"0.5"` = 贖回 50%，`"1"` = 全部平倉  
receiveTokenCode| false| string| 接收贖回金額的代幣代碼  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderNo| string| 本次贖回操作的訂單號，可通過 [查詢訂單列表](/docs/zh-TW/v5/alpha/trade/order-list) 跟蹤狀態  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/redeem HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "positionId": 12345,  
        "poolAddress": "0x1234567890abcdef",  
        "dercRatio": "0.5"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderNo": "LP_REDEEM_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }