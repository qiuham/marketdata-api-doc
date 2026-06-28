---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/finance/advanced-earn/dual-asset/order
api_type: REST
updated_at: 2026-05-27 19:16:48.731057
---

# Get Order Info

info

  * Need authentication. **Up to 10 requests** per second.
  * Query your Dual Assets order history. Requires Earn permission on the API key.



### HTTP Request

GET `/v5/earn/advance/order`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#advanced-earn-category)| **true**|  string| Product type, e.g. `DualAssets`  
productId| false| string| Product ID  
orderId| false| string| OrderId  
orderLinkId| false| string| User customised order ID  
startTime| false| string| Start time (order creation time), unix timestamp in milliseconds  
endTime| false| string| End time, unix timestamp in milliseconds  
limit| false| int| Number of items per page. Default: 20, Max: 20  
cursor| false| string| Pagination cursor. Use nextPageCursor from previous response  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#advanced-earn-category)| string| `DualAssets`  
nextPageCursor| string| Next page cursor, empty means no more data  
list| array| Order list  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
> productId| string| Product ID  
> [category](/docs/v5/enum#advanced-earn-category)| string| Product category,'DualAssets'  
> orderType| string| `Stake`: Subscribe  
> amount| string| Order amount  
> coin| string| Coin name  
> baseCoin| string| Base coin  
> quoteCoin| string| Quote coin  
> [status](/docs/v5/enum#advanced-earn-order-status)| string| `Pending`: Order confirming, `Success`: Order successful, position created, `Settled`: Position settled, `Fail`: Order failed  
> createdTime| string| Created time, unix timestamp in ms  
> updatedTime| string| Updated time, unix timestamp in ms  
> direction| string| `BuyLow`, `SellHigh`  
> targetPrice| string| Target price in USDT  
> settlementTime| int64| Settlement time, unix timestamp in ms  
> estimateApyE8| int64| Estimated annualized yield, e8 precision  
> duration| string| Product term, e.g. 8h, 1d, 2d, 3d  
> accountType| string| Account type  
> toAccountType| string| Settlement destination account  
> selectApyE8| int64| APY selected by user at order time, e8 precision  
> isVip| bool| Whether it is a VIP product  
> settlementCoin| string| Settlement coin, Only available when status=Settled  
> settlementAmount| string| Settlement amount, Only available when status=Settled  
> orderMode| string| Order mode: `Normal`, `RFQ`  
> settlementPrice| string| Settlement price in USDT, Only available when status=Settled  
> refundStatus| string| Refund status. Only valid when status=`Fail`, `Processing`, `Processed`  
> trialBonusAmount| string| Trial bonus amount  
> trialBonusPnl| string| Trial bonus P&L  
  
* * *

### Request Example

  * HTTP


    
    
    GET /v5/earn/advance/order?category=DualAssets&limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672280218882  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DualAssets",  
            "list": [  
                {  
                    "orderId": "ef9644c2-0c98-40e5-ae33-8aa5b6d85058",  
                    "orderLinkId": "54b3589b-da55-4b17-acdd-aa75912c9eb9",  
                    "productId": "36320",  
                    "category": "DualAssets",  
                    "orderType": "Stake",  
                    "amount": "20",  
                    "coin": "USDT",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "status": "Success",  
                    "createdTime": "1773815357000",  
                    "updatedTime": "1773815357000",  
                    "direction": "BuyLow",  
                    "targetPrice": "2325",  
                    "settlementTime": "0",  
                    "estimateApyE8": "771808500",  
                    "duration": "3d",  
                    "accountType": "UNIFIED",  
                    "toAccountType": "",  
                    "selectApyE8": "857565000",  
                    "isVip": false,  
                    "settlementCoin": "ETH",  
                    "settlementAmount": "0",  
                    "orderMode": "Normal",  
                    "settlementPrice": "",  
                    "refundStatus": "",  
                    "trialBonusAmount": "",  
                    "trialBonusPnl": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1773815392318  
    }

---

# 查詢訂單資訊

信息

  * 需要身份驗證。每秒**最多 10 次請求** 。
  * 查詢您的雙幣投資訂單歷史紀錄。API 金鑰需要具備 Earn (理財) 權限。



### HTTP 請求

GET `/v5/earn/advance/order`

### 請求參數

參數| 必填| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#advanced-earn-category)| **true**|  string| 產品類型，例如 `DualAssets`  
productId| false| string| 產品 ID  
orderId| false| string| 訂單 ID  
orderLinkId| false| string| 用戶自定義訂單 ID  
startTime| false| string| 開始時間（訂單創建時間），毫秒級 Unix 時間戳  
endTime| false| string| 結束時間，毫秒級 Unix 時間戳  
limit| false| int| 每頁數量。預設值：20，最大值：20  
cursor| false| string| 分頁游標。請使用上一次請求返回的 `nextPageCursor`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#advanced-earn-category)| string| `DualAssets`  
nextPageCursor| string| 下一頁的游標，為空字串代表沒有更多資料  
list| array| 訂單列表  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> productId| string| 產品 ID  
> [category](/docs/zh-TW/v5/enum#advanced-earn-category)| string| 產品類別，`DualAssets`  
> orderType| string| `Stake`: 申購  
> amount| string| 訂單數量  
> coin| string| 幣種名稱  
> baseCoin| string| 基礎幣種 (Base Coin)  
> quoteCoin| string| 計價幣種 (Quote Coin)  
> [status](/docs/zh-TW/v5/enum#advanced-earn-order-status)| string| `Pending`: 訂單確認中, `Success`: 訂單成功（已創建倉位）, `Settled`: 倉位已結算, `Fail`: 訂單失敗  
> createdTime| string| 創建時間，毫秒級 Unix 時間戳  
> updatedTime| string| 更新時間，毫秒級 Unix 時間戳  
> direction| string| 方向：`BuyLow` (低買), `SellHigh` (高賣)  
> targetPrice| string| 目標價格（掛鉤價），單位為 USDT  
> settlementTime| int64| 結算時間，毫秒級 Unix 時間戳  
> estimateApyE8| int64| 預估年化收益率（e8 精度）  
> duration| string| 產品期限，例如 8h, 1d, 2d, 3d  
> accountType| string| 帳戶類型  
> toAccountType| string| 結算目標帳戶  
> selectApyE8| int64| 用戶下單時選擇的年化收益率（e8 精度）  
> isVip| bool| 是否為 VIP 產品  
> settlementCoin| string| 結算幣種，僅在 status=`Settled` (已結算) 時有效  
> settlementAmount| string| 結算數量，僅在 status=`Settled` (已結算) 時有效  
> orderMode| string| 訂單模式：`Normal` (普通), `RFQ` (報價請求)  
> settlementPrice| string| 結算價格，單位為 USDT，僅在 status=`Settled` (已結算) 時有效  
> refundStatus| string| 退款狀態。僅在 status=`Fail` 時有效，包含 `Processing` (處理中), `Processed` (已處理)  
> trialBonusAmount| string| 體驗金數量  
> trialBonusPnl| string| 體驗金盈虧 (P&L)  
  
* * *

### 請求示例

  * HTTP


    
    
    GET /v5/earn/advance/order?category=DualAssets&limit=2 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672280218882  
    X-BAPI-RECV-WINDOW: 5000  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "category": "DualAssets",  
            "list": [  
                {  
                    "orderId": "ef9644c2-0c98-40e5-ae33-8aa5b6d85058",  
                    "orderLinkId": "54b3589b-da55-4b17-acdd-aa75912c9eb9",  
                    "productId": "36320",  
                    "category": "DualAssets",  
                    "orderType": "Stake",  
                    "amount": "20",  
                    "coin": "USDT",  
                    "baseCoin": "ETH",  
                    "quoteCoin": "USDT",  
                    "status": "Success",  
                    "createdTime": "1773815357000",  
                    "updatedTime": "1773815357000",  
                    "direction": "BuyLow",  
                    "targetPrice": "2325",  
                    "settlementTime": "0",  
                    "estimateApyE8": "771808500",  
                    "duration": "3d",  
                    "accountType": "UNIFIED",  
                    "toAccountType": "",  
                    "selectApyE8": "857565000",  
                    "isVip": false,  
                    "settlementCoin": "ETH",  
                    "settlementAmount": "0",  
                    "orderMode": "Normal",  
                    "settlementPrice": "",  
                    "refundStatus": "",  
                    "trialBonusAmount": "",  
                    "trialBonusPnl": ""  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1773815392318  
    }