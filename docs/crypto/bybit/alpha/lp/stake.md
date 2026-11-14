---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/stake
api_type: REST
updated_at: 2026-11-13 19:21:07.675589
---

# Execute LP Stake

Stake tokens into a liquidity pool to provide liquidity and earn rewards.

info

  * Must call [Get Pay Token List](/docs/v5/alpha/trade/pay-token-list) to verify available balance before staking
  * Must display stake details (amount, fees, expected APY) to user and obtain explicit confirmation before calling this endpoint
  * `200` response is only an ACK — use [Get Order List](/docs/v5/alpha/trade/order-list) to check final position status
  * Supports new position creation (`positionId=0`) or adding liquidity to an existing position
  * Either use `rangeLower`/`rangeUpper` OR `priceLower`/`priceUpper`, not both
  * Position activation typically takes 10–60 seconds for on-chain confirmation
  * **Rate Limit:** 1 req/s (per user), 2000 req/s (global)



### HTTP Request

POST`/v5/alpha/lp/stake`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
positionId| **true**|  integer| Position ID. Use `0` to create a new position, or provide an existing position ID to add liquidity  
poolAddress| **true**|  string| Pool contract address  
payTokenAmount| **true**|  string| Payment token amount (positive decimal as string)  
payTokenCode| **true**|  string| Payment token code, e.g. `CEX_1` for USDT  
rangeUpper| false| string| Range order upper limit. Use this OR `priceUpper`, not both  
rangeLower| false| string| Range order lower limit. Use this OR `priceLower`, not both  
priceUpper| false| string| Price order upper limit (price priority). Use this OR `rangeUpper`, not both  
priceLower| false| string| Price order lower limit (price priority). Use this OR `rangeLower`, not both  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
positionId| integer| Position ID (new or existing)  
orderNo| string| Order number for this stake operation  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/stake HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "positionId": 0,  
        "poolAddress": "0x1234567890abcdef",  
        "payTokenAmount": "1000",  
        "payTokenCode": "CEX_1",  
        "rangeUpper": "2000",  
        "rangeLower": "1800"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positionId": 12345,  
            "orderNo": "LP_ORD_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 執行 LP 質押

向流動性礦池質押代幣以提供流動性並賺取收益。

信息

  * 質押前必須先調用 [查詢支付代幣列表](/docs/zh-TW/v5/alpha/trade/pay-token-list) 確認可用餘額
  * 必須向用戶展示質押詳情（金額、費用、預期 APY）並獲得明確確認後，才能調用此接口
  * `200` 響應僅為確認回執 — 請使用 [查詢訂單列表](/docs/zh-TW/v5/alpha/trade/order-list) 確認最終倉位狀態
  * 支持新建倉位（`positionId=0`）或向已有倉位追加流動性
  * `rangeLower`/`rangeUpper` 和 `priceLower`/`priceUpper` 二選一，不可同時使用
  * 倉位激活通常需要 10–60 秒的鏈上確認時間
  * **頻率限制：** 1 次/秒（用戶），2000 次/秒（全局）



### HTTP 請求

POST`/v5/alpha/lp/stake`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
positionId| **true**|  integer| 倉位ID。傳 `0` 新建倉位，傳已有倉位ID則追加流動性  
poolAddress| **true**|  string| 礦池合約地址  
payTokenAmount| **true**|  string| 支付代幣數量（正數小數字符串）  
payTokenCode| **true**|  string| 支付代幣代碼，如 `CEX_1` 代表 USDT  
rangeUpper| false| string| 範圍訂單上限。與 `priceUpper` 二選一，不可同時使用  
rangeLower| false| string| 範圍訂單下限。與 `priceLower` 二選一，不可同時使用  
priceUpper| false| string| 價格訂單上限（價格優先）。與 `rangeUpper` 二選一，不可同時使用  
priceLower| false| string| 價格訂單下限（價格優先）。與 `rangeLower` 二選一，不可同時使用  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
positionId| integer| 倉位ID（新建或已有）  
orderNo| string| 本次質押操作的訂單號  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/stake HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "positionId": 0,  
        "poolAddress": "0x1234567890abcdef",  
        "payTokenAmount": "1000",  
        "payTokenCode": "CEX_1",  
        "rangeUpper": "2000",  
        "rangeLower": "1800"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "positionId": 12345,  
            "orderNo": "LP_ORD_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }