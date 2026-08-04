---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/websocket/private/dcp
api_type: WebSocket
updated_at: 2026-08-04 19:08:09.544309
---

# Order

Subscribe to the order stream to see changes to your orders in **real-time**.

**All-In-One Topic:** `order`  
**Categorised Topic:** `order.spot`, `order.linear`, `order.inverse`, `order.option`

info

  * All-In-One topic and Categorised topic **cannot** be in the same subscription request
  * All-In-One topic: Allow you to listen to all categories (spot, linear, inverse, option) websocket updates
  * Categorised Topic: Allow you to listen only to specific category websocket updates



tip

You may receive two orderStatus=`Filled` messages when the cancel request is accepted but the order is executed at the same time. Generally, one message contains "orderStatus=Filled, rejectReason=EC_NoError", and another message contains "orderStatus=Filled, cancelType=CancelByUser, rejectReason=EC_OrigClOrdIDDoesNotExist". The first message tells you the order is executed, and the second message tells you the followed cancel request is rejected due to order is executed.

### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Message ID  
topic| string| Topic name  
creationTime| number| Data created timestamp (ms)  
data| array| Object  
> category| string| Product type `spot`, `linear`, `inverse`, `option`  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
> parentOrderLinkId| string| Indicates the linked parent order for attached take-profit and stop-loss orders. Supported for futures and options.

  * [Amending](/docs/v5/order/amend-order) take-profit or stop-loss orders does not change the parentOrderLinkId
  * **Futures** : using [set trading stop](/docs/v5/position/trading-stop) to update attached TP/SL from the original order does not change the parentOrderLinkId.
  * **Options** : using [set trading stop](/docs/v5/position/trading-stop) to update attached TP/SL from the original order will change the parentOrderLinkId.
  * **Futures & Options**: if TP/SL is set via [set trading stop](/docs/v5/position/trading-stop)for a position that originally has no attached TP/SL, the parentOrderLinkId is meaningless.

  
