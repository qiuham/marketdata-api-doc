---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/trade/order-list
api_type: Trading
updated_at: 2026-11-13 19:22:36.033422
---

# Get Event Contract Order History

Query Event Contract historical orders. Returns orders in the past 2 years.

info

  * Only **Event Contract maker accounts** are allowed to access this endpoint.
  * Results are sorted by `createdTime` in descending order.
  * Default query window: **7 days** if `startTime`/`endTime` are not specified.



### HTTP Request

GET`/v5/event/order-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| false| string| Symbol name, e.g. `ETHUSDT-28AUG26-2450-2570-OUT`  
orderId| false| string| Order ID  
orderLinkId| false| string| User-defined order ID  
startTime| false| integer| Start time in milliseconds. Default: 7 days ago  
endTime| false| integer| End time in milliseconds. Default: now  
limit| false| integer| Number of items per page. Default: `50`, Range: [`1`, `100`]  
cursor| false| string| Pagination cursor  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Event Contract order history list  
> orderId| string| Order ID  
> orderLinkId| string| User-defined order ID  
> orderStatus| string| Order status: `Filled`, `Cancelled`, `Rejected`, `PartiallyFilledCanceled`  
> symbol| string| Symbol name  
> symbolId| string| Symbol ID  
> baseCoin| string| Base coin  
> quoteCoin| string| Quote coin  
> settleCoin| string| Settle coin  
> ecDirection| string| Direction: `UP`/`DOWN` (UpDown type), `ABOVE`/`BELOW` (Target type), `RANGE_IN`/`RANGE_OUT` (Range type)  
> ecDurationWindow| string| Duration window in seconds  
> ecTargetPrice| string| Target price. Target type only.  
> ecContractType| string| Event contract type: `UpDown`, `Target`, `Range`  
> ecLowerBound| string| Lower bound. Range type only.  
> ecUpperBound| string| Upper bound. Range type only.  
> settleTimeMs| string| Settlement time in milliseconds  
> ecOrderValue| string| Event Contract order value  
> ecIndexPrice| string| Index price at order creation  
> orderAvgPayoutRatio| string| Average payout ratio of filled portion  
> cumExecValue| string| Cumulative executed value  
> payoutRatio| string| Order payout ratio (price)  
> tradeFee| string| Trade fee  
> transTime| string| Transaction time in milliseconds  
> createTime| string| Order creation time in milliseconds  
> updateTime| string| Order update time in milliseconds  
> cumPayout| string| Cumulative payout  
> cumExecFee| string| Cumulative executed fee  
> cancelType| string| Cancel type. Empty if not cancelled.  
> createType| string| Order create type, e.g. `CreateByUser`  
> rejectReason| string| Reject reason. Empty if not rejected.  
> extraFees| string| Extra fees (JSON string if applicable)  
cursor| string| Cursor for next page pagination  
  
* * *

### Request Example
    
    
    GET /v5/event/order-list?symbol=ETHUSDT-28AUG26-2450-2570-OUT&limit=50 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1694402559000  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "1234567890",  
                    "orderLinkId": "",  
                    "orderStatus": "Filled",  
                    "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
                    "symbolId": "100001",  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "settleCoin": "USDT",  
                    "ecDirection": "UP",  
                    "ecDurationWindow": "300",  
                    "ecTargetPrice": "",  
                    "ecContractType": "UpDown",  
                    "ecLowerBound": "",  
                    "ecUpperBound": "",  
                    "settleTimeMs": "1694515498753",  
                    "ecOrderValue": "50",  
                    "ecIndexPrice": "26000.5",  
                    "orderAvgPayoutRatio": "1.85",  
                    "cumExecValue": "50",  
                    "payoutRatio": "1.95",  
                    "tradeFee": "0.5",  
                    "transTime": "1694402559843",  
                    "createTime": "1694402559843",  
                    "updateTime": "1694515498753",  
                    "cumPayout": "92.5",  
                    "cumExecFee": "0.5",  
                    "cancelType": "",  
                    "createType": "CreateByUser",  
                    "rejectReason": "",  
                    "extraFees": ""  
                }  
            ],  
            "cursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1694402560000  
    }

---

# 查詢Event Contract歷史訂單

查詢事件合約歷史訂單，支持查詢過去 2 年內的訂單記錄。

信息

  * 僅 **Event Contract maker 帳戶** 可訪問此接口。
  * 結果按 `createdTime` 降序排列。
  * 若未指定 `startTime`/`endTime`，默認查詢窗口為 **7 天** 。



### HTTP 請求

GET`/v5/event/order-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| 否| string| 交易對名稱，如 `ETHUSDT-28AUG26-2450-2570-OUT`  
orderId| 否| string| 訂單 ID  
orderLinkId| 否| string| 用戶自定義訂單 ID  
startTime| 否| integer| 開始時間（毫秒）。默認：7 天前  
endTime| 否| integer| 結束時間（毫秒）。默認：當前時間  
limit| 否| integer| 每頁數量。默認：`50`，範圍：[`1`, `100`]  
cursor| 否| string| 分頁游標  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| Event Contract 歷史訂單列表  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> orderStatus| string| 訂單狀態：`Filled`（已成交）、`Cancelled`（已取消）、`Rejected`（已拒絕）、`PartiallyFilledCanceled`（部分成交後取消）  
> symbol| string| 交易對名稱  
> symbolId| string| 交易對 ID  
> baseCoin| string| 標的幣種  
> quoteCoin| string| 計價幣種  
> settleCoin| string| 結算幣種  
> ecDirection| string| 方向：`UP`/`DOWN`（UpDown 類型），`ABOVE`/`BELOW`（Target 類型），`RANGE_IN`/`RANGE_OUT`（Range 類型）  
> ecDurationWindow| string| 持續時間窗口（秒）  
> ecTargetPrice| string| 目標價格，僅 Target 類型適用  
> ecContractType| string| 事件合約類型：`UpDown`、`Target`、`Range`  
> ecLowerBound| string| 下限價格，僅 Range 類型適用  
> ecUpperBound| string| 上限價格，僅 Range 類型適用  
> settleTimeMs| string| 結算時間（毫秒）  
> ecOrderValue| string| Event Contract 訂單金額  
> ecIndexPrice| string| 下單時的指數價格  
> orderAvgPayoutRatio| string| 已成交部分的平均賠付比率  
> cumExecValue| string| 累計成交金額  
> payoutRatio| string| 訂單賠付比率（價格）  
> tradeFee| string| 交易手續費  
> transTime| string| 成交時間（毫秒）  
> createTime| string| 訂單創建時間（毫秒）  
> updateTime| string| 訂單更新時間（毫秒）  
> cumPayout| string| 累計賠付金額  
> cumExecFee| string| 累計已結算手續費  
> cancelType| string| 取消類型，未取消時為空  
> createType| string| 訂單創建類型，如 `CreateByUser`  
> rejectReason| string| 拒絕原因，未拒絕時為空  
> extraFees| string| 額外費用（適用時為 JSON 字符串）  
cursor| string| 下一頁分頁游標  
  
