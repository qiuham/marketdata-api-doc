---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/websocket/private/order
api_type: WebSocket
updated_at: 2026-10-23 18:51:17.888159
---

# Order

Subscribe to the order stream to see changes to your orders in **real-time**.

**Topic:** `spread.order`  


### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array| Object  
> category| string| Category name, `combination`, `spot_leg`, `future_leg`  
> symbol| string| Combo or leg's symbol name  
> parentOrderId| string| Leg's parent order ID  
> orderId| string| Combo or leg's order ID  
> orderLinkId| string| Combo's user customised order ID  
> side| string| Combo or leg's order side, `Buy`, `Sell`  
> orderStatus| string| Combo or leg's order status  
> [cancelType](/docs/v5/enum#canceltype)| string| Cancel type  
> [rejectReason](/docs/v5/enum#rejectreason)| string| Reject reason  
> timeInForce| string| Time in force, `GTC`, `FOK`, `IOC`, `PostOnly`  
> price| string| Order price  
> qty| string| Order qty  
> avgPrice| string| Average filled price  
> leavesQty| string| The remaining qty not executed  
> leavesValue| string| The estimated value not executed  
> cumExecQty| string| Cumulative executed order qty  
> cumExecValue| string| Cumulative executed order value  
> cumExecFee| string| Deprecated. Cumulative executed trading fee  
> orderType| string| Order type. `Market`,`Limit`  
> isLeverage| string| Account-wide, if Spot Margin is enabled, the spot_leg field in the execution message shows 1, combo is "", and future_leg is 0.  
> createdTime| string| Order created timestamp (ms)  
> updatedTime| string| Order updated timestamp (ms)  
> feeCurrency| string| Deprecated. Trading fee currency for Spot leg only  
> createType| string| Order create type  
> closedPnl| string| Closed profit and loss for each close position order  
> cumFeeDetail| json| Cumulative trading fee details instead of `cumExecFee` and `feeCurrency`  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "spread.order"  
        ]  
    }  
    

### Stream Example
    
    
    {  
        "topic": "spread.order",  
        "id": "1448939_SOLUSDT_28732003549",  
        "creationTime": 1744170555912,  
        "data": [  
            {  
                "category": "combination",  
                "symbol": "SOLUSDT_SOL/USDT",  
                "parentOrderId": "",  
                "orderId": "aa858ea9-f3a0-40b6-ad57-888d47307345",  
                "orderLinkId": "",  
                "side": "Buy",  
                "orderStatus": "Filled",  
                "cancelType": "UNKNOWN",  
                "rejectReason": "EC_NoError",  
                "timeInForce": "GTC",  
                "price": "14",  
                "qty": "2",  
                "avgPrice": "",  
                "leavesQty": "0",  
                "leavesValue": "",  
                "cumExecQty": "2",  
                "cumExecValue": "",  
                "cumExecFee": "",  
                "orderType": "Limit",  
                "isLeverage": "",  
                "createdTime": "1744170534447",  
                "updatedTime": "1744170555905",  
                "feeCurrency": "",  
                "createType": "CreateByUser",  
                "closedPnl": "",  
                "cumFeeDetail": {  
                    "MNT": "0.00242968"  
                }  
            },  
            {  
                "category": "future_leg",  
                "symbol": "SOLUSDT",  
                "parentOrderId": "aa858ea9-f3a0-40b6-ad57-888d47307345",  
                "orderId": "2948d2dc-f8f1-4485-a83d-0bad3dae2c31",  
                "orderLinkId": "",  
                "side": "Buy",  
                "orderStatus": "Filled",  
                "cancelType": "UNKNOWN",  
                "rejectReason": "EC_NoError",  
                "timeInForce": "GTC",  
                "price": "118.2",  
                "qty": "2",  
                "avgPrice": "118.2",  
                "leavesQty": "0",  
                "leavesValue": "0",  
                "cumExecQty": "2",  
                "cumExecValue": "236.4",  
                "cumExecFee": "0.01182",  
                "orderType": "Limit",  
                "isLeverage": "",  
                "createdTime": "1744170534447",  
                "updatedTime": "1744170555910",  
                "feeCurrency": "",  
                "createType": "CreateByFutureSpread",  
                "closedPnl": "0",  
                "cumFeeDetail": {  
                    "MNT": "0.00242968"  
                }  
            }  
        ]  
    }

---

# 訂單

訂閱價差交易訂單推送

**Topic:** `spread.order`  


### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息ID  
topic| string| Topic名  
creationTime| number| 消息數據創建時間 (ms)  
data| array<object>|   
> category| string| 組合或單腿類型, `combination`: 組合, `spot_leg`: 現貨單腿, `future_leg`: 合約單腿  
> symbol| string| 組合或單腿的合約名稱  
> parentOrderId| string| 單腿訂單的所屬組合訂單ID  
> orderId| string| 組合或單腿的訂單ID  
> orderLinkId| string| 組合單的用戶自定義ID  
> side| string| 組合或單腿的訂單方向, `Buy`, `Sell`  
> orderStatus| string| 組合或單腿的訂單狀態  
> [cancelType](/docs/zh-TW/v5/enum#canceltype)| string| 訂單被取消類型  
> [rejectReason](/docs/zh-TW/v5/enum#rejectreason)| string| 拒絕原因  
> timeInForce| string| 執行策略, `GTC`, `FOK`, `IOC`, `PostOnly`  
> price| string| 訂單價格  
> qty| string| 訂單數量  
> avgPrice| string| 平均成交價格  
> leavesQty| string| 訂單剩餘未成交的數量  
> leavesValue| string| 訂單剩餘未成交的價值  
> cumExecQty| string| 訂單累計成交數量  
> cumExecValue| string| 訂單累計成交價值  
> cumExecFee| string| 已棄用. 訂單累計成交的手續費  
> orderType| string| 訂單類型. `Market`,`Limit`  
> isLeverage| string| 帳戶維度, 如果現貨槓桿打開了, 那麼對於category=spot_leg, 該字段暫時為1, 組合總是"", category=future_leg總是"0"  
> createdTime| string| 創建訂單的時間戳 (毫秒)  
> updatedTime| string| 訂單更新的時間戳 (毫秒)  
> feeCurrency| string| 已棄用. 手續費幣種, 僅適用於現貨單腿訂單  
> [createType](/docs/zh-TW/v5/enum#createtype)| string| 訂單創建類型  
> closedPnl| string| 平倉單盈虧, 部分平倉時, 減去了平攤的開倉手續費和期間產生的資金費以及平倉手續費  
> cumFeeDetail| json| 累積交易費詳情, 替代`cumExecFee`和`feeCurrency`  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "spread.order"  
        ]  
    }  
    

### 推送示例
    
    
    {  
        "topic": "spread.order",  
        "id": "1448939_SOLUSDT_28732003549",  
        "creationTime": 1744170555912,  
        "data": [  
            {  
                "category": "combination",  
                "symbol": "SOLUSDT_SOL/USDT",  
                "parentOrderId": "",  
                "orderId": "aa858ea9-f3a0-40b6-ad57-888d47307345",  
                "orderLinkId": "",  
                "side": "Buy",  
                "orderStatus": "Filled",  
                "cancelType": "UNKNOWN",  
                "rejectReason": "EC_NoError",  
                "timeInForce": "GTC",  
                "price": "14",  
                "qty": "2",  
                "avgPrice": "",  
                "leavesQty": "0",  
                "leavesValue": "",  
                "cumExecQty": "2",  
                "cumExecValue": "",  
                "cumExecFee": "",  
                "orderType": "Limit",  
                "isLeverage": "",  
                "createdTime": "1744170534447",  
                "updatedTime": "1744170555905",  
                "feeCurrency": "",  
                "createType": "CreateByUser",  
                "closedPnl": "",  
                "cumFeeDetail": {  
                    "MNT": "0.00242968"  
                }  
            },  
            {  
                "category": "future_leg",  
                "symbol": "SOLUSDT",  
                "parentOrderId": "aa858ea9-f3a0-40b6-ad57-888d47307345",  
                "orderId": "2948d2dc-f8f1-4485-a83d-0bad3dae2c31",  
                "orderLinkId": "",  
                "side": "Buy",  
                "orderStatus": "Filled",  
                "cancelType": "UNKNOWN",  
                "rejectReason": "EC_NoError",  
                "timeInForce": "GTC",  
                "price": "118.2",  
                "qty": "2",  
                "avgPrice": "118.2",  
                "leavesQty": "0",  
                "leavesValue": "0",  
                "cumExecQty": "2",  
                "cumExecValue": "236.4",  
                "cumExecFee": "0.01182",  
                "orderType": "Limit",  
                "isLeverage": "",  
                "createdTime": "1744170534447",  
                "updatedTime": "1744170555910",  
                "feeCurrency": "",  
                "createType": "CreateByFutureSpread",  
                "closedPnl": "0",  
                "cumFeeDetail": {  
                    "MNT": "0.00242968"  
                }  
            }  
        ]  
    }