> isLeverage| string| Whether to borrow. `0`: false, `1`: true  
> blockTradeId| string| Block trade ID  
> symbol| string| Symbol name  
> price| string| Order price  
> brokerOrderPrice| string| Dedicated field for EU liquidity provider  
> qty| string| Order qty  
> side| string| Side. `Buy`,`Sell`  
> [positionIdx](/docs/v5/enum#positionidx)| integer| Position index. Used to identify positions in different position modes  
> [orderStatus](/docs/v5/enum#orderstatus)| string| Order status  
> [createType](/docs/v5/enum#createtype)| string| Order create type, Spot, Option do not have this key  
> [cancelType](/docs/v5/enum#canceltype)| string| Cancel type  
> [rejectReason](/docs/v5/enum#rejectreason)| string| Reject reason  
> avgPrice| string| Average filled price, returns `""` for those orders without avg price  
> leavesQty| string| The remaining qty not executed  
> leavesValue| string| The remaining value not executed  
> cumExecQty| string| Cumulative executed order qty  
> cumExecValue| string| Cumulative executed order value  
> cumExecFee| string| 

  * `inverse`, `option`: Cumulative executed trading fee.
  * `linear`, `spot`: Deprecated. Use `cumFeeDetail` instead.
  * After upgraded to the Unified account, you can use `execFee` for each fill in [Execution](/docs/v5/websocket/private/execution) topic

  
> closedPnl| string| Closed profit and loss for each close position order. The figure is the same as "closedPnl" from [Get Closed PnL](/docs/v5/position/close-pnl)  
> feeCurrency| string| Deprecated. Trading fee currency for Spot only. Please understand Spot trading fee currency [here](/docs/v5/enum#spot-fee-currency-instruction)  
> [timeInForce](/docs/v5/enum#timeinforce)| string| Time in force  
> [orderType](/docs/v5/enum#ordertype)| string| Order type. `Market`,`Limit`. For TP/SL orders, is the order type after the order was triggered  
> [stopOrderType](/docs/v5/enum#stopordertype)| string| Stop order type  
> ocoTriggerBy| string| The trigger type of Spot OCO order.`OcoTriggerByUnknown`, `OcoTriggerByTp`, `OcoTriggerBySl`  
> orderIv| string| Implied volatility  
> marketUnit| string| The unit for `qty` when create **Spot market** orders. `baseCoin`, `quoteCoin`  
> slippageToleranceType| string| Spot and Futures market order slippage tolerance type `TickSize`, `Percent`, `UNKNOWN`(default)  
> slippageTolerance| string| Slippage tolerance value  
> triggerPrice| string| Trigger price. If `stopOrderType`=_TrailingStop_ , it is activate price. Otherwise, it is trigger price  
> takeProfit| string| Take profit price  
> stopLoss| string| Stop loss price  
> tpslMode| string| TP/SL mode, `Full`: entire position for TP/SL. `Partial`: partial position tp/sl. Spot does not have this field, and Option returns always ""  
> tpLimitPrice| string| The limit order price when take profit price is triggered  
> slLimitPrice| string| The limit order price when stop loss price is triggered  
> [tpTriggerBy](/docs/v5/enum#triggerby)| string| The price type to trigger take profit  
> [slTriggerBy](/docs/v5/enum#triggerby)| string| The price type to trigger stop loss  
> triggerDirection| integer| Trigger direction. `1`: rise, `2`: fall  
> [triggerBy](/docs/v5/enum#triggerby)| string| The price type of trigger price  
> lastPriceOnCreated| string| Last price when place the order  
> reduceOnly| boolean| Reduce only. `true` means reduce position size  
> closeOnTrigger| boolean| Close on trigger. [What is a close on trigger order?](https://www.bybit.com/en/help-center/article/Close-On-Trigger-Order)  
> placeType| string| Place type, `option` used. `iv`, `price`  
> [smpType](/docs/v5/enum#smptype)| string| SMP execution type  
> smpGroup| integer| Smp group ID. If the UID has no group, it is `0` by default  
> smpOrderId| string| The counterparty's orderID which triggers this SMP execution  
> createdTime| string| Order created timestamp (ms)  
> updatedTime| string| Order updated timestamp (ms)  
> cumFeeDetail| json| 

  * `linear`, `spot`: Cumulative trading fee details instead of `cumExecFee`

  
> rpiTakerAccess| boolean| Whether the order has matched with an RPI order as the counterparty. `true`: the counterparty is an RPI order, `false`: the counterparty is not an RPI order.  
> rpiMatchedQty| string| Cumulative quantity matched against RPI orders as the counterparty.  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "order"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="private",  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    def handle_message(message):  
        print(message)  
    ws.order_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### Stream Example
    
    
    {  
        "id": "5923240c6880ab-c59f-420b-9adb-3639adc9dd90",  
        "topic": "order",  
        "creationTime": 1672364262474,  
        "data": [  
            {  
                "symbol": "ETH-30DEC22-1400-C",  
                "orderId": "5cf98598-39a7-459e-97bf-76ca765ee020",  
                "side": "Sell",  
                "orderType": "Market",  
                "cancelType": "UNKNOWN",  
                "price": "72.5",  
                "qty": "1",  
                "orderIv": "",  
                "timeInForce": "IOC",  
                "orderStatus": "Filled",  
                "orderLinkId": "",  
                "lastPriceOnCreated": "",  
                "reduceOnly": false,  
                "leavesQty": "",  
                "leavesValue": "",  
                "cumExecQty": "1",  
                "cumExecValue": "75",  
                "avgPrice": "75",  
                "blockTradeId": "",  
                "positionIdx": 0,  
                "cumExecFee": "0.358635",  
                "closedPnl": "0",  
                "createdTime": "1672364262444",  
                "updatedTime": "1672364262457",  
                "rejectReason": "EC_NoError",  
                "stopOrderType": "",  
                "tpslMode": "",  
                "triggerPrice": "",  
                "takeProfit": "",  
                "stopLoss": "",  
                "tpTriggerBy": "",  
                "slTriggerBy": "",  
                "tpLimitPrice": "",  
                "slLimitPrice": "",  
                "triggerDirection": 0,  
                "triggerBy": "",  
                "closeOnTrigger": false,  
                "category": "option",  
                "placeType": "price",  
                "smpType": "None",  
                "smpGroup": 0,  
                "smpOrderId": "",  
                "feeCurrency": "",  
                "cumFeeDetail": {  
                    "MNT": "0.00242968"  
                },  
                "rpiTakerAccess": false,  
                "rpiMatchedQty": "0"  
            }  
        ]  
    }

---

# 訂單

訂閱訂單數據推送

**All-In-One Topic:** `order`  
**Categorised Topic:** `order.spot`, `order.linear`, `order.inverse`, `order.option`

信息

  * All-In-One topic 和 Categorised topic **不能** 放在同一個訂閱請求裡
  * All-In-One topic: 允許您監聽所有業務線的websocket更新(現貨, 正向合約, 反向合約, 期權)
  * Categorised Topic: 您只能監聽您指定的那個業務的websocket更新



提示

當您提交了撤單請求後, 恰巧此時訂單被撮合了, 那麼您可能會接收到兩條orderStatus=`Filled`的消息推送。常見的情況是, 一條消息裡包含 "orderStatus=Filled, rejectReason=EC_NoError", 然後另一條消息包含"orderStatus=Filled, cancelType=CancelByUser, rejectReason=EC_OrigClOrdIDDoesNotExist"。 前者表示訂單成交了, 後者表示由於訂單已成交, 導致對應的撤單請求被拒絕了。

### 響應參數

參數| 類型| 說明  
---|---|---  
id| string| 消息id  
topic| string| Topic名  
creationTime| number| 消息數據創建時間  
data| array| Object  
> category| string| 產品類型 `spot`, `linear`, `inverse`, `option`  
> orderId| string| 訂單ID  
> orderLinkId| string| 用戶自定義ID  
> parentOrderLinkId| string| 表示關聯到的母訂單, 用於關聯附帶的止盈(Take Profit)與止損(Stop Loss)訂單. 支援期貨與期權. 

  * 對止盈或止損訂單進行[修改](/docs/zh-TW/v5/order/amend-order)不會改變parentOrderLinkId
  * **期貨** : 使用[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)修改從原始訂單更新附帶的TP/SL, 不會改變 parentOrderLinkId  
**期權** : 使用[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)修改從原始訂單更新附帶的TP/SL, 會改變 parentOrderLinkId  
**期貨與期權** : 若對原本沒有附帶 TP/SL 的倉位，透過[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)設定 TP/SL, 則parentOrderLinkId沒有實際意義

  
> isLeverage| string| 是否借貸. 僅`spot`有效

  * `0`: 否, 幣幣交易
  * `1`: 是, 槓桿交易

  
> blockTradeId| string| 大宗交易訂單Id  
> symbol| string| 合約名稱  
> price| string| 訂單價格  
> brokerOrderPrice| string| EU流動性經紀商專有字段  
> qty| string| 訂單數量  
> side| string| 方向. `Buy`,`Sell`  
> [positionIdx](/docs/zh-TW/v5/enum#positionidx)| integer| 倉位標識。用戶不同倉位模式  
> [orderStatus](/docs/zh-TW/v5/enum#orderstatus)| string| 訂單狀態  
> [createType](/docs/zh-TW/v5/enum#createtype)| string| 訂單創建類型

  * 僅作用於category=linear 或 inverse
  * 現貨、期權不返回該字段

  
> [cancelType](/docs/zh-TW/v5/enum#canceltype)| string| 訂單被取消類型  
> [rejectReason](/docs/zh-TW/v5/enum#rejectreason)| string| 拒絕原因  
> avgPrice| string| 訂單平均成交價格. 對於不存在avg price的場景, 總返回`""`  
> leavesQty| string| 訂單剩餘未成交的數量  
> leavesValue| string| 訂單剩餘未成交的價值  
> cumExecQty| string| 訂單累計成交數量  
> cumExecValue| string| 訂單累計成交價值  
> cumExecFee| string| 

  * `inverse`, `option`: 訂單累計成交的手續費.
  * `linear`, `spot`: 已棄用. 用`cumFeeDetail`替代.
  * 升級到統一帳戶後, 您可以使用[成交](/docs/zh-TW/v5/websocket/private/execution)頻道中的`execFee`字段來獲取每次成交的手續費

  
> closedPnl| string| 平倉單盈虧, 部分平倉時, 減去了平攤的開倉手續費和期間產生的資金費以及平倉手續費. 該數據和[查詢平倉盈虧](/docs/zh-TW/v5/position/close-pnl)接口裡的"closedPnl"保持一致  
> feeCurrency| string| 已棄用. 現貨交易的手續費幣種. 可以從[這裡](/docs/zh-TW/v5/enum#%E7%8F%BE%E8%B2%A8%E4%BA%A4%E6%98%93%E6%89%8B%E7%BA%8C%E8%B2%BB%E5%B9%A3%E7%A8%AE%E8%AA%AA%E6%98%8E)了解現貨交易的手續費幣種規則  
> [timeInForce](/docs/zh-TW/v5/enum#timeinforce)| string| 執行策略  
> [orderType](/docs/zh-TW/v5/enum#ordertype)| string| 訂單類型. `Market`,`Limit`. 對於止盈止損單, 則表示為觸發後的訂單類型  
> [stopOrderType](/docs/zh-TW/v5/enum#stopordertype)| string| 條件單類型  
> ocoTriggerBy| string| 現貨OCO訂單的觸發類型.`OcoTriggerByUnknown`, `OcoTriggerByTp`, `OcoTriggerBySl`  
> orderIv| string| 隱含波動率  
> marketUnit| string| 現貨交易時給入參`qty`選擇的單位. `baseCoin`, `quoteCoin`  
> slippageToleranceType| string| 市價單滑點容差類型, `TickSize`, `Percent`, `UNKNOWN`(默認值)  
> slippageTolerance| string| 滑點容差數值  
> triggerPrice| string| 觸發價格. 若`stopOrderType`=_TrailingStop_ , 則這是激活價格. 否則, 它是觸發價格  
> takeProfit| string| 止盈價格  
> stopLoss| string| 止損價格  
> tpslMode| string| 止盈止損模式 `Full`: 全部倉位止盈止損, `Partial`: 部分倉位止盈止損  
 _現貨不返回該字段, 期權總是返回""_  
> tpLimitPrice| string| 觸發止盈後轉換為限價單的價格  
> slLimitPrice| string| 觸發止損後轉換為限價單的價格  
> [tpTriggerBy](/docs/zh-TW/v5/enum#triggerby)| string| 觸發止盈的價格類型  
> [slTriggerBy](/docs/zh-TW/v5/enum#triggerby)| string| 觸發止損的價格類型  
> triggerDirection| integer| 觸發方向. `1`: 上漲, `2`: 下跌  
> [triggerBy](/docs/zh-TW/v5/enum#triggerby)| string| 觸發價格的觸發類型  
> lastPriceOnCreated| string| 下單時的市場價格  
> reduceOnly| boolean| 只減倉. `true`表明這是只減倉單  
> closeOnTrigger| boolean| 觸發後平倉委託. [什麼是觸發後平倉委託?](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001050)  
> placeType| string| 期權下單方式. `iv`, `price`  
> [smpType](/docs/zh-TW/v5/enum#smptype)| string| SMP執行類型  
> smpGroup| integer| 所屬Smp組ID. 如果uid不屬於任何組, 則默認為`0`  
> smpOrderId| string| 觸發此SMP執行的交易對手的 orderID  
> createdTime| string| 創建訂單的時間戳 (毫秒)  
> updatedTime| string| 訂單更新的時間戳 (毫秒)  
> cumFeeDetail| json| 

  * `linear`, `spot`: 累積交易費詳情, 替代`cumExecFee`

`  
> rpiTakerAccess| boolean| 訂單的交易對手方是否為RPI訂單。`true`: 交易對手方為RPI訂單, `false`: 交易對手方非RPI訂單。  
> rpiMatchedQty| string| 與RPI訂單作為交易對手方的累計成交數量。  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": [  
            "order"  
        ]  
    }  
    
    
    
    from pybit.unified_trading import WebSocket  
    from time import sleep  
    ws = WebSocket(  
        testnet=True,  
        channel_type="private",  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    def handle_message(message):  
        print(message)  
    ws.order_stream(callback=handle_message)  
    while True:  
        sleep(1)  
    

### 推送示例
    
    
    {  
        "id": "5923240c6880ab-c59f-420b-9adb-3639adc9dd90",  
        "topic": "order",  
        "creationTime": 1672364262474,  
        "data": [  
            {  
                "symbol": "ETH-30DEC22-1400-C",  
                "orderId": "5cf98598-39a7-459e-97bf-76ca765ee020",  
                "side": "Sell",  
                "orderType": "Market",  
                "cancelType": "UNKNOWN",  
                "price": "72.5",  
                "qty": "1",  
                "orderIv": "",  
                "timeInForce": "IOC",  
                "orderStatus": "Filled",  
                "orderLinkId": "",  
                "lastPriceOnCreated": "",  
                "reduceOnly": false,  
                "leavesQty": "",  
                "leavesValue": "",  
                "cumExecQty": "1",  
                "cumExecValue": "75",  
                "closedPnl": "0",  
                "avgPrice": "75",  
                "blockTradeId": "",  
                "positionIdx": 0,  
                "cumExecFee": "0.358635",  
                "createdTime": "1672364262444",  
                "updatedTime": "1672364262457",  
                "rejectReason": "EC_NoError",  
                "stopOrderType": "",  
                "tpslMode": "",  
                "triggerPrice": "",  
                "takeProfit": "",  
                "stopLoss": "",  
                "tpTriggerBy": "",  
                "slTriggerBy": "",  
                "tpLimitPrice": "",  
                "slLimitPrice": "",  
                "triggerDirection": 0,  
                "triggerBy": "",  
                "closeOnTrigger": false,  
                "category": "option",  
                "placeType": "price",  
                "smpType": "None",  
                "smpGroup": 0,  
                "smpOrderId": "",  
                "feeCurrency": "",  
                "cumFeeDetail": {  
                    "MNT": "0.00242968"  
                }  
            }  
        ]  
    }