* * *

### 請求示例
    
    
    GET /v5/event/order-list?symbol=ETHUSDT-28AUG26-2450-2570-OUT&limit=50 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1694402559000  
    X-BAPI-RECV-WINDOW: 5000  
    

### 返回示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "1234567890",  
                    "orderLinkId": "",  
                    "orderStatus": "Filled",  
                    "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
                    "symbolId": "100001",  
                    "baseCoin": "BTC",  
                    "quoteCoin": "USDT",  
                    "settleCoin": "USDT",  
                    "ecDirection": "UP",  
                    "ecDurationWindow": "300",  
                    "ecTargetPrice": "",  
                    "ecContractType": "UpDown",  
                    "ecLowerBound": "",  
                    "ecUpperBound": "",  
                    "settleTimeMs": "1694515498753",  
                    "ecOrderValue": "50",  
                    "ecIndexPrice": "26000.5",  
                    "orderAvgPayoutRatio": "1.85",  
                    "cumExecValue": "50",  
                    "payoutRatio": "1.95",  
                    "tradeFee": "50",  
                    "transTime": "1694402559843",  
                    "createTime": "1694402559843",  
                    "updateTime": "1694515498753",  
                    "cumPayout": "92.5",  
                    "cumExecFee": "0.5",  
                    "cancelType": "",  
                    "createType": "CreateByUser",  
                    "rejectReason": "",  
                    "extraFees": ""  
                }  
            ],  
            "cursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1694402560000  
    }