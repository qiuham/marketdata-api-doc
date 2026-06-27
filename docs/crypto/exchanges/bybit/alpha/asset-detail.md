---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/asset-detail
api_type: REST
updated_at: 2026-05-27 19:14:29.788414
---

# Get Token Details

Query detailed information for a specific on-chain token, including description, social links, and risk flags.

info

  * Token is identified by `chainCode` \+ `tokenAddress` — get these from [Get Biz Token List](/docs/v5/alpha/biz-token-list) or [Get Asset List](/docs/v5/alpha/asset-list)
  * `riskFlag=1` indicates risk — warn the user before trading
  * When `showMessage=1`, display the `content` notification to the user; if `linkName` and `linkAddress` are provided, include the link
  * Only returns tokens with `status=1` (Listed) or `status=2` (Delisting)



### HTTP Request

POST`/v5/alpha/trade/biz-token-details`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
chainCode| **true**|  string| Blockchain code, e.g. `ETH`, `SOL`, `BSC`  
tokenAddress| **true**|  string| Token contract address on the specified chain  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
tokenCode| string| Token code in `DEX_<id>` format  
chainCode| string| Blockchain code  
chainIconUrl| string| Chain icon URL  
tokenAddress| string| Token contract address  
symbol| string| Token symbol  
tokenDecimals| integer| Token decimal precision  
tokenIconUrlDay| string| Token icon URL (light mode)  
tokenIconUrlNight| string| Token icon URL (dark mode)  
minOrderQuantity| string| Minimum order quantity  
maxOrderQuantity| string| Maximum order quantity  
maxPositionQuantity| string| Maximum position quantity per user  
tokenDesc| string| Token project description  
xUrl| string| X (Twitter) profile URL  
officialUrl| string| Official website URL  
whitePaperUrl| string| Whitepaper URL  
tokenTag| integer| Token tag. `0`: No tag, `1`: New token sniping, `2`: On-chain hot token  
riskFlag| integer| Risk flag. `0`: No risk, `1`: Risk identified — warn user before trading  
createTimeOnchain| integer| On-chain creation time (Unix timestamp in seconds)  
status| integer| Token status. `0`: Not listed, `1`: Listed, `2`: Delisting, `3`: In delivery, `4`: Delisted  
tokenTags| array| Tag ID list  
showMessage| integer| Whether to display a notification. `0`: No notification, `1`: Display notification  
content| string| Notification message content. Present when `showMessage=1`  
linkName| string| Notification link display name. Present when `showMessage=1`  
linkAddress| string| Notification link URL. Present when `showMessage=1`  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/biz-token-details HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "chainCode": "ETH",  
        "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tokenCode": "DEX_123",  
            "chainCode": "ETH",  
            "chainIconUrl": "https://example.com/eth.png",  
            "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933",  
            "symbol": "PEPE",  
            "tokenDecimals": 18,  
            "tokenIconUrlDay": "https://example.com/pepe-day.png",  
            "tokenIconUrlNight": "https://example.com/pepe-night.png",  
            "minOrderQuantity": "1",  
            "maxOrderQuantity": "50000",  
            "maxPositionQuantity": "100000",  
            "tokenDesc": "PEPE is a meme token on Ethereum.",  
            "xUrl": "https://x.com/pepecoineth",  
            "officialUrl": "https://www.pepe.vip",  
            "whitePaperUrl": "",  
            "tokenTag": 2,  
            "riskFlag": 0,  
            "createTimeOnchain": 1682000000,  
            "status": 1,  
            "tokenTags": [1, 2],  
            "showMessage": 0  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }

---

# 獲取代幣詳情

查詢指定鏈上代幣的詳細信息，包含項目描述、社交鏈接及風險標識。

信息

  * 代幣通過 `chainCode` \+ `tokenAddress` 識別 — 可從 [獲取業務代幣列表](/docs/zh-TW/v5/alpha/biz-token-list) 或 [查詢資產列表](/docs/zh-TW/v5/alpha/asset-list) 獲取
  * `riskFlag=1` 表示存在風險 — 交易前須向用戶發出警告
  * 當 `showMessage=1` 時，需向用戶展示 `content` 通知內容；若存在 `linkName` 和 `linkAddress`，需同時展示鏈接
  * 僅返回 `status=1`（已上線）或 `status=2`（下線中）的代幣



### HTTP 請求

POST`/v5/alpha/trade/biz-token-details`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
chainCode| **true**|  string| 區塊鏈代碼，如 `ETH`、`SOL`、`BSC`  
tokenAddress| **true**|  string| 指定鏈上的代幣合約地址  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
tokenCode| string| `DEX_<id>` 格式的代幣代碼  
chainCode| string| 區塊鏈代碼  
chainIconUrl| string| 鏈圖標 URL  
tokenAddress| string| 代幣合約地址  
symbol| string| 代幣符號  
tokenDecimals| integer| 代幣小數精度  
tokenIconUrlDay| string| 代幣圖標 URL（淺色模式）  
tokenIconUrlNight| string| 代幣圖標 URL（深色模式）  
minOrderQuantity| string| 最小下單數量  
maxOrderQuantity| string| 最大下單數量  
maxPositionQuantity| string| 用戶最大持倉數量  
tokenDesc| string| 代幣項目描述  
xUrl| string| X（Twitter）主頁 URL  
officialUrl| string| 官方網站 URL  
whitePaperUrl| string| 白皮書 URL  
tokenTag| integer| 代幣標籤。`0`: 無標籤，`1`: 新幣狙擊，`2`: 鏈上熱門代幣  
riskFlag| integer| 風險標識。`0`: 無風險，`1`: 存在風險 — 交易前須警告用戶  
createTimeOnchain| integer| 鏈上創建時間（Unix 時間戳，秒）  
status| integer| 代幣狀態。`0`: 未上線，`1`: 已上線，`2`: 下線中，`3`: 交割中，`4`: 已下線  
tokenTags| array| 標籤 ID 列表  
showMessage| integer| 是否顯示通知。`0`: 無通知，`1`: 顯示通知  
content| string| 通知消息內容，`showMessage=1` 時存在  
linkName| string| 通知鏈接顯示名稱，`showMessage=1` 時存在  
linkAddress| string| 通知鏈接 URL，`showMessage=1` 時存在  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/trade/biz-token-details HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "chainCode": "ETH",  
        "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "tokenCode": "DEX_123",  
            "chainCode": "ETH",  
            "chainIconUrl": "https://example.com/eth.png",  
            "tokenAddress": "0x6982508145454ce325ddbe47a25d4ec3d2311933",  
            "symbol": "PEPE",  
            "tokenDecimals": 18,  
            "tokenIconUrlDay": "https://example.com/pepe-day.png",  
            "tokenIconUrlNight": "https://example.com/pepe-night.png",  
            "minOrderQuantity": "1",  
            "maxOrderQuantity": "50000",  
            "maxPositionQuantity": "100000",  
            "tokenDesc": "PEPE is a meme token on Ethereum.",  
            "xUrl": "https://x.com/pepecoineth",  
            "officialUrl": "https://www.pepe.vip",  
            "whitePaperUrl": "",  
            "tokenTag": 2,  
            "riskFlag": 0,  
            "createTimeOnchain": 1682000000,  
            "status": 1,  
            "tokenTags": [1, 2],  
            "showMessage": 0  
        },  
        "retExtInfo": {},  
        "time": 1704067200000  
    }