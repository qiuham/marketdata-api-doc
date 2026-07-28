---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spread/trade/open-order
api_type: Trading
updated_at: 2026-07-28 19:04:49.365091
---

# Get Order History

info

  * orderId & orderLinkId has a higher priority than startTime & endTime
  * Fully cancelled orders are stored for up to 24 hours.



**Single leg orders can also be found with "createType"=`CreateByFutureSpread` via [Get Order History](/docs/v5/order/order-list)**

### HTTP Request

GET`/v5/spread/order/history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
symbol| false| string| Spread combination symbol name  
baseCoin| false| string| Base coin  
orderId| false| string| Spread combination order ID  
orderLinkId| false| string| User customised order ID  
startTime| false| long| The start timestamp (ms)

  * startTime and endTime are not passed, return 7 days by default
  * Only startTime is passed, return range between startTime and startTime+7 days
  * Only endTime is passed, return range between endTime-7 days and endTime
  * If both are passed, the rule is endTime - startTime <= 7 days

  
endTime| false| long| The end timestamp (ms)  
limit| false| integer| Limit for data size per page. [`1`, `50`]. Default: `20`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array<object>| Order info  
> symbol| string| Spread combination symbol name  
> orderType| string| Order type, `Market`, `Limit`  
> orderLinkId| string| User customised order ID  
> orderId| string| Spread combination order ID  
> contractType| string| Combo type 

  * `FundingRateArb`: perpetual & spot combination
  * `CarryTrade`: futures & spot combination
  * `FutureSpread`: different expiry futures combination
  * `PerpBasis`: futures & perpetual

  
> [cxlRejReason](/docs/v5/enum#rejectreason)| string| Reject reason  
> [orderStatus](/docs/v5/enum#orderstatus)| string| Order status, `Rejected`, `Cancelled`, `Filled`  
> price| string| Order price  
> orderQty| string| Order qty  
> timeInForce| string| Time in force, `GTC`, `FOK`, `IOC`, `PostOnly`  
> baseCoin| string| Base coin  
> createdAt| string| Order created timestamp (ms)  
> updatedAt| string| Order updated timestamp (ms)  
> side| string| Side, `Buy`, `Sell`  
> leavesQty| string| The remaining qty not executed. It is meaningless for a cancelled order  
> settleCoin| string| Settle coin  
> cumExecQty| string| Cumulative executed order qty  
> qty| string| Order qty  
> leg1Symbol| string| Leg1 symbol name  
> leg1ProdType| string| Leg1 product type, `Futures`, `Spot`  
> leg1OrderId| string| Leg1 order ID  
> leg1Side| string| Leg1 order side  
> leg2ProdType| string| Leg2 product type, `Futures`, `Spot`  
> leg2OrderId| string| Leg2 order ID  
> leg2Symbol| string| Leg2 symbol name  
> leg2Side| string| Leg2 orde side  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/spread/order/history?orderId=aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744100522465  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spread_get_order_history(  
        orderId="aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4"  
    ))  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "nextPageCursor": "aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4%3A1744096099767%2Caaaee090-fab3-42ea-aea0-c9fbfe6c4bc4%3A1744096099767",  
            "list": [  
                {  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "orderType": "Limit",  
                    "orderLinkId": "",  
                    "orderId": "aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4",  
                    "contractType": "FundingRateArb",  
                    "orderStatus": "Cancelled",  
                    "createdAt": "1744096099767",  
                    "price": "-4",  
                    "leg2Symbol": "SOLUSDT",  
                    "orderQty": "0.1",  
                    "timeInForce": "PostOnly",  
                    "baseCoin": "SOL",  
                    "updatedAt": "1744098396079",  
                    "side": "Buy",  
                    "leg2Side": "Sell",  
                    "leavesQty": "0",  
                    "leg1Side": "Buy",  
                    "settleCoin": "USDT",  
                    "cumExecQty": "0",  
                    "qty": "0.1",  
                    "leg1OrderId": "82335b0a-b7d9-4ea5-9230-e71271a65100",  
                    "leg2OrderId": "1924011967786517249",  
                    "leg2ProdType": "Spot",  
                    "leg1ProdType": "Futures",  
                    "leg1Symbol": "SOLUSDT"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1744102655725  
    }

---

# 查詢價差訂單歷史

信息

  * orderId 和 orderLinkId優先級高於startTime 和 endTime
  * 完全取消單保存24小時



**單腿的訂單信息也會出現[查詢訂單歷史](/docs/zh-TW/v5/order/order-list)接口中**, 標記是"createType"=`CreateByFutureSpread`

### HTTP請求

GET`/v5/spread/order/history`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
symbol| false| string| 價差產品名稱  
baseCoin| false| string| 交易幣種  
orderId| false| string| 價差訂單ID  
orderLinkId| false| string| 用戶自定義ID  
startTime| false| long| 開始時間戳 (毫秒)

  * startTime 和 endTime都不傳入, 則默認返回最近7天的數據
  * startTime 和 endTime都傳入的話, 則確保endTime - startTime <= 7天
  * 若只傳startTime，則查詢startTime和startTime+7天的數據
  * 若只傳endTime，則查詢endTime-7天和endTime的數據

  
endTime| false| long| 結束時間戳 (毫秒)  
limit| false| integer| 每頁數量限制. [`1`, `50`]. 默認: `20`  
cursor| false| string| 游標，用於翻頁  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array<object>| 訂單信息  
> symbol| string| 價差產品名稱  
> orderType| string| 訂單類型, `Market`, `Limit`  
> orderLinkId| string| 用戶自定義ID  
> orderId| string| 價差訂單ID  
> contractType| string| 價差類型 

  * `FundingRateArb`: 永續 & 現貨組合
  * `CarryTrade`: 到期合約& 現貨組合
  * `FutureSpread`: 不同到期日合約組合
  * `PerpBasis`: 到期合約& 永續組合

  
> [cxlRejReason](/docs/zh-TW/v5/enum#rejectreason)| string| 拒絕理由  
> [orderStatus](/docs/zh-TW/v5/enum#orderstatus)| string| 訂單狀態`Filled`, `Cancelled`  
> price| string| 訂單價格  
> orderQty| string| 訂單數量  
> timeInForce| string| 訂單執行策略, `GTC`, `FOK`, `IOC`, `PostOnly`  
> baseCoin| string| 交易幣種  
> createdAt| string| 訂單創建時間 (毫秒)  
> updatedAt| string| 訂單更新時間 (毫秒)  
> side| string| 訂單方向, `Buy`, `Sell`  
> leavesQty| string| 剩餘未成交數量. 對於撤銷單來說無意義  
> settleCoin| string| 結算幣種  
> cumExecQty| string| 累計成交數量  
> qty| string| 訂單數量  
> leg1Symbol| string| 單腿1的合約名稱  
> leg1ProdType| string| 單腿1的產品類型, `Spot`(現貨), `Futures`(期貨)  
> leg1OrderId| string| 單腿1的訂單ID  
> leg1Side| string| 單腿1的訂單方向  
> leg2ProdType| string| 單腿2的產品類型, `Spot`(現貨), `Futures`(期貨)  
> leg2OrderId| string| 單腿2的訂單ID  
> leg2Symbol| string| 單腿2的合約名稱  
> leg2Side| string| 單腿2的訂單方向  
nextPageCursor| string| 游標，用於翻頁  
  
### 請求示例
    
    
    GET /v5/spread/order/history?orderId=aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1744100522465  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "Success",  
        "result": {  
            "nextPageCursor": "aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4%3A1744096099767%2Caaaee090-fab3-42ea-aea0-c9fbfe6c4bc4%3A1744096099767",  
            "list": [  
                {  
                    "symbol": "SOLUSDT_SOL/USDT",  
                    "orderType": "Limit",  
                    "orderLinkId": "",  
                    "orderId": "aaaee090-fab3-42ea-aea0-c9fbfe6c4bc4",  
                    "contractType": "FundingRateArb",  
                    "orderStatus": "Cancelled",  
                    "createdAt": "1744096099767",  
                    "price": "-4",  
                    "leg2Symbol": "SOLUSDT",  
                    "orderQty": "0.1",  
                    "timeInForce": "PostOnly",  
                    "baseCoin": "SOL",  
                    "updatedAt": "1744098396079",  
                    "side": "Buy",  
                    "leg2Side": "Sell",  
                    "leavesQty": "0",  
                    "leg1Side": "Buy",  
                    "settleCoin": "USDT",  
                    "cumExecQty": "0",  
                    "qty": "0.1",  
                    "leg1OrderId": "82335b0a-b7d9-4ea5-9230-e71271a65100",  
                    "leg2OrderId": "1924011967786517249",  
                    "leg2ProdType": "Spot",  
                    "leg1ProdType": "Futures",  
                    "leg1Symbol": "SOLUSDT"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1744102655725  
    }