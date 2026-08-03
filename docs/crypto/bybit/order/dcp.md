---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/dcp
api_type: Trading
updated_at: 2026-08-03 19:07:54.948098
---

# Get Open & Closed Orders

Primarily query unfilled or partially filled orders in **real-time** , but also supports querying recent 500 closed status (Cancelled, Filled) orders. Please see the usage of request param `openOnly`.  
And to query older order records, please use the [order history](/docs/v5/order/order-list) interface.

tip

  * You can query filled, cancelled, and rejected orders to the most recent 500 orders for spot, linear, inverse and option categories
  * You can query by symbol, baseCoin, orderId and orderLinkId, and if you pass multiple params, the system will process them according to this priority: orderId > orderLinkId > symbol > baseCoin.
  * The records are sorted by the `createdTime` from newest to oldest.



info

  * After a server release or restart, filled, cancelled, and rejected orders of Unified account should only be queried through [order history](/docs/v5/order/order-list).
  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/order/realtime`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type `linear`, `inverse`, `spot`, `option`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only. For **linear** , either `symbol`, `baseCoin`, `settleCoin` is **required**  
baseCoin| false| string| Base coin, uppercase only 

  * Supports `linear`, `inverse` & `option`
  * `option`: it returns all option open orders by default

  
settleCoin| false| string| Settle coin, uppercase only 

  * **linear** : either `symbol`, `baseCoin` or `settleCoin` is **required**
  * `spot`: not supported
  * `option`: USDT or USDC

  
orderId| false| string| Order ID  
orderLinkId| false| string| User customised order ID  
openOnly| false| integer| 

  * `0`(default): query open status orders (e.g., New, PartiallyFilled) **only**
  * `1`: Query a maximum of recent 500 closed status records are kept under each account each category (e.g., Cancelled, Rejected, Filled orders).  
_If the Bybit service is restarted due to an update, this part of the data will be cleared and accumulated again, but the order records will still be queried in[order history](/docs/v5/order/order-list)_
  * `openOnly` param will be ignored when query by _orderId_ or _orderLinkId_

  
orderFilter| false| string| `Order`: active order, `StopOrder`: conditional order for Futures and Spot, `tpslOrder`: spot TP/SL order, `OcoOrder`: Spot oco order, `BidirectionalTpslOrder`: Spot bidirectional TPSL order

  * all kinds of orders by default

  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Product type  
nextPageCursor| string| Refer to the `cursor` request parameter  
list| array| Object  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
> parentOrderLinkId| string| Indicates the linked parent order for attached take-profit and stop-loss orders. Supported for futures and options.

  * [Amending](/docs/v5/order/amend-order) take-profit or stop-loss orders does not change the parentOrderLinkId
  * **Futures** : using [set trading stop](/docs/v5/position/trading-stop) to update attached TP/SL from the original order does not change the parentOrderLinkId.
  * **Options** : using [set trading stop](/docs/v5/position/trading-stop) to update attached TP/SL from the original order will change the parentOrderLinkId.
  * **Futures & Options**: if TP/SL is set via [set trading stop](/docs/v5/position/trading-stop)for a position that originally has no attached TP/SL, the parentOrderLinkId is meaningless.

  
> blockTradeId| string| Paradigm block trade ID  
> symbol| string| Symbol name  
> price| string| Order price  
> qty| string| Order qty  
> side| string| Side. `Buy`,`Sell`  
> isLeverage| string| Whether to borrow `0`: false, `1`: true  
> [positionIdx](/docs/v5/enum#positionidx)| integer| Position index. Used to identify positions in different position modes.  
> [orderStatus](/docs/v5/enum#orderstatus)| string| Order status  
> [createType](/docs/v5/enum#createtype)| string| Order create type 

  * Spot does not have this key

  
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
> [stopOrderType](/docs/v5/enum#stopordertype)| string| Stop order type  
> orderIv| string| Implied volatility  
> marketUnit| string| The unit for `qty` when create **Spot market** orders. `baseCoin`, `quoteCoin`  
> triggerPrice| string| Trigger price. If `stopOrderType`=_TrailingStop_ , it is activate price. Otherwise, it is trigger price  
> takeProfit| string| Take profit price  
> stopLoss| string| Stop loss price  
> tpslMode| string| TP/SL mode, `Full`: entire position for TP/SL. `Partial`: partial position tp/sl. Spot does not have this field, and Option returns always ""  
> ocoTriggerBy| string| The trigger type of Spot OCO order.`OcoTriggerByUnknown`, `OcoTriggerByTp`, `OcoTriggerByBySl`  
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
> smpGroup| integer| Smp group ID. If the UID has no group, it is `0` by default  
> smpOrderId| string| The counterparty's orderID which triggers this SMP execution  
> createdTime| string| Order created timestamp (ms)  
> updatedTime| string| Order updated timestamp (ms)  
> cumFeeDetail| json| 

  * `linear`, `spot`: Cumulative trading fee details instead of `cumExecFee`

  
[](/docs/api-explorer/v5/trade/open-order)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/order/realtime?symbol=ETHUSDT&category=linear&openOnly=0&limit=1  HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672219525810  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_open_orders(  
        category="linear",  
        symbol="ETHUSDT",  
        openOnly=0,  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var openLinearOrdersResult = client.getOpenOrders(openOrderRequest.category(CategoryType.LINEAR).openOnly(1).build());  
    System.out.println(openLinearOrdersResult);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getActiveOrders({  
            category: 'linear',  
            symbol: 'ETHUSDT',  
            openOnly: 0,  
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
                    "orderId": "fd4300ae-7847-404e-b947-b46980a4d140",  
                    "orderLinkId": "test-000005",  
                    "blockTradeId": "",  
                    "symbol": "ETHUSDT",  
                    "price": "1600.00",  
                    "qty": "0.10",  
                    "side": "Buy",  
                    "isLeverage": "",  
                    "positionIdx": 1,  
                    "orderStatus": "New",  
                    "cancelType": "UNKNOWN",  
                    "rejectReason": "EC_NoError",  
                    "avgPrice": "0",  
                    "leavesQty": "0.10",  
                    "leavesValue": "160",  
                    "cumExecQty": "0.00",  
                    "cumExecValue": "0",  
                    "cumExecFee": "0",  
                    "timeInForce": "GTC",  
                    "orderType": "Limit",  
                    "stopOrderType": "UNKNOWN",  
                    "orderIv": "",  
                    "triggerPrice": "0.00",  
                    "takeProfit": "2500.00",  
                    "stopLoss": "1500.00",  
                    "tpTriggerBy": "LastPrice",  
                    "slTriggerBy": "LastPrice",  
                    "triggerDirection": 0,  
                    "triggerBy": "UNKNOWN",  
                    "lastPriceOnCreated": "",  
                    "reduceOnly": false,  
                    "closeOnTrigger": false,  
                    "smpType": "None",  
                    "smpGroup": 0,  
                    "smpOrderId": "",  
                    "tpslMode": "Full",  
                    "tpLimitPrice": "",  
                    "slLimitPrice": "",  
                    "placeType": "",  
                    "createdTime": "1684738540559",  
                    "updatedTime": "1684738540561",  
                    "cumFeeDetail": {  
                        "MNT": "0.00242968"  
                    }  
                }  
            ],  
            "nextPageCursor": "page_args%3Dfd4300ae-7847-404e-b947-b46980a4d140%26symbol%3D6%26",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1684765770483  
    }

---

# 查詢實時和終態委託單

主要用於實時查詢未成交或部分成交的訂單信息, 但結合入参`openOnly`能夠查詢到最近500條到達終態的訂單. 若需要查詢更久的訂單紀錄，請使用[查詢歷史訂單](/docs/zh-TW/v5/order/order-list)接口.

提示

  * 支持查詢已成交, 取消和拒絕類型的最近500條訂單信息對於spot, linear, inverse和option類別. 
  * 您可以通過指定symbol, baseCoin, orderId 和 orderLinkId字段來查詢. 如果您使用多字段組合，系統的查詢優先級如下: orderId > orderLinkId > symbol > baseCoin.
  * 返回的結果將以`createdTime`從新到舊排序.



信息

  * 服務器重啓或發佈後請使用[查詢歷史訂單](/docs/zh-TW/v5/order/order-list)接口去查詢已成交，取消和拒絕類型的訂單信息
  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP請求

GET`/v5/order/realtime`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型 `spot`, `linear`, `inverse`, `option`  
symbol| false| string| 合約名稱

  * 當category=**linear** , `symbol`, `baseCoin` 和 `settleCoin`**必傳** 其中一個

  
baseCoin| false| string| 交易幣種

  * 支持`linear`, `inverse`和`option`
  * 對於category=**option** , 若不傳baseCoin, 則返回期權下所有活動委託單

  
settleCoin| false| string| 結算幣種 

  * **linear** : `symbol` 和 `settleCoin`**必傳** 其中一個
  * `spot`: 該字段無效
  * `option`: USDT 或 USDC

  
orderId| false| string| 訂單Id  
orderLinkId| false| string| 用戶自定義訂單Id  
openOnly| false| integer| 

  * `0`(默認): 僅查詢活動委託訂單, 比如New, PartiallyFilled訂單
  * `1`: 返回僅終態（已取消/拒絕/完全成交）的訂單數據, 每個帳戶每個category下最多保留500條紀錄. _如果因Bybit服務更新重啟則該部分數據會情況並重新累計, 但是訂單紀錄仍然可以從[歷史訂單](/docs/zh-TW/v5/order/order-list)中查詢到_
  * 當查詢是按照 _orderId_ 或者 _orderLinkId_ 時, `openOnly`入参將會被忽略

  
orderFilter| false| string| `Order`: 活動單  
`StopOrder`: 條件單, 支持現貨和期貨  
`tpslOrder`: 止盈止損單, 僅現貨有效  
`OcoOrder`: OCO訂單  
`BidirectionalTpslOrder`: 現貨雙向止盈止損訂單  
默認返回全部類型訂單  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
nextPageCursor| string| 游標，用於翻頁  
list| array| Object  
> orderId| string| 訂單Id  
> orderLinkId| string| 用戶自定義Id  
> parentOrderLinkId| string| 表示關聯到的母訂單, 用於關聯附帶的止盈(Take Profit)與止損(Stop Loss)訂單. 支援期貨與期權. 

  * 對止盈或止損訂單進行[修改](/docs/zh-TW/v5/order/amend-order)不會改變parentOrderLinkId
  * **期貨** : 使用[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)修改從原始訂單更新附帶的TP/SL, 不會改變 parentOrderLinkId  
**期權** : 使用[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)修改從原始訂單更新附帶的TP/SL, 會改變 parentOrderLinkId  
**期貨與期權** : 若對原本沒有附帶 TP/SL 的倉位，透過[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)設定 TP/SL, 則parentOrderLinkId沒有實際意義

  
> blockTradeId| string| Paradigm大宗交易Id  
> symbol| string| 合約名稱  
> price| string| 訂單價格  
> qty| string| 訂單數量  
> side| string| 方向. `Buy`,`Sell`  
> isLeverage| string| 是否借貸. 僅`spot`有效

  * `0`: 否
  * `1`: 是

  
> [positionIdx](/docs/zh-TW/v5/enum#positionidx)| integer| 倉位標識。用戶不同倉位模式  
> [orderStatus](/docs/zh-TW/v5/enum#orderstatus)| string| 訂單狀態  
> [createType](/docs/zh-TW/v5/enum#createtype)| string| 訂單創建類型

  * 現貨不返回該字段

  
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
> triggerPrice| string| 觸發價格. 若`stopOrderType`=_TrailingStop_ , 則這是激活價格. 否則, 它是觸發價格  
> takeProfit| string| 止盈價格  
> stopLoss| string| 止損價格  
> tpslMode| string| 止盈止損模式 `Full`: 全部倉位止盈止損, `Partial`: 部分倉位止盈止損  
現貨不返回該字段, 期權總是返回""  
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
> smpGroup| integer| 所屬Smp組ID. 如果uid不屬於任何組, 則默認為`0`  
> smpOrderId| string| 觸發此SMP執行的交易對手的 orderID  
> createdTime| string| 創建訂單的時間戳 (毫秒)  
> updatedTime| string| 訂單更新的時間戳 (毫秒)  
> cumFeeDetail| json| `linear`, `spot`: 累積交易費詳情, 替代`cumExecFee`  
[](/docs/zh-TW/api-explorer/v5/trade/open-order)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * Node.js


    
    
    GET /v5/order/realtime?symbol=ETHUSDT&category=linear&openOnly=0&limit=1  HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672219525810  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_open_orders(  
        category="linear",  
        symbol="ETHUSDT",  
        openOnly=0,  
        limit=1,  
    ))  
    
    
    
    import com.bybit.api.client.config.BybitApiConfig;  
    import com.bybit.api.client.domain.trade.request.TradeOrderRequest;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET", BybitApiConfig.TESTNET_DOMAIN).newTradeRestClient();  
    var openLinearOrdersResult = client.getOpenOrders(openOrderRequest.category(CategoryType.LINEAR).openOnly(1).build());  
    System.out.println(openLinearOrdersResult);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .getActiveOrders({  
            category: 'linear',  
            symbol: 'ETHUSDT',  
            openOnly: 0,  
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
                    "orderId": "fd4300ae-7847-404e-b947-b46980a4d140",  
                    "orderLinkId": "test-000005",  
                    "blockTradeId": "",  
                    "symbol": "ETHUSDT",  
                    "price": "1600.00",  
                    "qty": "0.10",  
                    "side": "Buy",  
                    "isLeverage": "",  
                    "positionIdx": 1,  
                    "orderStatus": "New",  
                    "cancelType": "UNKNOWN",  
                    "rejectReason": "EC_NoError",  
                    "avgPrice": "0",  
                    "leavesQty": "0.10",  
                    "leavesValue": "160",  
                    "cumExecQty": "0.00",  
                    "cumExecValue": "0",  
                    "cumExecFee": "0",  
                    "timeInForce": "GTC",  
                    "orderType": "Limit",  
                    "stopOrderType": "UNKNOWN",  
                    "orderIv": "",  
                    "triggerPrice": "0.00",  
                    "takeProfit": "2500.00",  
                    "stopLoss": "1500.00",  
                    "tpTriggerBy": "LastPrice",  
                    "slTriggerBy": "LastPrice",  
                    "triggerDirection": 0,  
                    "triggerBy": "UNKNOWN",  
                    "lastPriceOnCreated": "",  
                    "reduceOnly": false,  
                    "closeOnTrigger": false,  
                    "smpType": "None",  
                    "smpGroup": 0,  
                    "smpOrderId": "",  
                    "tpslMode": "Full",  
                    "tpLimitPrice": "",  
                    "slLimitPrice": "",  
                    "placeType": "",  
                    "createdTime": "1684738540559",  
                    "updatedTime": "1684738540561",  
                    "cumFeeDetail": {  
                        "MNT": "0.00242968"  
                    }  
                }  
            ],  
            "nextPageCursor": "page_args%3Dfd4300ae-7847-404e-b947-b46980a4d140%26symbol%3D6%26",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1684765770483  
    }