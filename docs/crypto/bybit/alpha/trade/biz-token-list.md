---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/trade/biz-token-list
api_type: Trading
updated_at: 2026-11-13 19:21:20.949236
---

# Get Biz Token List

Query the list of on-chain tokens available for trading, with risk flags and order limits.

info

  * Returns token codes in `DEX_<id>` format used by [Get Trade Quote](/docs/v5/alpha/trade/trade-quote) and execution endpoints
  * `riskFlag=1` indicates risk — warn the user before proceeding to trade
  * `payTokenCodes` lists which payment tokens are supported for each trading token
  * To get token prices or market data, use [Get Token Price List](/docs/v5/alpha/trade/biz-token-price-list) instead



### HTTP Request

POST`/v5/alpha/trade/biz-token-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
tokenTag| false| integer| Token tag filter. `0`: All (default), `1`: New token sniping, `2`: On-chain hot token  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tokenCode| string| Token code in `DEX_<id>` format. Use this in quote and execution requests  
chainCode| string| Blockchain code, e.g. `ETH`, `BSC`, `SOL`, `TRX`, `BASE`  
chainIconUrl| string| Chain icon URL  
tokenAddress| string| Token contract address on chain  
symbol| string| Token symbol, e.g. `PEPE`  
tokenDecimals| integer| Token decimal precision  
tokenIconUrlDay| string| Token icon URL (light mode)  
tokenIconUrlNight| string| Token icon URL (dark mode)  
createTime| integer| Token listing time on platform (Unix timestamp in seconds)  
createTimeOnchain| integer| Token creation time on chain (Unix timestamp in seconds)  
riskFlag| integer| Risk flag. `0`: No risk identified, `1`: Risk identified — warn user before trading  
minOrderQuantity| number| Minimum order quantity (in payment token unit, e.g. USD)  
maxOrderQuantity| number| Maximum order quantity (in payment token unit)  
tokenTags| array| Tag ID list associated with this token  
payTokenCodes| array| Supported payment token codes (`CEX_<id>`), e.g. `["CEX_1", "CEX_2"]`  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/biz-token-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenTag": 2  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenCode": "DEX_123",  
                "chainCode": "ETH",  
                "chainIconUrl": "https://example.com/eth.png",  
                "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933",  
                "symbol": "PEPE",  
                "tokenDecimals": 18,  
                "tokenIconUrlDay": "https://example.com/pepe-day.png",  
                "tokenIconUrlNight": "https://example.com/pepe-night.png",  
                "createTime": 1704067200,  
                "createTimeOnchain": 1682000000,  
                "riskFlag": 0,  
                "minOrderQuantity": 1,  
                "maxOrderQuantity": 50000,  
                "tokenTags": [1, 2],  
                "payTokenCodes": ["CEX_1", "CEX_2"]  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取業務代幣列表

查詢可交易的鏈上代幣列表，包含風險標識及下單限制。

信息

  * 返回 `DEX_<id>` 格式的代幣代碼，供 [獲取交易報價](/docs/zh-TW/v5/alpha/trade/trade-quote) 及執行接口使用
  * `riskFlag=1` 表示存在風險 — 交易前須向用戶發出警告
  * `payTokenCodes` 列出每個交易代幣支持的支付代幣
  * 若需查詢代幣價格或行情數據，請使用 [獲取代幣價格列表](/docs/zh-TW/v5/alpha/trade/biz-token-price-list)



### HTTP 請求

POST`/v5/alpha/trade/biz-token-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
tokenTag| false| integer| 代幣標籤篩選。`0`: 全部（默認），`1`: 新幣狙擊，`2`: 鏈上熱門代幣  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tokenCode| string| `DEX_<id>` 格式的代幣代碼，用於報價及執行接口  
chainCode| string| 區塊鏈代碼，如 `ETH`、`BSC`、`SOL`、`TRX`、`BASE`  
chainIconUrl| string| 鏈圖標 URL  
tokenAddress| string| 鏈上代幣合約地址  
symbol| string| 代幣符號，如 `PEPE`  
tokenDecimals| integer| 代幣小數精度  
tokenIconUrlDay| string| 代幣圖標 URL（淺色模式）  
tokenIconUrlNight| string| 代幣圖標 URL（深色模式）  
createTime| integer| 代幣在平台上架時間（Unix 時間戳，秒）  
createTimeOnchain| integer| 代幣鏈上創建時間（Unix 時間戳，秒）  
riskFlag| integer| 風險標識。`0`: 無風險，`1`: 存在風險 — 交易前須警告用戶  
minOrderQuantity| number| 最小下單數量（以支付代幣單位計，如 USD）  
maxOrderQuantity| number| 最大下單數量（以支付代幣單位計）  
tokenTags| array| 該代幣關聯的標籤 ID 列表  
payTokenCodes| array| 支持的支付代幣代碼（`CEX_<id>`），如 `["CEX_1", "CEX_2"]`  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/biz-token-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "tokenTag": 2  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": [  
            {  
                "tokenCode": "DEX_123",  
                "chainCode": "ETH",  
                "chainIconUrl": "https://example.com/eth.png",  
                "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933",  
                "symbol": "PEPE",  
                "tokenDecimals": 18,  
                "tokenIconUrlDay": "https://example.com/pepe-day.png",  
                "tokenIconUrlNight": "https://example.com/pepe-night.png",  
                "createTime": 1704067200,  
                "createTimeOnchain": 1682000000,  
                "riskFlag": 0,  
                "minOrderQuantity": 1,  
                "maxOrderQuantity": 50000,  
                "tokenTags": [1, 2],  
                "payTokenCodes": ["CEX_1", "CEX_2"]  
            }  
        ],  
        "retExtInfo": {},  
        "time": 1704067200000  
    }