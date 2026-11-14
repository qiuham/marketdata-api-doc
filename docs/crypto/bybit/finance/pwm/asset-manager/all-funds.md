---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/asset-manager/all-funds
api_type: REST
updated_at: 2026-11-13 19:23:22.260356
---

# Get All Funds

info

Results are sorted by fund ID in **descending order** (newest first).

### HTTP Request

GET`/v5/earn/pwm/asset-manager/all-funds`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| Filter by coin  
fundId| false| string| Filter by fund ID. Only funds created by the institution via Open API can be queried  
status| false| string| Filter by status: `PendingSubscribe` / `Active` / `Closing` / `Closed`  
limit| false| integer| Page size. Default: `20`, max: `50`  
cursor| false| string| Pagination cursor (uses fund ID as cursor)  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Fund list  
> fundId| string| Unique fund identifier  
> fundName| string| Fund name  
> coin| string| Fund denomination coin  
> status| string| Fund status: `PendingSubscribe` / `Active` / `Closing` / `Closed`  
> totalEquity| string| Total fund equity (base coin)  
> totalShares| string| Total fund shares  
> currentNav| string| Current NAV (= shareValue / initialShareValue)  
> currentAPR| string| Current 30-day APR  
> accountUid| string| Main fund sub-account UID  
> subAccountList| array| Sub-account UIDs attached to this fund  
>> (element)| string| Sub-account UID  
> profitShareRate| string| Profit sharing rate (%), e.g. `"20.00"` means 20%  
> managementFeeRate| string| Management fee rate (annualized %), e.g. `"2.00"` means 2%  
> uncollectedProfit| string| Unsettled profit-sharing amount (base coin)  
> collectedProfit| string| Historically settled profit-sharing amount (base coin)  
> totalLoan| string| Current unsettled leverage amount (base coin)  
> createdTime| string| Fund creation timestamp (milliseconds)  
nextPageCursor| string| Next page cursor. Empty string indicates no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/pwm/asset-manager/all-funds HTTP/1.1  
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
                    "fundId": "123",  
                    "fundName": "BTC Alpha Fund",  
                    "coin": "BTC",  
                    "status": "active",  
                    "totalEquity": "10.5",  
                    "totalShares": "1000.00",  
                    "currentNav": "1.05",  
                    "accountUid": "456789",  
                    "subAccountList": ["456790", "456791"],  
                    "profitShareRate": "20.00",  
                    "managementFeeRate": "2.00",  
                    "uncollectedProfit": "0.5",  
                    "collectedProfit": "1.2",  
                    "totalLoan": "0",  
                    "createdTime": "1640000000000"  
                }  
            ],  
            "nextPageCursor": "32"  
        }  
    }

---

# 查詢機構管轄的基金列表

信息

返回數據按基金 ID **降序排列** （最新的在前）。

### HTTP 請求

GET`/v5/earn/pwm/asset-manager/all-funds`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 幣種篩選  
fundId| false| string| 基金ID篩選（該接口只能查詢機構 Open API 創建的基金）  
status| false| string| 狀態篩選：`PendingSubscribe`（待申購）/ `Active`（運行中）/ `Closing`（關閉中）/ `Closed`（已關閉）  
limit| false| integer| 每頁數量，默認 `20`，最大 `50`  
cursor| false| string| 分頁游標（使用基金ID作為游標）  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 基金列表  
> fundId| string| 基金唯一標識  
> fundName| string| 基金名稱  
> coin| string| 基金計價幣種  
> status| string| 基金狀態：`PendingSubscribe`（待申購）/ `Active`（運行中）/ `Closing`（關閉中）/ `Closed`（已關閉）  
> totalEquity| string| 基金總權益（本位幣）  
> totalShares| string| 基金總份額  
> currentNav| string| 當前淨值（nav = shareValue / initialShareValue）  
> currentAPR| string| 當前30日APR  
> accountUid| string| 主基金子賬戶UID  
> subAccountList| array| 當前基金附屬子賬戶UID列表  
>> (元素)| string| 子賬戶UID  
> profitShareRate| string| 利潤分成比例（%），如 `"20.00"` 表示20%  
> managementFeeRate| string| 管理費率（年化%），如 `"2.00"` 表示2%  
> uncollectedProfit| string| 當前未結算分潤的資產數量（本位幣）  
> collectedProfit| string| 歷史已結算分潤資產數量（本位幣）  
> totalLoan| string| 當前未結算的配資規模（本位幣）  
> createdTime| string| 基金創建時間戳（毫秒）  
nextPageCursor| string| 下一頁游標，為空表示無更多數據  
  
* * *

### 請求示例
    
    
    GET /v5/earn/pwm/asset-manager/all-funds HTTP/1.1  
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
                    "fundId": "123",  
                    "fundName": "BTC Alpha Fund",  
                    "coin": "BTC",  
                    "status": "active",  
                    "totalEquity": "10.5",  
                    "totalShares": "1000.00",  
                    "currentNav": "1.05",  
                    "accountUid": "456789",  
                    "subAccountList": ["456790", "456791"],  
                    "profitShareRate": "20.00",  
                    "managementFeeRate": "2.00",  
                    "uncollectedProfit": "0.5",  
                    "collectedProfit": "1.2",  
                    "totalLoan": "0",  
                    "createdTime": "1640000000000"  
                }  
            ],  
            "nextPageCursor": "32"  
        }  
    }