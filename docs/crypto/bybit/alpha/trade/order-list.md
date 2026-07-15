---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/trade/order-list
api_type: Trading
updated_at: 2026-07-15 18:48:49.974308
---

# Get Payment Token List

Query available payment tokens (e.g. USDT, USDC) and their `CEX_<id>` token codes for on-chain trading.

info

  * Returns token codes in `CEX_<id>` format used by [Get Trade Quote](/docs/v5/alpha/trade/trade-quote) and execution endpoints
  * Each payment token lists supported chains via `supportChains`
  * To get on-chain tradable tokens, use [Get Biz Token List](/docs/v5/alpha/trade/biz-token-list) instead



### HTTP Request

POST`/v5/alpha/trade/pay-token-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
chainCode| **true**|  string| Blockchain code, e.g. `SOL`, `MANTLE`  
tokenAddress| **true**|  string| Token contract address on the specified chain  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tokenCode| string| Payment token code in `CEX_<id>` format. Use this in quote and execution requests  
symbol| string| Token symbol, e.g. `USDT`, `USDC`  
tokenDecimals| integer| Token decimal precision  
tokenIconUrlDay| string| Token icon URL (light mode)  
tokenIconUrlNight| string| Token icon URL (dark mode)  
limit| string| Maximum trading amount for this payment token  
supportChains| array| Supported blockchain codes, e.g. `["ETH", "BSC", "SOL"]`  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/pay-token-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "chainCode": "SOL",  
        "tokenAddress": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenCode": "CEX_1",  
                "symbol": "USDT",  
                "tokenDecimals": 6,  
                "tokenIconUrlDay": "https://example.com/usdt-day.png",  
                "tokenIconUrlNight": "https://example.com/usdt-night.png",  
                "limit": "50000",  
                "supportChains": ["ETH", "BSC", "SOL", "TRX"]  
            },  
            {  
                "tokenCode": "CEX_2",  
                "symbol": "USDC",  
                "tokenDecimals": 6,  
                "tokenIconUrlDay": "https://example.com/usdc-day.png",  
                "tokenIconUrlNight": "https://example.com/usdc-night.png",  
                "limit": "50000",  
                "supportChains": ["ETH", "SOL", "BASE"]  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取支付代幣列表

查詢可用的支付代幣（如 USDT、USDC）及其 `CEX_<id>` 代幣代碼，用於鏈上交易。

信息

  * 返回 `CEX_<id>` 格式的代幣代碼，供 [獲取交易報價](/docs/zh-TW/v5/alpha/trade/trade-quote) 及執行接口使用
  * 每個支付代幣通過 `supportChains` 列出支持的鏈
  * 若需查詢可交易的鏈上代幣，請使用 [獲取業務代幣列表](/docs/zh-TW/v5/alpha/trade/biz-token-list)



### HTTP 請求

POST`/v5/alpha/trade/pay-token-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
chainCode| **true**|  string| 區塊鏈代碼，如 `SOL`、`MANTLE`  
tokenAddress| **true**|  string| 指定鏈上的代幣合約地址  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tokenCode| string| `CEX_<id>` 格式的支付代幣代碼，用於報價及執行接口  
symbol| string| 代幣符號，如 `USDT`、`USDC`  
tokenDecimals| integer| 代幣小數精度  
tokenIconUrlDay| string| 代幣圖標 URL（淺色模式）  
tokenIconUrlNight| string| 代幣圖標 URL（深色模式）  
limit| string| 該支付代幣的最大交易金額  
supportChains| array| 支持的區塊鏈代碼列表，如 `["ETH", "BSC", "SOL"]`  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/pay-token-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "chainCode": "SOL",  
        "tokenAddress": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenCode": "CEX_1",  
                "symbol": "USDT",  
                "tokenDecimals": 6,  
                "tokenIconUrlDay": "https://example.com/usdt-day.png",  
                "tokenIconUrlNight": "https://example.com/usdt-night.png",  
                "limit": "50000",  
                "supportChains": ["ETH", "BSC", "SOL", "TRX"]  
            },  
            {  
                "tokenCode": "CEX_2",  
                "symbol": "USDC",  
                "tokenDecimals": 6,  
                "tokenIconUrlDay": "https://example.com/usdc-day.png",  
                "tokenIconUrlNight": "https://example.com/usdc-night.png",  
                "limit": "50000",  
                "supportChains": ["ETH", "SOL", "BASE"]  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }