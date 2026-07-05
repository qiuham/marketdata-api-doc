---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/pwm/investment-plan/order
api_type: REST
updated_at: 2026-07-05 19:09:05.095731
---

# Get Investment Plan Orders

Query subscription / redemption / auto-reinvest orders under the current user's investment plans. Supports filtering by plan, product category, order type, status, and date range.

info

Orders are sorted by creation time in **descending order** (newest first).

### HTTP Request

GET`/v5/earn/pwm/investment-plan/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
planId| false| string| Investment plan ID. Returns orders for all plans if omitted  
category| false| string| Product type filter: `flexibleSavings` / `fundPool` / `fundPoolPremium` / `equityFund` / `onchainEarn`. Returns all if omitted  
type| false| string| Order type filter: `Subscribe` / `Redeem`. Returns all if omitted  
status| false| string| Order status filter: `Completed` / `Pending` / `Failed`. Returns all if omitted  
startTime| false| string| Start time in milliseconds. No lower limit if omitted  
endTime| false| string| End time in milliseconds. Defaults to current time if omitted  
limit| false| int| Page size. Default: `20`, max: `50`  
cursor| false| string| Pagination cursor  
orderLinkId| false| string| User-defined order ID, max 36 characters  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Order list  
> orderId| string| Unique order identifier (UUID format)  
> planId| string| Investment plan ID  
> type| string| Order type: `Subscribe` / `Redeem` / `AutoReinvest`  
> accountType| string| Source account type: `Funding` / `Unified`  
> coin| string| Order coin, e.g. `USDT`, `BTC`  
> amount| string| Order amount (base coin)  
> category| string| Product type: `flexibleSavings` / `fundPool` / `fundPoolPremium` / `equityFund` / `onchainEarn`  
> productId| string| Product ID  
> status| string| Order status: `Completed` / `Pending` / `Failed`  
> orderTime| string| Order creation timestamp (milliseconds), UTC  
nextPageCursor| string| Next page cursor. Empty string indicates no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/pwm/investment-plan/order?planId=10001&limit=20 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "result": {  
            "list": [  
                {  
                    "orderId": "a285b975-9968-4ba0-bd78-58430ead715f",  
                    "planId": "10001",  
                    "type": "Subscribe",  
                    "accountType": "Funding",  
                    "coin": "USDT",  
                    "amount": "100.0000",  
                    "category": "flexibleSavings",  
                    "productId": "11123",  
                    "status": "Completed",  
                    "orderTime": "1739519687000"  
                },  
                {  
                    "orderId": "f463ad6e-263c-499a-aff6-70c23be846ef",  
                    "planId": "10001",  
                    "type": "Subscribe",  
                    "accountType": "Funding",  
                    "coin": "BTC",  
                    "amount": "0.002000",  
                    "category": "equityFund",  
                    "productId": "11123",  
                    "status": "Completed",  
                    "orderTime": "1739519687000"  
                },  
                {  
                    "orderId": "98dc5a11-a578-49c2-830f-fc5d8c317ea7",  
                    "planId": "10005",  
                    "type": "AutoReinvest",  
                    "accountType": "Funding",  
                    "coin": "BTC",  
                    "amount": "10.409201",  
                    "category": "fundPool",  
                    "productId": "11123",  
                    "status": "Completed",  
                    "orderTime": "1739498401000"  
                }  
            ],  
            "nextPageCursor": ""  
        }  
    }

---

# 查詢投資計劃訂單列表

查詢當前用戶投資計劃下的申購 / 贖回 / 自動續投訂單列表，支持按投資計劃、產品類別、訂單類型、狀態及日期範圍等條件篩選。

信息

訂單按創建時間**降序排列** （最新訂單在前）。

### HTTP 請求

GET`/v5/earn/pwm/investment-plan/order`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
planId| false| string| 投資計劃ID，不傳返回全部計劃的訂單  
category| false| string| 產品類型篩選：`flexibleSavings` / `fundPool` / `fundPoolPremium` / `equityFund` / `onchainEarn`，不傳返回全部  
type| false| string| 訂單類型篩選：`Subscribe` / `Redeem`，不傳返回全部  
status| false| string| 訂單狀態篩選：`Completed`（已完成）/ `Pending`（處理中）/ `Failed`（失敗），不傳返回全部  
startTime| false| string| 起始時間毫秒時間戳，不傳默認無限制  
endTime| false| string| 結束時間毫秒時間戳，不傳默認為當前時間  
limit| false| int| 分頁大小，默認 `20`，最大 `50`  
cursor| false| string| 分頁游標  
orderLinkId| false| string| 用戶自定義訂單ID，最長36字符  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 訂單列表  
> orderId| string| 訂單唯一標識（UUID格式）  
> planId| string| 所屬投資計劃ID  
> type| string| 訂單類型：`Subscribe`（申購）/ `Redeem`（贖回）/ `AutoReinvest`（自動續投）  
> accountType| string| 資金來源賬戶類型：`Funding`（資金賬戶）/ `Unified`（統一交易賬戶）  
> coin| string| 訂單幣種，如 `USDT`、`BTC`  
> amount| string| 訂單金額（本位幣數量）  
> category| string| 產品類型：`flexibleSavings` / `fundPool` / `fundPoolPremium` / `equityFund` / `onchainEarn`  
> productId| string| 產品ID  
> status| string| 訂單狀態：`Completed`（已完成）/ `Pending`（處理中）/ `Failed`（失敗）  
> orderTime| string| 訂單創建時間戳（毫秒），UTC時間  
nextPageCursor| string| 下一頁游標，為空表示無更多數據  
  
* * *

### 請求示例
    
    
    GET /v5/earn/pwm/investment-plan/order?planId=10001&limit=20 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "result": {  
            "list": [  
                {  
                    "orderId": "a285b975-9968-4ba0-bd78-58430ead715f",  
                    "planId": "10001",  
                    "type": "Subscribe",  
                    "accountType": "Funding",  
                    "coin": "USDT",  
                    "amount": "100.0000",  
                    "category": "flexibleSavings",  
                    "productId": "11123",  
                    "status": "Completed",  
                    "orderTime": "1739519687000"  
                },  
                {  
                    "orderId": "f463ad6e-263c-499a-aff6-70c23be846ef",  
                    "planId": "10001",  
                    "type": "Subscribe",  
                    "accountType": "Funding",  
                    "coin": "BTC",  
                    "amount": "0.002000",  
                    "category": "equityFund",  
                    "productId": "11123",  
                    "status": "Completed",  
                    "orderTime": "1739519687000"  
                },  
                {  
                    "orderId": "98dc5a11-a578-49c2-830f-fc5d8c317ea7",  
                    "planId": "10005",  
                    "type": "AutoReinvest",  
                    "accountType": "Funding",  
                    "coin": "BTC",  
                    "amount": "10.409201",  
                    "category": "fundPool",  
                    "productId": "11123",  
                    "status": "Completed",  
                    "orderTime": "1739498401000"  
                }  
            ],  
            "nextPageCursor": ""  
        }  
    }