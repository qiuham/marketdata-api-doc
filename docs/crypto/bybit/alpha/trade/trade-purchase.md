---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/trade/trade-purchase
api_type: Trading
updated_at: 2026-11-13 19:21:23.985412
---

# Execute Purchase

Execute a buy trade to purchase on-chain tokens using payment tokens (e.g. USDT/USDC).

info

  * Must call [Get Trade Quote](/docs/v5/alpha/trade/trade-quote) first to get a valid quote
  * Must display quote details to the user and obtain explicit confirmation before calling this endpoint
  * Pass `quoteData`, `correctingCode`, and `gas` from the quote response as-is
  * A `200` response is only an acknowledgment — use [Get Order List](/docs/v5/alpha/trade/order-list) to check the final order status
  * Idempotent based on `quoteDataId` — duplicate submissions return the same order number
  * On-chain confirmation typically takes 10–60 seconds



### HTTP Request

POST`/v5/alpha/trade/purchase`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
fromTokenCode| **true**|  string| Payment token code (`CEX_<id>`), e.g. `CEX_1` for USDT. Must match the quote request  
fromTokenAmount| **true**|  string| Payment amount (positive decimal as string). Must match the quote request  
toTokenCode| **true**|  string| Target on-chain token code (`DEX_<id>`), e.g. `DEX_123`. Must match the quote request  
slippage| **true**|  string| Slippage tolerance as decimal. `0.005` = 0.5%, `0.01` = 1%, `0.05` = 5%  
quoteData| **true**|  string| Base64-encoded quote data. Must pass as-is from the `/quote` response  
gas| **true**|  string| Estimated gas fee. Must pass as-is from the `/quote` response  
quoteMode| **true**|  integer| Quote mode. Must be consistent with the `/quote` request. `0`: Auto, `1`: Price Priority, `2`: Success Rate Priority  
correctingCode| **true**|  string| MD5 checksum for data integrity. Must pass as-is from the `/quote` response  
tenant| false| string| Optional tenant identifier  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderNo| string| System-generated order number. Use this to query order status via [Get Order List](/docs/v5/alpha/trade/order-list)  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/purchase HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "fromTokenCode": "CEX_1",  
        "fromTokenAmount": "100",  
        "toTokenCode": "DEX_123",  
        "slippage": "0.01",  
        "quoteData": "eyJhbGciOiJIUzI1NiJ9...",  
        "gas": "0.0003",  
        "quoteMode": 0,  
        "correctingCode": "a1b2c3d4e5f6"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderNo": "ORD_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 執行購買

執行買入交易，使用支付代幣（如 USDT/USDC）購買鏈上代幣。

信息

  * 必須先調用 [獲取交易報價](/docs/zh-TW/v5/alpha/trade/trade-quote) 以獲取有效報價
  * 必須向用戶展示報價詳情並獲得明確確認後，才能調用此接口
  * `quoteData`、`correctingCode` 和 `gas` 必須原樣傳入來自報價接口的返回值
  * `200` 響應僅為確認回執 — 請使用 [查詢訂單列表](/docs/zh-TW/v5/alpha/trade/order-list) 確認最終訂單狀態
  * 基於 `quoteDataId` 的冪等性 — 重複提交將返回相同訂單號
  * 鏈上確認通常需要 10–60 秒



### HTTP 請求

POST`/v5/alpha/trade/purchase`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
fromTokenCode| **true**|  string| 支付代幣代碼（`CEX_<id>`），如 USDT 對應 `CEX_1`，須與報價請求一致  
fromTokenAmount| **true**|  string| 支付數量（正數小數字符串），須與報價請求一致  
toTokenCode| **true**|  string| 目標鏈上代幣代碼（`DEX_<id>`），如 `DEX_123`，須與報價請求一致  
slippage| **true**|  string| 滑點容忍度（小數形式）。`0.005` = 0.5%，`0.01` = 1%，`0.05` = 5%  
quoteData| **true**|  string| Base64 編碼的報價數據。必須原樣傳入來自 `/quote` 的返回值  
gas| **true**|  string| 預估 Gas 費用。必須原樣傳入來自 `/quote` 的返回值  
quoteMode| **true**|  integer| 報價模式，須與 `/quote` 請求一致。`0`: 自動，`1`: 價格優先，`2`: 成功率優先  
correctingCode| **true**|  string| 數據完整性 MD5 校驗碼。必須原樣傳入來自 `/quote` 的返回值  
tenant| false| string| 可選的租戶標識符  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderNo| string| 系統生成的訂單號，可通過 [查詢訂單列表](/docs/zh-TW/v5/alpha/trade/order-list) 查詢訂單狀態  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/purchase HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "fromTokenCode": "CEX_1",  
        "fromTokenAmount": "100",  
        "toTokenCode": "DEX_123",  
        "slippage": "0.01",  
        "quoteData": "eyJhbGciOiJIUzI1NiJ9...",  
        "gas": "0.0003",  
        "quoteMode": 0,  
        "correctingCode": "a1b2c3d4e5f6"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderNo": "ORD_20240101_001"  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }