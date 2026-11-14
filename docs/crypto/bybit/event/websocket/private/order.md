---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/event/websocket/private/order
api_type: WebSocket
updated_at: 2026-11-13 19:22:39.290182
---

# Order

Subscribe to the `order` or `order.event` topic to receive real-time Event Contract order updates.

**Topic:** `order` / `order.event`

info

  * Authentication is required before subscribing to private topics.
  * Pushed when an Event Contract order status changes (e.g., filled, partially filled, cancelled).



### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array| Object  
> category| string| Product type. `event`  
> orderId| string| Order ID  
> orderLinkId| string| User-defined order ID  
> symbol| string| Symbol name  
> symbolId| integer| Symbol ID  
> side| string| Side: `Buy` or `Sell`  
> baseCoin| string| Base coin  
> quoteCoin| string| Quote coin  
> settleCoin| string| Settle coin  
> orderStatus| string| Order status: `New`, `PartiallyFilled`, `Filled`, `Cancelled`, `Rejected`  
> ecContractType| string| Event contract type: `UpDown`, `Target`, `Range`  
> ecDirection| string| Direction: `UP`/`DOWN` (UpDown type), `ABOVE`/`BELOW` (Target type), `RANGE_IN`/`RANGE_OUT` (Range type)  
> ecDurationWindow| integer| Duration window in seconds  
> ecTargetPrice| string| Target price. Target type only.  
> ecLowerBound| string| Lower bound. Range type only.  
> ecUpperBound| string| Upper bound. Range type only.  
> ecOrderValue| string| Event Contract order value  
> ecIndexPrice| string| Index price at order creation  
> ecSettleTime| string| Expected settlement time in milliseconds  
> payoutRatio| string| Order payout ratio (price)  
> orderAvgPayoutRatio| string| Average payout ratio of filled portion  
> cumExecValue| string| Cumulative executed value  
> cumExecFee| string| Cumulative executed fee  
> leavesValue| string| Remaining order value  
> cumPayout| string| Cumulative payout  
> createType| integer| Order create type  
> cancelType| string| Cancel type  
> rejectReason| string| Reject reason  
> extraFees| array| Extra fees  
> transTime| string| Transaction time in milliseconds  
> createdTime| string| Order creation time in milliseconds  
> updatedTime| string| Order update time in milliseconds  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "order"  
        ]  
    }  
    

### Stream Example
    
    
    {  
        "topic": "order",  
        "id": "1509583_ETHUSDT-5MIN-UP_1311",  
        "creationTime": 1787635282379,  
        "data": [  
            {  
                "category": "event",  
                "orderId": "746a6c87-a6dd-4008-8889-37e694046681",  
                "orderLinkId": "cjm1119",  
                "symbol": "ETHUSDT-5MIN-UP",  
                "symbolId": 500000,  
                "side": "Sell",  
                "baseCoin": "ETH",  
                "quoteCoin": "USDT",  
                "settleCoin": "USDT",  
                "orderStatus": "PartiallyFilled",  
                "ecContractType": "UpDown",  
                "ecDirection": "UP",  
                "ecDurationWindow": 300,  
                "ecTargetPrice": "",  
                "ecLowerBound": "",  
                "ecUpperBound": "",  
                "ecOrderValue": "5000",  
                "ecIndexPrice": "2503.50730825",  
                "ecSettleTime": "1787635582374",  
                "payoutRatio": "3.5",  
                "orderAvgPayoutRatio": "3.5000035",  
                "cumExecValue": "200",  
                "cumExecFee": "8.57142858",  
                "leavesValue": "4800",  
                "cumPayout": "700",  
                "createType": 1,  
                "cancelType": "UNKNOWN",  
                "rejectReason": "EC_NoError",  
                "extraFees": [],  
                "transTime": "1787635282374",  
                "createdTime": "1787635103917",  
                "updatedTime": "1787635103917"  
            }  
        ]  
    }

---

# 訂單

訂閱 `order` 或 `order.event` 主題，實時接收 Event Contract 訂單狀態更新推送。

