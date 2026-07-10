---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/rwa/order
api_type: REST
updated_at: 2026-07-10 19:02:29.927616
---

# Get Order List

info

  * Pass `orderId` or `orderLinkId` alone to perform an exact lookup; other filters are ignored.
  * For paginated listing: `startTime` defaults to 7 days ago, `endTime` defaults to now. The earliest accessible time is 180 days ago.
  * **Rate Limit:** 10 req/s (UID)



### HTTP Request

GET`/v5/earn/rwa/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| System order ID for exact lookup (highest priority)  
orderLinkId| false| string| User-defined order ID for exact lookup (used when `orderId` is empty)  
orderType| false| string| Order type filter: `Stake`, `Redeem`  
productId| false| integer| Product ID filter  
startTime| false| integer| Start timestamp (Unix seconds). Default: 7 days ago; earliest: 180 days ago  
endTime| false| integer| End timestamp (Unix seconds). Default: now  
limit| false| integer| Number of records per page. Default: `20`, max: `50`  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from the previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Order list  
> orderId| string| System order ID  
> orderLinkId| string| User-defined idempotency key  
> orderType| string| Order type: `Stake`, `Redeem`  
> productId| integer| Product ID  
> coin| string| Settlement coin  
> stakeAmount| string| Stake amount (only present for Stake orders)  
> redeemShares| string| Redeem share quantity (only present for Redeem orders)  
> status| string| Order status: `Processing`, `Success`, `Failed`  
> accountType| string| Source/destination account: `FUND`, `UNIFIED`  
> createdTime| integer| Creation timestamp (Unix seconds)  
> updatedTime| integer| Last update timestamp (Unix seconds)  
> settledShares| string| Final confirmed share quantity (only present for successful Stake orders)  
> settledAmount| string| Final settled amount (only present for successful Redeem orders)  
nextPageCursor| string| Cursor for the next page; empty string indicates the last page  
  
* * *

### Request Example
    
    
    GET /v5/earn/rwa/order?orderType=Stake&limit=20 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1710691200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "orderId": "550e8400-e29b-41d4-a716-446655440000",  
                    "orderLinkId": "my-stake-001",  
                    "orderType": "Stake",  
                    "productId": 1001,  
                    "coin": "USDC",  
                    "stakeAmount": "100",  
                    "status": "Success",  
                    "accountType": "FUND",  
                    "createdTime": 1710691200,  
                    "updatedTime": 1710694800,  
                    "settledShares": "97.560975"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzNDU2fQ=="  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }

---

# 獲取訂單列表

信息

  * 單獨傳入 `orderId` 或 `orderLinkId` 可進行精確查詢，其他篩選條件將被忽略。
  * 分頁列表查詢：`startTime` 默認為 7 天前，`endTime` 默認為當前時間；最早可查詢 180 天前的數據。
  * **頻率限制：** 10 次/秒（UID）



### HTTP 請求

GET`/v5/earn/rwa/order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 系統訂單 ID，用於精確查詢（優先級最高）  
orderLinkId| false| string| 用戶自定義訂單 ID，用於精確查詢（`orderId` 為空時生效）  
orderType| false| string| 訂單類型篩選：`Stake`、`Redeem`  
productId| false| integer| 產品 ID 篩選  
startTime| false| integer| 起始時間戳（Unix 秒）。默認：7 天前；最早：180 天前  
endTime| false| integer| 結束時間戳（Unix 秒）。默認：當前時間  
limit| false| integer| 每頁記錄數。默認：`20`，最大：`50`  
cursor| false| string| 分頁遊標。使用上一次響應中的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 訂單列表  
> orderId| string| 系統訂單 ID  
> orderLinkId| string| 用戶自定義冪等鍵  
> orderType| string| 訂單類型：`Stake`、`Redeem`  
> productId| integer| 產品 ID  
> coin| string| 結算幣種  
> stakeAmount| string| 認購金額（僅 Stake 訂單返回）  
> redeemShares| string| 贖回份額數量（僅 Redeem 訂單返回）  
> status| string| 訂單狀態：`Processing`（處理中）、`Success`（成功）、`Failed`（失敗）  
> accountType| string| 資金賬戶：`FUND`、`UNIFIED`  
> createdTime| integer| 創建時間戳（Unix 秒）  
> updatedTime| integer| 最後更新時間戳（Unix 秒）  
> settledShares| string| 最終確認份額數量（僅 Stake 成功訂單返回）  
> settledAmount| string| 最終結算金額（僅 Redeem 成功訂單返回）  
nextPageCursor| string| 下一頁遊標；空字符串表示已是最後一頁  
  
* * *

### 請求示例
    
    
    GET /v5/earn/rwa/order?orderType=Stake&limit=20 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1710691200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "orderId": "550e8400-e29b-41d4-a716-446655440000",  
                    "orderLinkId": "my-stake-001",  
                    "orderType": "Stake",  
                    "productId": 1001,  
                    "coin": "USDC",  
                    "stakeAmount": "100",  
                    "status": "Success",  
                    "accountType": "FUND",  
                    "createdTime": 1710691200,  
                    "updatedTime": 1710694800,  
                    "settledShares": "97.560975"  
                }  
            ],  
            "nextPageCursor": "eyJpZCI6MTIzNDU2fQ=="  
        },  
        "retExtInfo": {},  
        "time": 1710691200000  
    }