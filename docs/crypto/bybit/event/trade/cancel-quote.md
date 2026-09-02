---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/trade/cancel-quote
api_type: Trading
updated_at: 2026-09-02 18:41:56.715663
---

# Get Event Contract Active Orders

Query real-time unfilled or partially filled Event Contract orders.

info

  * Only **Event Contract maker accounts** are allowed to access this endpoint.



### HTTP Request

GET`/v5/event/order-realtime`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| false| string| Symbol name, e.g. `ETHUSDT-28AUG26-2450-2570-OUT`  
orderId| false| string| Order ID. If both `orderId` and `orderLinkId` are passed, `orderId` takes priority  
orderLinkId| false| string| User-defined order ID  
limit| false| integer| Number of items per page. Default: `20`, Range: [`1`, `50`]  
cursor| false| string| Pagination cursor. Use `nextPageCursor` from the response to retrieve the next page  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Event Contract active order list  
> orderId| string| Order ID  
> orderLinkId| string| User-defined order ID  
> symbol| string| Symbol name  
> symbolId| string| Symbol ID  
> side| string| Order side: `Buy` or `Sell`  
> orderStatus| string| Order status: `New` (order created), `PartiallyFilled` (partially filled), `Untriggered` (awaiting trigger)  
> payoutRatio| string| Order payout ratio (price)  
> cumExecValue| string| Cumulative executed value  
> cumExecFee| string| Cumulative executed fee  
> leavesValue| string| Remaining order value  
> ecContractType| string| Event contract type: `UpDown`, `Target`, `Range`  
> ecDirection| string| Direction: `UP`/`DOWN` (UpDown type), `ABOVE`/`BELOW` (Target type), `RANGE_IN`/`RANGE_OUT` (Range type)  
> ecOrderValue| string| Event Contract order value  
> ecSettleTime| string| Expected settlement time in milliseconds  
> ecTargetPrice| string| Target price. Target type only.  
> ecLowerBound| string| Lower bound. Range type only.  
> ecUpperBound| string| Upper bound. Range type only.  
> ecDurationWindow| string| Duration window in seconds  
> ecIndexPrice| string| Index price at order creation  
> orderAvgPayoutRatio| string| Average payout ratio of filled portion  
> createType| string| Order create type, e.g. `CreateByUser`  
> createdTime| string| Order creation timestamp in milliseconds  
> updatedTime| string| Order update timestamp in milliseconds  
nextPageCursor| string| Cursor for next page pagination  
  
* * *

### Request Example
    
    
    GET /v5/event/order-realtime?symbol=ETHUSDT-28AUG26-2450-2570-OUT&limit=20 HTTP/1.1  
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
                    "orderLinkId": "my-order-001",  
                    "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
                    "symbolId": "100001",  
                    "side": "Buy",  
                    "orderStatus": "New",  
                    "payoutRatio": "1.95",  
                    "cumExecValue": "0",  
                    "cumExecFee": "0",  
                    "leavesValue": "50",  
                    "ecContractType": "UpDown",  
                    "ecDirection": "UP",  
                    "ecOrderValue": "50",  
                    "ecSettleTime": "1694515498753",  
                    "ecTargetPrice": "",  
                    "ecLowerBound": "",  
                    "ecUpperBound": "",  
                    "ecDurationWindow": "300",  
                    "ecIndexPrice": "26000.5",  
                    "orderAvgPayoutRatio": "0",  
                    "createType": "CreateByUser",  
                    "createdTime": "1694402559843",  
                    "updatedTime": "1694402559843"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1694402560000  
    }

---

# 查詢Event Contract活躍訂單

查詢實時未成交或部分成交的 Event Contract 訂單。

信息

  * 僅 **Event Contract maker 帳戶** 可訪問此接口。



### HTTP 請求

GET`/v5/event/order-realtime`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| 否| string| 交易對名稱，如 `ETHUSDT-28AUG26-2450-2570-OUT`  
orderId| 否| string| 訂單 ID。若同時傳入 `orderId` 和 `orderLinkId`，以 `orderId` 為準  
orderLinkId| 否| string| 用戶自定義訂單 ID  
limit| 否| integer| 每頁數量。默認：`20`，範圍：[`1`, `50`]  
cursor| 否| string| 分頁游標，使用返回結果中的 `nextPageCursor` 獲取下一頁  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| Event Contract 活躍訂單列表  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> symbol| string| 交易對名稱  
> symbolId| string| 交易對 ID  
> side| string| 訂單方向：`Buy` 或 `Sell`  
> orderStatus| string| 訂單狀態：`New`（已創建）、`PartiallyFilled`（部分成交）、`Untriggered`（等待觸發）  
> payoutRatio| string| 訂單賠付比率（價格）  
> cumExecValue| string| 累計成交金額  
> cumExecFee| string| 累計已結算手續費  
> leavesValue| string| 剩餘未成交金額  
> ecContractType| string| 事件合約類型：`UpDown`、`Target`、`Range`  
> ecDirection| string| 方向：`UP`/`DOWN`（UpDown 類型），`ABOVE`/`BELOW`（Target 類型），`RANGE_IN`/`RANGE_OUT`（Range 類型）  
> ecOrderValue| string| Event Contract 訂單金額  
> ecSettleTime| string| 預計結算時間（毫秒）  
> ecTargetPrice| string| 目標價格，僅 Target 類型適用  
> ecLowerBound| string| 下限價格，僅 Range 類型適用  
> ecUpperBound| string| 上限價格，僅 Range 類型適用  
> ecDurationWindow| string| 持續時間窗口（秒）  
> ecIndexPrice| string| 下單時的指數價格  
> orderAvgPayoutRatio| string| 已成交部分的平均賠付比率  
> createType| string| 訂單創建類型，如 `CreateByUser`  
> createdTime| string| 訂單創建時間（毫秒）  
> updatedTime| string| 訂單更新時間（毫秒）  
nextPageCursor| string| 下一頁分頁游標  
  
* * *

### 請求示例
    
    
    GET /v5/event/order-realtime?symbol=ETHUSDT-28AUG26-2450-2570-OUT&limit=20 HTTP/1.1  
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
                    "orderLinkId": "my-order-001",  
                    "symbol": "ETHUSDT-28AUG26-2450-2570-OUT",  
                    "symbolId": "100001",  
                    "side": "Buy",  
                    "orderStatus": "New",  
                    "payoutRatio": "1.95",  
                    "cumExecValue": "0",  
                    "cumExecFee": "0",  
                    "leavesValue": "50",  
                    "ecContractType": "UpDown",  
                    "ecDirection": "UP",  
                    "ecOrderValue": "50",  
                    "ecSettleTime": "1694515498753",  
                    "ecTargetPrice": "",  
                    "ecLowerBound": "",  
                    "ecUpperBound": "",  
                    "ecDurationWindow": "300",  
                    "ecIndexPrice": "26000.5",  
                    "orderAvgPayoutRatio": "0",  
                    "createType": "CreateByUser",  
                    "createdTime": "1694402559843",  
                    "updatedTime": "1694402559843"  
                }  
            ],  
            "nextPageCursor": ""  
        },  
        "retExtInfo": {},  
        "time": 1694402560000  
    }