**Topic：** `order` / `order.event`

信息

  * 訂閱私有主題前需先完成身份驗證。
  * 當 Event Contract 訂單狀態發生變化時推送（如成交、部分成交、取消等）。



### 返回參數

參數| 類型| 說明  
---|---|---  
id| string| 消息 ID  
topic| string| Topic 名稱  
creationTime| number| 數據創建時間戳（毫秒）  
data| array| 對象  
> category| string| 產品類型。`event`  
> orderId| string| 訂單 ID  
> orderLinkId| string| 用戶自定義訂單 ID  
> symbol| string| 交易對名稱  
> symbolId| integer| 交易對 ID  
> side| string| 方向：`Buy` 或 `Sell`  
> baseCoin| string| 標的幣種  
> quoteCoin| string| 計價幣種  
> settleCoin| string| 結算幣種  
> orderStatus| string| 訂單狀態：`New`、`PartiallyFilled`、`Filled`、`Cancelled`、`Rejected`  
> ecContractType| string| 事件合約類型：`UpDown`、`Target`、`Range`  
> ecDirection| string| 方向：`UP`/`DOWN`（UpDown 類型），`ABOVE`/`BELOW`（Target 類型），`RANGE_IN`/`RANGE_OUT`（Range 類型）  
> ecDurationWindow| integer| 持續時間窗口（秒）  
> ecTargetPrice| string| 目標價格，僅 Target 類型適用  
> ecLowerBound| string| 下限價格，僅 Range 類型適用  
> ecUpperBound| string| 上限價格，僅 Range 類型適用  
> ecOrderValue| string| Event Contract 訂單金額  
> ecIndexPrice| string| 下單時的指數價格  
> ecSettleTime| string| 預計結算時間（毫秒）  
> payoutRatio| string| 訂單賠付比率（價格）  
> orderAvgPayoutRatio| string| 已成交部分的平均賠付比率  
> cumExecValue| string| 累計成交金額  
> cumExecFee| string| 累計已結算手續費  
> leavesValue| string| 剩餘未成交金額  
> cumPayout| string| 累計賠付金額  
> createType| integer| 訂單創建類型  
> cancelType| string| 取消類型  
> rejectReason| string| 拒絕原因  
> extraFees| array| 額外費用  
> transTime| string| 成交時間（毫秒）  
> createdTime| string| 訂單創建時間（毫秒）  
> updatedTime| string| 訂單更新時間（毫秒）  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "order"  
        ]  
    }  
    

### 推送示例
    
    
    {  
        "topic": "order",  
        "id": "1509583_ETHUSDT-5MIN-UP_1311",  
        "creationTime": 1787635282379,  
        "data": [  
            {  
                "category": "event",  
                "orderId": "746a6c87-a6dd-4008-8889-37e694046681",  
                "orderLinkId": "cjm1119",  
                "symbol": "ETHUSDT-5MIN-UP",  
                "symbolId": 500000,  
                "side": "Sell",  
                "baseCoin": "ETH",  
                "quoteCoin": "USDT",  
                "settleCoin": "USDT",  
                "orderStatus": "PartiallyFilled",  
                "ecContractType": "UpDown",  
                "ecDirection": "UP",  
                "ecDurationWindow": 300,  
                "ecTargetPrice": "",  
                "ecLowerBound": "",  
                "ecUpperBound": "",  
                "ecOrderValue": "5000",  
                "ecIndexPrice": "2503.50730825",  
                "ecSettleTime": "1787635582374",  
                "payoutRatio": "3.5",  
                "orderAvgPayoutRatio": "3.5000035",  
                "cumExecValue": "200",  
                "cumExecFee": "8.57142858",  
                "leavesValue": "4800",  
                "cumPayout": "700",  
                "createType": 1,  
                "cancelType": "UNKNOWN",  
                "rejectReason": "EC_NoError",  
                "extraFees": [],  
                "transTime": "1787635282374",  
                "createdTime": "1787635103917",  
                "updatedTime": "1787635103917"  
            }  
        ]  
    }