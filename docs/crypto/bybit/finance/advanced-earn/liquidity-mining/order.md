---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/liquidity-mining/order
api_type: REST
updated_at: 2026-11-13 19:22:56.140678
---

# Get Order Info

info

  * Need authentication. **Up to 10 requests** per second per UID. Requires Earn permission on the API key.
  * Pass `orderId` or `orderLinkId` alone to retrieve a single order. Omit both to query the order list with optional filters.



### HTTP Request

GET`/v5/earn/liquidity-mining/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Order ID. Pass to retrieve a single order (mutually exclusive with `orderLinkId` for exact lookup)  
orderLinkId| false| string| User-customised order ID. Pass to retrieve a single order  
productId| false| string| Filter by product ID  
orderType| false| string| Filter by order type: `AddLiquidity`, `RemoveLiquidity`, `Reinvest`, `AddMargin`  
startTime| false| string| Start time (order creation time), unix timestamp in milliseconds  
endTime| false| string| End time, unix timestamp in milliseconds  
status| false| string| Filter by status: `Success`, `Processing`. Returns all terminal statuses if not specified  
limit| false| integer| Number of items per page. Default: `20`, Max: `50`  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from the previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orders| array| Order list  
> orderId| string| Order ID  
> orderLinkId| string| User-customised order ID  
> productId| string| Product ID  
> orderType| string| Order type: `AddLiquidity`, `RemoveLiquidity`, `Reinvest`, `AddMargin`  
> baseCoin| string| Base coin  
> quoteCoin| string| Quote coin  
> quoteAmount| string| quoteCoin amount  
> baseAmount| string| baseCoin amount  
> status| string| Order status: `Success`, `Processing`, `Fail`  
> removeType| string| Withdrawal mode (only for `RemoveLiquidity`): `Normal`, `SingleQuoteCoin`, `SingleBaseCoin`  
> removeRate| integer| Withdrawal percentage, integer (only for `RemoveLiquidity`)  
> leverage| string| Leverage multiplier at order time (only for `AddLiquidity`)  
> slippageValue| string| Slippage deduction amount (only for `AddLiquidity`, populated after `Success`)  
> createdTime| string| Order creation time, unix timestamp in milliseconds  
nextPageCursor| string| Cursor for next page. Empty string means no more data  
  
* * *

### Request Example
    
    
    GET /v5/earn/liquidity-mining/order?orderLinkId=lm-001 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orders": [  
                {  
                    "orderId": "5e651d09-6169-4f72-a609-8622ff421d19",  
                    "orderLinkId": "lm-001",  
                    "productId": "36",  
                    "orderType": "AddLiquidity",  
                    "baseCoin": "TON",  
                    "quoteCoin": "USDT",  
                    "quoteAmount": "200",  
                    "baseAmount": "0",  
                    "status": "Success",  
                    "removeType": "Normal",  
                    "removeRate": 0,  
                    "leverage": "2",  
                    "slippageValue": "0.02",  
                    "createdTime": "1775123507000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775123797220  
    }

---

# 查詢訂單資訊

信息

  * 需要身份驗證。每個 UID 每秒**最多 10 次請求** 。API 金鑰需要具備 Earn（理財）權限。
  * 單獨傳入 `orderId` 或 `orderLinkId` 可查詢單筆訂單。兩者均不傳入時，可搭配可選篩選條件查詢訂單列表。



### HTTP 請求

GET`/v5/earn/liquidity-mining/order`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
orderId| false| string| 訂單 ID。傳入可查詢單筆訂單（與 `orderLinkId` 精確查詢互斥）  
orderLinkId| false| string| 用戶自定義訂單 ID。傳入可查詢單筆訂單  
productId| false| string| 按產品 ID 篩選  
orderType| false| string| 按訂單類型篩選：`AddLiquidity`、`RemoveLiquidity`、`Reinvest`、`AddMargin`  
startTime| false| string| 開始時間（訂單建立時間），毫秒級 Unix 時間戳  
endTime| false| string| 結束時間，毫秒級 Unix 時間戳  
status| false| string| 按狀態篩選：`Success`、`Processing`。不指定時返回所有終態狀態  
limit| false| integer| 每頁返回數量。預設：`20`，最大：`50`  
cursor| false| string| 分頁游標。使用上次響應中的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orders| array| 訂單列表  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> productId| string| 產品 ID  
> orderType| string| 訂單類型：`AddLiquidity`、`RemoveLiquidity`、`Reinvest`、`AddMargin`  
> baseCoin| string| 基礎幣種  
> quoteCoin| string| 計價幣種  
> quoteAmount| string| 計價幣種金額  
> baseAmount| string| 基礎幣種金額  
> status| string| 訂單狀態：`Success`（成功）、`Processing`（處理中）、`Fail`（失敗）  
> removeType| string| 提取模式（僅適用於 `RemoveLiquidity`）：`Normal`、`SingleQuoteCoin`、`SingleBaseCoin`  
> removeRate| integer| 提取百分比，整數（僅適用於 `RemoveLiquidity`）  
> leverage| string| 下單時的槓桿倍數（僅適用於 `AddLiquidity`）  
> slippageValue| string| 滑點扣除金額（僅適用於 `AddLiquidity`，`Success` 後填充）  
> createdTime| string| 訂單建立時間，毫秒級 Unix 時間戳  
nextPageCursor| string| 下一頁游標，為空表示無更多資料  
  
* * *

### 請求示例
    
    
    GET /v5/earn/liquidity-mining/order?orderLinkId=lm-001 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1741651200000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "orders": [  
                {  
                    "orderId": "5e651d09-6169-4f72-a609-8622ff421d19",  
                    "orderLinkId": "lm-001",  
                    "productId": "36",  
                    "orderType": "AddLiquidity",  
                    "baseCoin": "TON",  
                    "quoteCoin": "USDT",  
                    "quoteAmount": "200",  
                    "baseAmount": "0",  
                    "status": "Success",  
                    "removeType": "Normal",  
                    "removeRate": 0,  
                    "leverage": "2",  
                    "slippageValue": "0.02",  
                    "createdTime": "1775123507000"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1775123797220  
    }