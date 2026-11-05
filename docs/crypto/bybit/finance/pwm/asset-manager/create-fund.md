---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/asset-manager/create-fund
api_type: REST
updated_at: 2026-11-05 18:37:06.328454
---

# Create Fund (Pending Subscription)

info

  1. Each institution can create a maximum of **10 funds**.
  2. A newly created fund will have a status of **`PendingSubscribe`** (pending subscription).



### HTTP Request

POST`/v5/earn/pwm/asset-manager/create-fund`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
fundName| **true**|  string| Fund name, 1–50 characters  
coin| **true**|  string| Base coin. Supported values: `BTC`, `ETH`, `USDT`, `USDC`, `SOL`, `MNT`, `XRP`  
profitShareRate| **true**|  string| High-watermark profit sharing rate (%), range: 0–100  
managementFeeRate| **true**|  string| Management fee rate (annualized %), range: 0–100  
fundIntroduction| false| string| Fund introduction ID (must be in the institution's allowed list)  
reqLinkId| **true**|  string| User-defined request ID, max 36 characters, used for idempotency  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
fundId| string| Unique identifier of the newly created fund  
fundName| string| Fund name  
coin| string| Fund denomination coin  
status| string| Fund status. Fixed as `PendingSubscription` upon creation. Possible values: `PendingSubscribe` / `Active` / `Closing` / `Closed`  
profitShareRate| string| Profit sharing rate (%)  
managementFeeRate| string| Management fee rate (annualized %)  
accountUid| string| Fund main sub-account UID automatically created by the system  
createdTime| string| Creation timestamp (milliseconds)  
  
* * *

### Request Example
    
    
    POST /v5/earn/pwm/asset-manager/create-fund HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "fundName": "BTC Alpha Fund",  
        "coin": "BTC",  
        "profitShareRate": "20.00",  
        "managementFeeRate": "2.00",  
        "reqLinkId": "create-fund-001"  
    }  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "fundId": "12345",  
            "fundName": "BTC Alpha Fund",  
            "coin": "BTC",  
            "status": "pending_subscribe",  
            "profitShareRate": "20.00",  
            "managementFeeRate": "2.00",  
            "accountUid": "0",  
            "createdTime": "1640000000000"  
        }  
    }

---

# 機構創建待申購基金

信息

  1. 每個機構最多創建 **10 個基金** 。
  2. 基金創建後狀態為 **`PendingSubscribe`** （待申購）。



### HTTP 請求

POST`/v5/earn/pwm/asset-manager/create-fund`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
fundName| **true**|  string| 基金名稱，長度1-50字符  
coin| **true**|  string| 本位幣，支持：`BTC`、`ETH`、`USDT`、`USDC`、`SOL`、`MNT`、`XRP`  
profitShareRate| **true**|  string| 高水位利潤分成比例（%），範圍0-100  
managementFeeRate| **true**|  string| 管理費率（年化%），範圍0-100  
fundIntroduction| false| string| 基金簡介ID（需在機構允許列表中）  
reqLinkId| **true**|  string| 用戶自定義請求ID，最長36字符，用於冪等  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
fundId| string| 新創建的基金唯一標識  
fundName| string| 基金名稱  
coin| string| 基金計價幣種  
status| string| 基金狀態，創建後固定為 `PendingSubscription`（待申購）。枚舉值：`PendingSubscribe`（待申購）/ `Active`（運行中）/ `Closing`（關閉中）/ `Closed`（已關閉）  
profitShareRate| string| 利潤分成比例（%）  
managementFeeRate| string| 管理費率（年化%）  
accountUid| string| 系統自動創建的基金主子賬戶UID  
createdTime| string| 創建時間戳（毫秒）  
  
* * *

### 請求示例
    
    
    POST /v5/earn/pwm/asset-manager/create-fund HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "fundName": "BTC Alpha Fund",  
        "coin": "BTC",  
        "profitShareRate": "20.00",  
        "managementFeeRate": "2.00",  
        "reqLinkId": "create-fund-001"  
    }  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "fundId": "12345",  
            "fundName": "BTC Alpha Fund",  
            "coin": "BTC",  
            "status": "pending_subscribe",  
            "profitShareRate": "20.00",  
            "managementFeeRate": "2.00",  
            "accountUid": "0",  
            "createdTime": "1640000000000"  
        }  
    }