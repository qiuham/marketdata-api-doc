---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/pre-upgrade/order-list
api_type: REST
updated_at: 2026-07-15 18:54:48.947448
---

# Get Pre-upgrade Order History

After the account is upgraded to a Unified account, you can get the orders which occurred before the upgrade.

By category="linear", you can query USDT Perps, USDC Perps data occurred during classic account  
By category="spot", you can query Spot data occurred during classic account  
By category="option", you can query Options data occurred during classic account  
By category="inverse", you can query Inverse Contract data occurred during **classic account or[UTA1.0](/docs/v5/acct-mode#uta-10)**

info

  * can get all status in 7 days
  * can only get filled orders beyond 7 days
  * USDC Perpeual & Option support the recent 6 months data. Please download older data via GUI



### HTTP Request

GET`/v5/pre-upgrade/order/history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`, `option`, `spot`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only. 

  * If not passed, return settleCoin=USDT by default
  * To get USDC perp, please pass symbol

  
baseCoin| false| string| Base coin, uppercase only. Used for `option` query  
orderId| false| string| Order ID  
orderLinkId| false| string| User customised order ID  
orderFilter| false| string| `Order`: active order, `StopOrder`: conditional order  
[orderStatus](/docs/v5/enum#orderstatus)| false| string| Order status. Not supported for `spot` category  
startTime| false| integer| The start timestamp (ms) 

  * `startTime` and `endTime` must be passed together or both are not passed
  * endTime - startTime <= 7 days
  * If both are not passed, it returns recent 7 days by default

  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
[category](/docs/v5/enum#category)| string| Product type  
list| array| Object  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
> blockTradeId| string| Block trade ID  
> symbol| string| Symbol name  
> price| string| Order price  
> qty| string| Order qty  
> side| string| Side. `Buy`,`Sell`  
> isLeverage| string| Useless field for those orders before upgraded  
> [positionIdx](/docs/v5/enum#positionidx)| integer| Position index. Used to identify positions in different position modes  
> [orderStatus](/docs/v5/enum#orderstatus)| string| Order status  
> [cancelType](/docs/v5/enum#canceltype)| string| Cancel type  
> [rejectReason](/docs/v5/enum#rejectreason)| string| Reject reason  
> avgPrice| string| Average filled price. If unfilled, it is `""`, and also for those orders have partilly filled but cancelled at the end  
> leavesQty| string| The remaining qty not executed  
> leavesValue| string| The estimated value not executed  
> cumExecQty| string| Cumulative executed order qty  
> cumExecValue| string| Cumulative executed order value  
> cumExecFee| string| Cumulative executed trading fee  
> [timeInForce](/docs/v5/enum#timeinforce)| string| Time in force  
> [orderType](/docs/v5/enum#ordertype)| string| Order type. `Market`,`Limit`  
> [stopOrderType](/docs/v5/enum#stopordertype)| string| Stop order type  
> orderIv| string| Implied volatility  
> triggerPrice| string| Trigger price. If `stopOrderType`=_TrailingStop_ , it is activate price. Otherwise, it is trigger price  
> takeProfit| string| Take profit price  
> stopLoss| string| Stop loss price  
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
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example
    
    
    GET /v5/pre-upgrade/order/history?category=linear&limit=1&orderStatus=Filled HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682576940304  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "67836246-460e-4c52-a009-af0c3e1d12bc",  
                    "orderLinkId": "",  
                    "blockTradeId": "",  
                    "symbol": "BTCUSDT",  
                    "price": "27203.40",  
                    "qty": "0.200",  
                    "side": "Sell",  
                    "isLeverage": "",  
                    "positionIdx": 0,  
                    "orderStatus": "Filled",  
                    "cancelType": "UNKNOWN",  
                    "rejectReason": "EC_NoError",  
                    "avgPrice": "28632.126000",  
                    "leavesQty": "0.000",  
                    "leavesValue": "0",  
                    "cumExecQty": "0.200",  
                    "cumExecValue": "5726.4252",  
                    "cumExecFee": "3.43585512",  
                    "timeInForce": "IOC",  
                    "orderType": "Market",  
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
                    "reduceOnly": true,  
                    "closeOnTrigger": true,  
                    "smpType": "None",  
                    "smpGroup": 0,  
                    "smpOrderId": "",  
                    "createdTime": "1682487465732",  
                    "updatedTime": "1682487465735",  
                    "placeType": ""  
                }  
            ],  
            "nextPageCursor": "page_token%3D69406%26",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1682576940540  
    }

---

# 查詢升級前訂單紀錄

支持查詢升級到統一帳戶之前發生的USDT永續, USDC永續, 反向合約, 現貨和期權

信息

  * 7天內, 可以查詢到全狀態的紀錄
  * 7天外, 僅能查詢到已成交的紀錄
  * USDC永續和期權僅支持查詢最近6個月的數據, 對於更老的數據, 請前往網頁端下載
  * 通過category=linear, 查詢到在經典帳戶期間產生的USDT永續, USDC永續數據  

  * 通過category=spot, 查詢到在經典帳戶期間產生的現貨數據  

  * 通過category=option, 查詢到在經典帳戶期間產生的期權數據  

  * 通過category=inverse, 查詢到在**經典帳戶或者[統一帳戶1.0](/docs/zh-TW/v5/acct-mode#%E7%B5%B1%E4%B8%80%E5%B8%B3%E6%88%B610)**期間產生的反向合約數據



### HTTP 請求

GET`/v5/pre-upgrade/order/history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `linear`, `inverse`, `option`, `spot`  
symbol| false| string| 合約名稱. 

  * 對於`linear`, 如果不傳symbol, 默認返回數據是結算幣種=USDT
  * 要查詢USDC永續, 請傳遞對應的合約名稱

  
baseCoin| false| string| 交易幣種. 期權的預留字段  
orderId| false| string| 訂單ID  
orderLinkId| false| string| 用戶自定義訂單ID  
orderFilter| false| string| `Order`: 普通單, `StopOrder`: 條件單  
[orderStatus](/docs/zh-TW/v5/enum#orderstatus)| false| string| 訂單狀態. 不支持現貨  
startTime| false| integer| 開始時間戳 (毫秒) 

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 7天

  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
[category](/docs/zh-TW/v5/enum#category)| string| 產品類型  
list| array| Object  
> orderId| string| 訂單Id  
> orderLinkId| string| 用戶自定義Id  
> blockTradeId| string| 大宗交易訂單Id  
> symbol| string| 合約名稱  
> price| string| 訂單價格  
> qty| string| 訂單數量  
> side| string| 方向. `Buy`,`Sell`  
> isLeverage| string| 該字段對升級前的帳戶訂單無意義  
> [positionIdx](/docs/zh-TW/v5/enum#positionidx)| integer| 倉位標識。用戶不同倉位模式  
> [orderStatus](/docs/zh-TW/v5/enum#orderstatus)| string| 訂單狀態  
> [cancelType](/docs/zh-TW/v5/enum#canceltype)| string| 訂單被取消類型  
> [rejectReason](/docs/zh-TW/v5/enum#rejectreason)| string| 拒絕原因  
> avgPrice| string| 訂單平均成交價格. 若沒有成交，則返回`""`, 以及部分成交但最終被手動取消的訂單  
> leavesQty| string| 訂單剩餘未成交的數量  
> leavesValue| string| 訂單剩餘未成交的價值  
> cumExecQty| string| 訂單累計成交數量  
> cumExecValue| string| 訂單累計成交價值  
> cumExecFee| string| 訂單累計成交的手續費  
> [timeInForce](/docs/zh-TW/v5/enum#timeinforce)| string| 執行策略  
> [orderType](/docs/zh-TW/v5/enum#ordertype)| string| 訂單類型. `Market`,`Limit`  
> [stopOrderType](/docs/zh-TW/v5/enum#stopordertype)| string| 條件單類型  
> orderIv| string| 隱含波動率  
> triggerPrice| string| 觸發價格. 若`stopOrderType`=_TrailingStop_ , 則這是激活價格. 否則, 它是觸發價格  
> takeProfit| string| 止盈價格  
> stopLoss| string| 止損價格  
> [tpTriggerBy](/docs/zh-TW/v5/enum#triggerby)| string| 觸發止盈的價格類型  
> [slTriggerBy](/docs/zh-TW/v5/enum#triggerby)| string| 觸發止損的價格類型  
> triggerDirection| integer| 觸發方向. `1`: 上漲, `2`: 下跌  
> [triggerBy](/docs/zh-TW/v5/enum#triggerby)| string| 觸發價格的觸發類型  
> lastPriceOnCreated| string| 下單時的市場價格  
> reduceOnly| boolean| 只減倉. `true`表明這是只減倉單  
> closeOnTrigger| boolean| 觸發後平倉委託. [什麼是觸發後平倉委託?](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001050)  
> placeType| string| 下單類型, 僅期權使用. `iv`, `price`  
> [smpType](/docs/zh-TW/v5/enum#smptype)| string| SMP執行類型  
> smpGroup| integer| 所屬Smp組ID. 如果uid不屬於任何組, 則默認為`0`  
> smpOrderId| string| 觸發此SMP執行的交易對手的 orderID  
> createdTime| string| 創建訂單的時間戳 (毫秒)  
> updatedTime| string| 訂單更新的時間戳 (毫秒)  
nextPageCursor| string| 游標，用於翻頁  
  
### Request Example
    
    
    GET /v5/pre-upgrade/order/history?category=linear&limit=1&orderStatus=Filled HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1682576940304  
    X-BAPI-RECV-WINDOW: 5000  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "orderId": "67836246-460e-4c52-a009-af0c3e1d12bc",  
                    "orderLinkId": "",  
                    "blockTradeId": "",  
                    "symbol": "BTCUSDT",  
                    "price": "27203.40",  
                    "qty": "0.200",  
                    "side": "Sell",  
                    "isLeverage": "",  
                    "positionIdx": 0,  
                    "orderStatus": "Filled",  
                    "cancelType": "UNKNOWN",  
                    "rejectReason": "EC_NoError",  
                    "avgPrice": "28632.126000",  
                    "leavesQty": "0.000",  
                    "leavesValue": "0",  
                    "cumExecQty": "0.200",  
                    "cumExecValue": "5726.4252",  
                    "cumExecFee": "3.43585512",  
                    "timeInForce": "IOC",  
                    "orderType": "Market",  
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
                    "reduceOnly": true,  
                    "closeOnTrigger": true,  
                    "smpType": "None",  
                    "smpGroup": 0,  
                    "smpOrderId": "",  
                    "createdTime": "1682487465732",  
                    "updatedTime": "1682487465735",  
                    "placeType": ""  
                }  
            ],  
            "nextPageCursor": "page_token%3D69406%26",  
            "category": "linear"  
        },  
        "retExtInfo": {},  
        "time": 1682576940540  
    }