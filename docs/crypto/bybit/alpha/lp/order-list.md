---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/alpha/lp/order-list
api_type: REST
updated_at: 2026-11-13 19:21:00.964283
---

# Get LP Order List

Query the user's LP order history (stake and redeem operations) with optional filters.

info

  * Use this endpoint after executing [Execute LP Stake](/docs/v5/alpha/lp/stake) or [Execute LP Redeem](/docs/v5/alpha/lp/redeem) to confirm order status
  * Orders are sorted by creation time descending
  * Maximum query range: 365 days
  * For current position details, use Get LP Position List instead
  * **Rate Limit:** 3 req/s (per user), 2000 req/s (global)



### HTTP Request

POST`/v5/alpha/lp/order-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderType| false| integer| Filter by order type. `0`: All (default), `1`: Stake, `2`: Redeem  
tokenCode| false| string| Filter by token code  
orderStatus| false| array| Filter by order status (multiple values allowed). `1`: Processing, `2`: Success, `3`: Failed  
days| false| integer| Query last N days. Default: `90`, Max: `365`  
limit| false| integer| Results per page. Default: `20`, Max: `100`  
pageIndex| false| integer| Page number (1-based). Default: `1`  
poolAddress| false| string| Filter by pool contract address  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
total| integer| Total order count matching the filter  
pageIndex| integer| Current page number  
orders| array| Order list  
> orderType| integer| Order type. `1`: Stake, `2`: Redeem  
> orderNo| string| System order number  
> orderStatus| integer| Order status. `1`: Processing, `2`: Success, `3`: Failed  
> poolAddress| string| Pool contract address  
> poolName| string| Pool name  
> positionId| integer| Associated position ID  
> tokenCode| string| Payment token code  
> tokenSymbol| string| Payment token symbol  
> tokenIconUrlDay| string| Token icon URL (light mode)  
> tokenIconUrlNight| string| Token icon URL (dark mode)  
> amount| string| Order amount  
> chainCode| string| Blockchain identifier  
> chainIconUrl| string| Blockchain icon URL  
> gasTokenSymbol| string| Gas token symbol  
> gasOnchain| string| On-chain gas fee  
> gasUsd| string| Gas fee in USD  
> platformFee| string| Platform fee  
> platformFeeUsd| string| Platform fee in USD  
> createTime| integer| Order creation time (Unix seconds)  
> executionTime| integer| Order completion time (Unix seconds)  
> failureReason| string| Failure reason; only present when `orderStatus` = `3`  
> dercRatio| string| Reduction ratio; only applicable for redeem orders  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/order-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderType": 0,  
        "days": 7,  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "total": 1,  
            "pageIndex": 1,  
            "orders": [  
                {  
                    "orderType": 1,  
                    "orderNo": "LP_ORD_20240101_001",  
                    "orderStatus": 2,  
                    "poolAddress": "0x1234567890abcdef",  
                    "poolName": "ETH-USDC Pool",  
                    "positionId": 12345,  
                    "tokenCode": "CEX_1",  
                    "tokenSymbol": "USDT",  
                    "tokenIconUrlDay": "",  
                    "tokenIconUrlNight": "",  
                    "amount": "1000",  
                    "chainCode": "",  
                    "chainIconUrl": "",  
                    "gasTokenSymbol": "",  
                    "gasOnchain": "",  
                    "gasUsd": null,  
                    "platformFee": "",  
                    "platformFeeUsd": null,  
                    "createTime": 1704067200,  
                    "executionTime": 1704067230,  
                    "failureReason": "",  
                    "dercRatio": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067300000  
    }

---

# 查詢 LP 訂單列表

查詢用戶的 LP 訂單歷史記錄（質押和贖回操作），支持可選條件過濾。

信息

  * 執行 [執行 LP 質押](/docs/zh-TW/v5/alpha/lp/stake) 或 [執行 LP 贖回](/docs/zh-TW/v5/alpha/lp/redeem) 後，可調用本接口確認訂單狀態
  * 訂單按創建時間倒序排列
  * 最大查詢範圍：365 天
  * 查詢當前倉位詳情請使用查詢 LP 倉位列表接口
  * **頻率限制：** 3 次/秒（用戶），2000 次/秒（全局）



### HTTP 請求

POST`/v5/alpha/lp/order-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderType| false| integer| 按訂單類型過濾。`0`: 全部（默認），`1`: 質押，`2`: 贖回  
tokenCode| false| string| 按代幣代碼過濾  
orderStatus| false| array| 按訂單狀態過濾（支持多值）。`1`: 處理中，`2`: 成功，`3`: 失敗  
days| false| integer| 查詢最近 N 天。默認: `90`，最大: `365`  
limit| false| integer| 每頁條數。默認: `20`，最大: `100`  
pageIndex| false| integer| 頁碼（從 1 開始）。默認: `1`  
poolAddress| false| string| 按礦池合約地址過濾  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
total| integer| 符合條件的訂單總數  
pageIndex| integer| 當前頁碼  
orders| array| 訂單列表  
> orderType| integer| 訂單類型。`1`: 質押，`2`: 贖回  
> orderNo| string| 系統訂單號  
> orderStatus| integer| 訂單狀態。`1`: 處理中，`2`: 成功，`3`: 失敗  
> poolAddress| string| 礦池合約地址  
> poolName| string| 礦池名稱  
> positionId| integer| 關聯倉位ID  
> tokenCode| string| 支付代幣代碼  
> tokenSymbol| string| 支付代幣符號  
> tokenIconUrlDay| string| 代幣圖標 URL（亮色模式）  
> tokenIconUrlNight| string| 代幣圖標 URL（暗色模式）  
> amount| string| 訂單金額  
> chainCode| string| 區塊鏈標識符  
> chainIconUrl| string| 區塊鏈圖標 URL  
> gasTokenSymbol| string| Gas 代幣符號  
> gasOnchain| string| 鏈上 Gas 費用  
> gasUsd| string| Gas 費用（USD）  
> platformFee| string| 平台費用  
> platformFeeUsd| string| 平台費用（USD）  
> createTime| integer| 訂單創建時間（Unix 秒）  
> executionTime| integer| 訂單完成時間（Unix 秒）  
> failureReason| string| 失敗原因；僅在 `orderStatus` = `3` 時有值  
> dercRatio| string| 減倉比例；僅適用於贖回訂單  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/alpha/lp/order-list HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1704067200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "orderType": 0,  
        "days": 7,  
        "limit": 20,  
        "pageIndex": 1  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "total": 1,  
            "pageIndex": 1,  
            "orders": [  
                {  
                    "orderType": 1,  
                    "orderNo": "LP_ORD_20240101_001",  
                    "orderStatus": 2,  
                    "poolAddress": "0x1234567890abcdef",  
                    "poolName": "ETH-USDC Pool",  
                    "positionId": 12345,  
                    "tokenCode": "CEX_1",  
                    "tokenSymbol": "USDT",  
                    "tokenIconUrlDay": "",  
                    "tokenIconUrlNight": "",  
                    "amount": "1000",  
                    "chainCode": "",  
                    "chainIconUrl": "",  
                    "gasTokenSymbol": "",  
                    "gasOnchain": "",  
                    "gasUsd": null,  
                    "platformFee": "",  
                    "platformFeeUsd": null,  
                    "createTime": 1704067200,  
                    "executionTime": 1704067230,  
                    "failureReason": "",  
                    "dercRatio": ""  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1704067300000  
    }