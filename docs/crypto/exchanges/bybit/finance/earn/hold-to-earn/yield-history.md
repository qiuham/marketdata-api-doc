---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/hold-to-earn/yield-history
api_type: REST
updated_at: 2026-05-27 19:17:41.932622
---

# Get All Fund Orders

### HTTP Request

GET`/v5/earn/pwm/asset-manager/all-order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
fundId| false| string| Filter by fund ID. Returns orders for all managed funds if omitted  
orderType| false| string| Order type filter: `Subscribe` / `Redeem`. Returns all if omitted  
status| false| string| Order status filter: `Pending Review` / `Processing` / `Completed` / `Rejected` / `Failed`. Returns all if omitted  
startTime| false| integer| Start time in milliseconds. See time range rules below  
endTime| false| integer| End time in milliseconds. See time range rules below  
limit| false| integer| Page size. Default: `20`, max: `50`  
cursor| false| string| Pagination cursor (uses order `orderId` as cursor)  
  
Time Range Rules

  * Neither `startTime` nor `endTime` passed: returns data from the last 7 days
  * Both passed: returns data from `max(endTime - 7 days, startTime)` to `endTime`
  * Only `startTime` passed: returns data from `startTime` to `startTime + 7 days`
  * Only `endTime` passed: returns data from `endTime - 7 days` to `endTime`



### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Order list  
> orderId| string| Unique order identifier  
> fundId| string| Fund ID  
> fundName| string| Fund name  
> accountUid| string| Fund main sub-account UID  
> orderType| string| Order type: `Subscribe` / `Redeem`  
> coin| string| Coin  
> amount| string| Order amount (base coin). Subscription orders only; empty for redemption orders  
> shares| string| Order shares. Redemption orders only; empty for subscription orders  
> status| string| Order status: `PendingReview` / `Pass` / `Rejected` / `Processing` / `Success` / `Failed`  
> createdTime| string| Order creation timestamp (milliseconds)  
nextPageCursor| string| Next page cursor. Empty string indicates no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/pwm/asset-manager/all-order?fundId=100001&limit=20 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "orderId": "768",  
                    "fundId": "100001",  
                    "fundName": "Alpha BTC Strategy Fund",  
                    "accountUid": "800001",  
                    "orderType": "Subscribe",  
                    "coin": "BTC",  
                    "amount": "10.00000000",  
                    "shares": "",  
                    "status": "Completed",  
                    "createdTime": "1700000000000"  
                },  
                {  
                    "orderId": "769",  
                    "fundId": "100001",  
                    "fundName": "Alpha BTC Strategy Fund",  
                    "accountUid": "800002",  
                    "orderType": "Redeem",  
                    "coin": "BTC",  
                    "amount": "",  
                    "shares": "5000.00",  
                    "status": "Pending Review",  
                    "createdTime": "1700100000000"  
                }  
            ],  
            "nextPageCursor": ""  
        }  
    }

---

# 查詢機構相關基金全部訂單列表

### HTTP 請求

GET`/v5/earn/pwm/asset-manager/all-order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
fundId| false| string| 篩選基金ID，不傳返回所有管轄基金的訂單  
orderType| false| string| 訂單類型篩選：`Subscribe` / `Redeem`，不傳返回全部  
status| false| string| 訂單狀態篩選：`Pending Review` / `Processing` / `Completed` / `Rejected` / `Failed`，不傳返回全部  
startTime| false| integer| 起始時間毫秒時間戳，時間範圍規則見下方說明  
endTime| false| integer| 結束時間毫秒時間戳，時間範圍規則見下方說明  
limit| false| integer| 每頁數量，默認 `20`，最大 `50`  
cursor| false| string| 分頁游標（使用訂單 `orderId` 作為游標）  
  
時間範圍規則

  * `startTime` 和 `endTime` 都不傳：默認返回最近7天數據
  * 都傳入：查詢 `max(endTime - 7天, startTime)` 到 `endTime` 的數據
  * 只傳 `startTime`：查詢 `startTime` 到 `startTime + 7天` 的數據
  * 只傳 `endTime`：查詢 `endTime - 7天` 到 `endTime` 的數據



### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 訂單列表  
> orderId| string| 訂單唯一標識  
> fundId| string| 基金ID  
> fundName| string| 基金名稱  
> accountUid| string| 基金主子賬戶UID  
> orderType| string| 訂單類型：`Subscribe`（申購）/ `Redeem`（贖回）  
> coin| string| 幣種  
> amount| string| 訂單金額（本位幣），僅申購訂單有值，贖回訂單為空  
> shares| string| 訂單份額，僅贖回訂單有值，申購訂單為空  
> status| string| 訂單狀態：`PendingReview`（待審核）/ `Pass`（審核通過）/ `Rejected`（審核拒絕）/ `Processing`（處理中）/ `Success`（成功）/ `Failed`（失敗）  
> createdTime| string| 訂單創建時間戳（毫秒）  
nextPageCursor| string| 下一頁游標，為空表示無更多數據  
  
* * *

### 請求示例
    
    
    GET /v5/earn/pwm/asset-manager/all-order?fundId=100001&limit=20 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "orderId": "768",  
                    "fundId": "100001",  
                    "fundName": "Alpha BTC Strategy Fund",  
                    "accountUid": "800001",  
                    "orderType": "Subscribe",  
                    "coin": "BTC",  
                    "amount": "10.00000000",  
                    "shares": "",  
                    "status": "Completed",  
                    "createdTime": "1700000000000"  
                },  
                {  
                    "orderId": "769",  
                    "fundId": "100001",  
                    "fundName": "Alpha BTC Strategy Fund",  
                    "accountUid": "800002",  
                    "orderType": "Redeem",  
                    "coin": "BTC",  
                    "amount": "",  
                    "shares": "5000.00",  
                    "status": "Pending Review",  
                    "createdTime": "1700100000000"  
                }  
            ],  
            "nextPageCursor": ""  
        }  
    }