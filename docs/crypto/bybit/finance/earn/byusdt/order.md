---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/earn/byusdt/order
api_type: REST
updated_at: 2026-11-13 19:23:06.062353
---

# Get Order List

info

  * Pass `orderLinkId` or `orderId` alone to retrieve a single order. Omit both to query the full order list with optional filters.



### HTTP Request

GET`/v5/earn/token/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| Token coin. Currently only `BYUSDT` is supported  
orderLinkId| false| string| User-customised order ID. Pass to retrieve a single order  
orderId| false| string| System order ID. Pass to retrieve a single order  
orderType| false| string| Filter by order type: `Mint`, `Redeem`. Returns all types if omitted  
startTime| false| integer| Start timestamp in seconds. Default: 1 year ago  
endTime| false| integer| End timestamp in seconds. Default: current time  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from the previous response  
limit| false| integer| Number of items per page. Default: `20`, Max: `100`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Order list  
> orderId| string| System order ID  
> orderLinkId| string| User-customised order ID  
> orderType| string| Order type: `Mint`, `Redeem`. Note: TradFi-originated balance changes (e.g. close-PnL, commission, dividend) are also surfaced under `Redeem`. Use `externalEventType` to distinguish a TradFi-driven redemption from a user-initiated one  
> fromCoin| string| Source coin  
> toCoin| string| Destination coin  
> fromAmount| string| Source amount  
> toAmount| string| Amount credited (after deducting fees)  
> serviceFee| string| Service fee  
> fromAccount| string| Source account type. `Mint`: `FlexibleSaving`; `Redeem`: `UNIFIED`; `Redeem` (TradFi-originated): `TRADFI`  
> toAccount| string| Destination account type. `Mint`: `UNIFIED`; `Redeem`: `FlexibleSaving`; `Redeem` (TradFi-originated): `TRADFI`  
> externalEventType| string| External event that triggered the order. Empty for user-initiated orders. Populated only for TradFi (MT5) account events: `RPL_CLOSE` (realised PnL on position close, includes swap/overnight fee), `COMMISSION` (position-open commission), `DIVIDEND` (index dividend), `ROLLOVER` (contract rollover), `RISK_ADJUSTMENT` (risk-control adjustment)  
> status| string| Order status: `Success`, `Processing`, `Fail`  
> createdTime| string| Order creation time, unix timestamp in seconds  
nextPageCursor| string| Cursor for the next page. Empty string means no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/token/order?coin=BYUSDT HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "orderId": "9985caf3-7b24-452e-bb28-afbc5b52805f",  
                    "orderLinkId": "byusdt-order-001",  
                    "orderType": "Mint",  
                    "fromCoin": "USDT",  
                    "toCoin": "BYUSDT",  
                    "fromAmount": "108",  
                    "toAmount": "108",  
                    "serviceFee": "0",  
                    "status": "Success",  
                    "createdTime": "1775179628"  
                },  
                {  
                    "orderId": "63581995-4e3b-4ffa-9a20-c8415e7ed558",  
                    "orderLinkId": "",  
                    "orderType": "Mint",  
                    "fromCoin": "USDT",  
                    "toCoin": "BYUSDT",  
                    "fromAmount": "588",  
                    "toAmount": "588",  
                    "serviceFee": "0",  
                    "status": "Success",  
                    "createdTime": "1775177332"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775179790446  
    }

---

# 查詢訂單列表

信息

  * 單獨傳入 `orderLinkId` 或 `orderId` 可查詢單筆訂單。兩者均不傳入時，可搭配可選篩選條件查詢訂單列表。



### HTTP 請求

GET`/v5/earn/token/order`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 代幣幣種。目前僅支援 `BYUSDT`  
orderLinkId| false| string| 用戶自定義訂單 ID。傳入可查詢單筆訂單  
orderId| false| string| 系統訂單 ID。傳入可查詢單筆訂單  
orderType| false| string| 按訂單類型篩選：`Mint`、`Redeem`。不傳入時返回所有類型  
startTime| false| integer| 開始時間，秒級時間戳。預設：1 年前  
endTime| false| integer| 結束時間，秒級時間戳。預設：當前時間  
cursor| false| string| 分頁游標。使用上次響應中的 `nextPageCursor`  
limit| false| integer| 每頁返回數量。預設：`20`，最大：`100`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| 訂單列表  
> orderId| string| 系統訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> orderType| string| 訂單類型：`Mint`、`Redeem`。注意：TradFi 產生的餘額變動（如平倉盈虧、佣金、分紅等）也會以 `Redeem` 呈現，可透過 `externalEventType` 區分 TradFi 觸發的贖回與用戶主動贖回  
> fromCoin| string| 來源幣種  
> toCoin| string| 目標幣種  
> fromAmount| string| 來源金額  
> toAmount| string| 到帳金額（扣除手續費後）  
> serviceFee| string| 服務費  
> fromAccount| string| 資金來源帳戶類型。`Mint`：`FlexibleSaving`；`Redeem`：`UNIFIED`；`Redeem`（TradFi 觸發）：`TRADFI`  
> toAccount| string| 資金目標帳戶類型。`Mint`：`UNIFIED`；`Redeem`：`FlexibleSaving`；`Redeem`（TradFi 觸發）：`TRADFI`  
> externalEventType| string| 觸發訂單的外部事件類型。用戶主動操作時為空。僅在 TradFi（MT5）帳戶事件觸發時填入：`RPL_CLOSE`（平倉實現盈虧，含隔夜/掉期費）、`COMMISSION`（開倉佣金）、`DIVIDEND`（指數分紅）、`ROLLOVER`（合約換倉）、`RISK_ADJUSTMENT`（風控調整）  
> status| string| 訂單狀態：`Success`（成功）、`Processing`（處理中）、`Fail`（失敗）  
> createdTime| string| 訂單建立時間，秒級 Unix 時間戳  
nextPageCursor| string| 下一頁游標，為空表示無更多資料  
  
* * *

### 請求示例
    
    
    GET /v5/earn/token/order?coin=BYUSDT HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "orderId": "9985caf3-7b24-452e-bb28-afbc5b52805f",  
                    "orderLinkId": "byusdt-order-001",  
                    "orderType": "Mint",  
                    "fromCoin": "USDT",  
                    "toCoin": "BYUSDT",  
                    "fromAmount": "108",  
                    "toAmount": "108",  
                    "serviceFee": "0",  
                    "status": "Success",  
                    "createdTime": "1775179628"  
                },  
                {  
                    "orderId": "63581995-4e3b-4ffa-9a20-c8415e7ed558",  
                    "orderLinkId": "",  
                    "orderType": "Mint",  
                    "fromCoin": "USDT",  
                    "toCoin": "BYUSDT",  
                    "fromAmount": "588",  
                    "toAmount": "588",  
                    "serviceFee": "0",  
                    "status": "Success",  
                    "createdTime": "1775177332"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775179790446  
    }