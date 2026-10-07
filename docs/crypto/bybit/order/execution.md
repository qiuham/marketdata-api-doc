---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/execution
api_type: Trading
updated_at: 2026-10-07 18:53:41.085657
---

# Get Order History

Query order history. As order creation/cancellation is **asynchronous** , the data returned from this endpoint may delay. If you want to get real-time order information, you could query this [endpoint](/docs/v5/order/open-order) or rely on the [websocket stream](/docs/v5/websocket/private/order) (recommended).

rule

  * The orders in the **last 7 days** :  
support querying all [closed status](/docs/v5/enum#orderstatus) except "Cancelled", "Rejected", "Deactivated" status
  * The orders in the **last 24 hours** :  
the orders with "Cancelled" (fully cancelled order), "Rejected", "Deactivated" can be query
  * The orders **beyond 7 days** :   
supports querying orders which have fills only, i.e., fully filled, partial filled but cancelled orders



### HTTP Request

GET`/v5/order/history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`, `spot`, `option`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
baseCoin| false| string| Base coin, uppercase only  
settleCoin| false| string| Settle coin, uppercase only  
orderId| false| string| Order ID  
orderLinkId| false| string| User customised order ID  
orderFilter| false| string| `Order`: active order  
`StopOrder`: conditional order for Futures and Spot  
`tpslOrder`: spot TP/SL order  
`OcoOrder`: spot OCO orders  
`BidirectionalTpslOrder`: Spot bidirectional TPSL order 

  * all kinds of orders are returned by default

  
[orderStatus](/docs/v5/enum#orderstatus)| false| string| Order status  
startTime| false| integer| The start timestamp (ms)

  * startTime and endTime are not passed, return 7 days by default
  * Only startTime is passed, return range between startTime and startTime+7 days
  * Only endTime is passed, return range between endTime-7 days and endTime
  * If both are passed, the rule is endTime - startTime <= 7 days

  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
list| array| Object  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
> parentOrderLinkId| string| Indicates the linked parent order for attached take-profit and stop-loss orders. Supported for futures and options.

  * [Amending](/docs/v5/order/amend-order) take-profit or stop-loss orders does not change the parentOrderLinkId
  * **Futures** : using [set trading stop](/docs/v5/position/trading-stop) to update attached TP/SL from the original order does not change the parentOrderLinkId.
  * **Options** : using [set trading stop](/docs/v5/position/trading-stop) to update attached TP/SL from the original order will change the parentOrderLinkId.
  * **Futures & Options**: if TP/SL is set via [set trading stop](/docs/v5/position/trading-stop) for a position that originally has no attached TP/SL, the parentOrderLinkId is meaningless.

  
> blockTradeId| string| Block trade ID  
> symbol| string| Symbol name  
> price| string| Order price  
> qty| string| Order qty  
> side| string| Side. `Buy`,`Sell`  
> isLeverage| string| Whether to borrow. `0`: false, `1`: true.  
> [positionIdx](/docs/v5/enum#positionidx)| integer| Position index. Used to identify positions in different position modes  
> [orderStatus](/docs/v5/enum#orderstatus)| string| Order status  
> [createType](/docs/v5/enum#createtype)| string| Order create type. Spot does not have this key  
> [cancelType](/docs/v5/enum#canceltype)| string| Cancel type  
> [rejectReason](/docs/v5/enum#rejectreason)| string| Reject reason  
> avgPrice| string| Average filled price, returns `""` for those orders without avg price  
> leavesQty| string| The remaining qty not executed  
> leavesValue| string| The estimated value not executed  
> cumExecQty| string| Cumulative executed order qty  
> cumExecValue| string| Cumulative executed order value  
> cumExecFee| string| 

  * `inverse`, `option`: Cumulative executed trading fee.
  * `linear`, `spot`: Deprecated. Use `cumFeeDetail` instead.

  
> [timeInForce](/docs/v5/enum#timeinforce)| string| Time in force  
> [orderType](/docs/v5/enum#ordertype)| string| Order type. `Market`,`Limit`. For TP/SL orders, is the order type after the order was triggered 

  * `Block trade Roll Back`, `Block trade-Limit`: Unique enum values for Unified account block trades

  
> [stopOrderType](/docs/v5/enum#stopordertype)| string| Stop order type  
> orderIv| string| Implied volatility  
> marketUnit| string| The unit for `qty` when create **Spot market** orders. `baseCoin`, `quoteCoin`  
> slippageToleranceType| string| Spot and Futures market order slippage tolerance type `TickSize`, `Percent`, `UNKNOWN`(default)  
> slippageTolerance| string| Slippage tolerance value  
> triggerPrice| string| Trigger price. If `stopOrderType`=_TrailingStop_ , it is activate price. Otherwise, it is trigger price  
> takeProfit| string| Take profit price  
> stopLoss| string| Stop loss price  
> tpslMode| string| TP/SL mode, `Full`: entire position for TP/SL. `Partial`: partial position tp/sl. Spot does not have this field, and Option returns always ""  
> ocoTriggerBy| string| The trigger type of Spot OCO order.`OcoTriggerByUnknown`, `OcoTriggerByTp`, `OcoTriggerBySl`  
> tpLimitPrice| string| The limit order price when take profit price is triggered  
> slLimitPrice| string| The limit order price when stop loss price is triggered  
> [tpTriggerBy](/docs/v5/enum#triggerby)| string| The price type to trigger take profit  
> [slTriggerBy](/docs/v5/enum#triggerby)| string| The price type to trigger stop loss  
> triggerDirection| integer| Trigger direction. `1`: rise, `2`: fall  
> [triggerBy](/docs/v5/enum#triggerby)| string| The price type of trigger price  
> lastPriceOnCreated| string| Last price when place the order, Spot is not applicable  
> basePrice| string| Last price when place the order, Spot has this field only  
> reduceOnly| boolean| Reduce only. `true` means reduce position size  
> closeOnTrigger| boolean| Close on trigger. [What is a close on trigger order?](https://www.bybit.com/en/help-center/article/Close-On-Trigger-Order)  
> placeType| string| Place type, `option` used. `iv`, `price`  
> [smpType](/docs/v5/enum#smptype)| string| SMP execution type  
> smpGroup| string| Smp group ID. If the UID has no group, it is `"0"` by default  
> smpOrderId| string| The counterparty's orderID which triggers this SMP execution  
> createdTime| string| Order created timestamp (ms)  
> updatedTime| string| Order updated timestamp (ms)  
> extraFees| string| Trading fee rate information. Currently, this data is returned only for spot orders placed on the Indonesian site or spot fiat currency orders placed on the EU site. In other cases, an empty string is returned. Enum: [feeType](/docs/v5/enum#extrafeesfeetype), [subFeeType](/docs/v5/enum#extrafeessubfeetype)  
> cumFeeDetail| json| 

  * `linear`, `spot`: Cumulative trading fee details instead of `cumExecFee`

  
> rpiTakerAccess| boolean| Whether the order has matched with an RPI order as the counterparty. `true`: the counterparty is an RPI order, `false`: the counterparty is not an RPI order.  
> rpiMatchedQty| string| Cumulative quantity matched against RPI orders as the counterparty.  
nextPageCursor| string| Refer to the `cursor` request parameter  
[](/docs/api-explorer/v5/trade/order-list)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/order/history?category=linear&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672221263407  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_order_history(  
        category="linear",  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var orderHistory = TradeOrderRequest.builder().category(CategoryType.LINEAR).limit(10).build();  
    System.out.println(client.getOrderHistory(orderHistory));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getHistoricOrders({  
            category: 'linear',  
            limit: 1,  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "14bad3a1-6454-43d8-bcf2-5345896cf74d",  
                    "orderLinkId": "YLxaWKMiHU",  
                    "blockTradeId": "",  
                    "symbol": "BTCUSDT",  
                    "price": "26864.40",  
                    "qty": "0.003",  
                    "side": "Buy",  
                    "isLeverage": "",  
                    "positionIdx": 1,  
                    "orderStatus": "Cancelled",  
                    "cancelType": "UNKNOWN",  
                    "rejectReason": "EC_PostOnlyWillTakeLiquidity",  
                    "avgPrice": "0",  
                    "leavesQty": "0.000",  
                    "leavesValue": "0",  
                    "cumExecQty": "0.000",  
                    "cumExecValue": "0",  
                    "cumExecFee": "0",  
                    "timeInForce": "PostOnly",  
                    "orderType": "Limit",  
                    "stopOrderType": "UNKNOWN",  
                    "orderIv": "",  
                    "triggerPrice": "0.00",  
                    "takeProfit": "0.00",  
                    "stopLoss": "0.00",  
                    "tpTriggerBy": "UNKNOWN",  
                    "slTriggerBy": "UNKNOWN",  
                    "triggerDirection": 0,  
                    "triggerBy": "UNKNOWN",  
                    "lastPriceOnCreated": "0.00",  
                    "reduceOnly": false,  
                    "closeOnTrigger": false,  
                    "smpType": "None",  
                    "smpGroup": "0",  
                    "smpOrderId": "",  
                    "tpslMode": "",  
                    "tpLimitPrice": "",  
                    "slLimitPrice": "",  
                    "placeType": "",  
                    "slippageToleranceType": "UNKNOWN",  
                    "slippageTolerance": "",  
                    "createdTime": "1684476068369",  
                    "updatedTime": "1684476068372",  
                    "extraFees": "",  
                    "cumFeeDetail": {  
                        "MNT": "0.00242968"  
                    },  
                    "rpiTakerAccess": false,  
                    "rpiMatchedQty": "0"  
                }  
            ],  
            "nextPageCursor": "page_token%3D39380%26",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1684766282976  
    }

---

# 查詢歷史訂單

獲取歷史訂單紀錄. 由於訂單創建/撤銷是**異步** 的, 該接口返回數據可能會有延遲. 若您想實時獲取訂單信息, 您可以查詢該[接口](/docs/zh-TW/v5/order/open-order)或者通過websocket推送(推薦)

提示

  * **7天內的訂單** :   
支持查詢**除了** "Cancelled"(完全取消), "Rejected", "Deactivated"以外的[終態訂單](/docs/zh-TW/v5/enum#orderstatus)
  * **24小時的订单** :   
對於完全取消(Cancelled),以及"Rejected", "Deactivated"的訂單僅支持查詢過去24小時的訂單記錄
  * **7天外的訂單** : 所有账户都只能查詢到有過成交的訂單, 即完全成交, 部分成交但最終取消的訂單



### HTTP請求

GET`/v5/order/history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `spot`, `linear`, `inverse`, `option`  
symbol| false| string| 合約名稱  
baseCoin| false| string| 交易幣種  
settleCoin| false| string| 結算幣種  
orderId| false| string| 訂單ID  
orderLinkId| false| string| 用戶自定義訂單ID  
orderFilter| false| string| `Order`: 普通單, `StopOrder`: 條件單, 支持現貨和期貨  
`tpslOrder`: 現貨止盈止損單, `OcoOrder`: OCO訂單  
`BidirectionalTpslOrder`: 現貨雙向止盈止損訂單 

  * 默認返回全部類型訂單

  
[orderStatus](/docs/zh-TW/v5/enum#orderstatus)| false| string| 訂單狀態, 不傳則默認查詢所有終態訂單  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 7天
  * 若只傳startTime，則查詢startTime和startTime+7天的數據
  * 若只傳endTime，則查詢endTime-7天和endTime的數據

  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> orderId| string| 訂單Id  
> orderLinkId| string| 用戶自定義Id  
> parentOrderLinkId| string| 表示關聯到的母訂單, 用於關聯附帶的止盈(Take Profit)與止損(Stop Loss)訂單. 支援期貨與期權. 

  * 對止盈或止損訂單進行[修改](/docs/zh-TW/v5/order/amend-order)不會改變parentOrderLinkId
  * **期貨** : 使用[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)修改從原始訂單更新附帶的TP/SL, 不會改變 parentOrderLinkId  
**期權** : 使用[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)修改從原始訂單更新附帶的TP/SL, 會改變 parentOrderLinkId  
**期貨與期權** : 若對原本沒有附帶 TP/SL 的倉位，透過[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)設定 TP/SL, 則parentOrderLinkId沒有實際意義

  
> blockTradeId| string| 大宗交易訂單Id  
> symbol| string| 合約名稱  
> price| string| 訂單價格  
> qty| string| 訂單數量  
> side| string| 方向. `Buy`,`Sell`  
> isLeverage| string| 是否借貸. 僅`spot`有效

  * `0`: 否
  * `1`: 是

  
> [positionIdx](/docs/zh-TW/v5/enum#positionidx)| integer| 倉位標識。用戶不同倉位模式  
> [orderStatus](/docs/zh-TW/v5/enum#orderstatus)| string| 訂單狀態  
> [createType](/docs/zh-TW/v5/enum#createtype)| string| 訂單創建類型. 現貨不返回該字段  
> [cancelType](/docs/zh-TW/v5/enum#canceltype)| string| 訂單被取消類型  
> [rejectReason](/docs/zh-TW/v5/enum#rejectreason)| string| 拒絕原因  
> avgPrice| string| 訂單平均成交價格 

  * 不存在avg price場景的訂單將會返回`""`

  
> leavesQty| string| 訂單剩餘未成交的數量  
> leavesValue| string| 訂單剩餘未成交的價值  
> cumExecQty| string| 訂單累計成交數量  
> cumExecValue| string| 訂單累計成交價值  
> cumExecFee| string| 

  * `inverse`, `option`: 訂單累計成交的手續費.
  * `linear`, `spot`: 已棄用. 用`cumFeeDetail`替代.

  
> [timeInForce](/docs/zh-TW/v5/enum#timeinforce)| string| 執行策略  
> [orderType](/docs/zh-TW/v5/enum#ordertype)| string| 訂單類型. `Market`,`Limit`. 對於止盈止損單, 則表示為觸發後的訂單類型  
> [stopOrderType](/docs/zh-TW/v5/enum#stopordertype)| string| 條件單類型  
> orderIv| string| 隱含波動率  
> marketUnit| string| 現貨交易時給入參`qty`選擇的單位. `baseCoin`, `quoteCoin`  
> slippageToleranceType| string| 市價單滑點容差類型, `TickSize`, `Percent`, `UNKNOWN`(默認值)  
> slippageTolerance| string| 滑點容差數值  
> triggerPrice| string| 觸發價格. 若`stopOrderType`=_TrailingStop_ , 則這是激活價格. 否則, 它是觸發價格  
> takeProfit| string| 止盈價格  
> stopLoss| string| 止損價格  
> tpslMode| string| 止盈止損模式 `Full`: 全部倉位止盈止損, `Partial`: 部分倉位止盈止損  
 _現貨不返回該字段, 期權總是返回 ""_  
> ocoTriggerBy| string| 現貨OCO訂單的觸發類型.`OcoTriggerByUnknown`, `OcoTriggerByTp`, `OcoTriggerBySl`  
> tpLimitPrice| string| 觸發止盈後轉換為限價單的價格  
> slLimitPrice| string| 觸發止損後轉換為限價單的價格  
> [tpTriggerBy](/docs/zh-TW/v5/enum#triggerby)| string| 觸發止盈的價格類型  
> [slTriggerBy](/docs/zh-TW/v5/enum#triggerby)| string| 觸發止損的價格類型  
> triggerDirection| integer| 觸發方向. `1`: 上漲, `2`: 下跌  
> [triggerBy](/docs/zh-TW/v5/enum#triggerby)| string| 觸發價格的觸發類型  
> lastPriceOnCreated| string| 下單時的市場價格, 現貨不適用  
> basePrice| string| 下單時的市場價格, 僅現貨有這個字段  
> reduceOnly| boolean| 只減倉. `true`表明這是只減倉單  
> closeOnTrigger| boolean| 觸發後平倉委託. [什麼是觸發後平倉委託?](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001050)  
> placeType| string| 下單類型, 僅期權使用. `iv`, `price`  
> [smpType](/docs/zh-TW/v5/enum#smptype)| string| SMP執行類型  
> smpGroup| string| 所屬Smp組ID. 如果uid不屬於任何組, 則默認為`"0"`  
> smpOrderId| string| 觸發此SMP執行的交易對手的 orderID  
> createdTime| string| 創建訂單的時間戳 (毫秒)  
> updatedTime| string| 訂單更新的時間戳 (毫秒)  
> extraFees| string| 交易費率。目前，僅針對kyc=Indian用戶或在印尼網站的現貨訂單或在歐盟站的現貨法定貨幣訂單返回此數據。在其他情況下，傳回空字串。字段枚舉: [feeType](/docs/zh-TW/v5/enum#extrafeesfeetype), [subFeeType](/docs/zh-TW/v5/enum#extrafeessubfeetype)  
> cumFeeDetail| json| `linear`, `spot`: 累積交易費詳情, 替代`cumExecFee`  
> rpiTakerAccess| boolean| 訂單的交易對手方是否為RPI訂單。`true`: 交易對手方為RPI訂單, `false`: 交易對手方非RPI訂單。  
> rpiMatchedQty| string| 與RPI訂單作為交易對手方的累計成交數量。  
[](/docs/zh-TW/api-explorer/v5/trade/order-list)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/order/history?category=linear&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672221263407  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_order_history(  
        category="linear",  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var orderHistory = TradeOrderRequest.builder().category(CategoryType.LINEAR).limit(10).build();  
    System.out.println(client.getOrderHistory(orderHistory));  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getHistoricOrders({  
            category: 'linear',  
            limit: 1,  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "14bad3a1-6454-43d8-bcf2-5345896cf74d",  
                    "orderLinkId": "YLxaWKMiHU",  
                    "blockTradeId": "",  
                    "symbol": "BTCUSDT",  
                    "price": "26864.40",  
                    "qty": "0.003",  
                    "side": "Buy",  
                    "isLeverage": "",  
                    "positionIdx": 1,  
                    "orderStatus": "Cancelled",  
                    "cancelType": "UNKNOWN",  
                    "rejectReason": "EC_PostOnlyWillTakeLiquidity",  
                    "avgPrice": "0",  
                    "leavesQty": "0.000",  
                    "leavesValue": "0",  
                    "cumExecQty": "0.000",  
                    "cumExecValue": "0",  
                    "cumExecFee": "0",  
                    "timeInForce": "PostOnly",  
                    "orderType": "Limit",  
                    "stopOrderType": "UNKNOWN",  
                    "orderIv": "",  
                    "triggerPrice": "0.00",  
                    "takeProfit": "0.00",  
                    "stopLoss": "0.00",  
                    "tpTriggerBy": "UNKNOWN",  
                    "slTriggerBy": "UNKNOWN",  
                    "triggerDirection": 0,  
                    "triggerBy": "UNKNOWN",  
                    "lastPriceOnCreated": "0.00",  
                    "reduceOnly": false,  
                    "closeOnTrigger": false,  
                    "smpType": "None",  
                    "smpGroup": "0",  
                    "smpOrderId": "",  
                    "tpslMode": "",  
                    "tpLimitPrice": "",  
                    "slLimitPrice": "",  
                    "placeType": "",  
                    "slippageToleranceType": "UNKNOWN",  
                    "slippageTolerance": "",  
                    "createdTime": "1684476068369",  
                    "updatedTime": "1684476068372",  
                    "extraFees":"",  
                    "cumFeeDetail": {  
                        "MNT": "0.00242968"  
                    },  
                    "rpiTakerAccess": false,  
                    "rpiMatchedQty": "0"  
                }  
            ],  
            "nextPageCursor": "page_token%3D39380%26",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1684766282976  
    }