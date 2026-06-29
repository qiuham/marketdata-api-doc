---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/batch-cancel
api_type: Trading
updated_at: 2026-06-29 19:30:57.647264
---

# Batch Place Order

tip

This endpoint allows you to place more than one order in a single request.

  * Make sure you have sufficient funds in your account when placing an order. Once an order is placed, according to the funds required by the order, the funds in your account will be frozen by the corresponding amount during the life cycle of the order.
  * A maximum of 20 orders (option), 20 orders (inverse), 20 orders (linear), 10 orders (spot) can be placed per request. The returned data list is divided into two lists. The first list indicates whether or not the order creation was successful and the second list details the created order information. The structure of the two lists are completely consistent.



info

  * **Option rate limt** instruction: its rate limit is count based on the actual number of request sent, e.g., by default, option trading rate limit is 10 reqs per sec, so you can send up to 20 * 10 = 200 orders in one second. 
  * **Perpetual, Futures, Spot rate limit instruction** , please check [here](/docs/v5/rate-limit#instructions-for-batch-endpoints)
  * **Risk control limit notice:**  
Bybit will monitor on your API requests. When the total number of orders of a single user (aggregated the number of orders across main account and subaccounts) within a day (UTC 0 - UTC 24) exceeds a certain upper limit, the platform will reserve the right to remind, warn, and impose necessary restrictions. Customers who use API default to acceptance of these terms and have the obligation to cooperate with adjustments.



### HTTP Request

POST`/v5/order/create-batch`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `option`, `spot`, `inverse`  
request| **true**|  array| Object  
> symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
> isLeverage| false| integer| Whether to borrow, `spot`** only. `0`(default): false then spot trading, `1`: true then margin trading  
> side| **true**|  string| `Buy`, `Sell`  
> [orderType](/docs/v5/enum#ordertype)| **true**|  string| `Market`, `Limit`  
> qty| **true**|  string| Order quantity 

  * Spot: set `marketUnit` for market order qty unit, `quoteCoin` for market buy by default, `baseCoin` for market sell by default
  * Perps, Futures & Option: always use base coin as unit.
  * Perps & Futures: If you pass `qty`="0" and specify `reduceOnly`=true&`closeOnTrigger`=true, you can close the position up to `maxMktOrderQty` or `maxOrderQty` shown on [Get Instruments Info](/docs/v5/market/instrument) of current symbol

  
> marketUnit| false| string| The unit for `qty` when create **Spot market** orders, `orderFilter`="tpslOrder" and "StopOrder" are supported as well.

  * `baseCoin`: for example, buy BTCUSDT, then "qty" unit is BTC
  * `quoteCoin`: for example, sell BTCUSDT, then "qty" unit is USDT

  
> price| false| string| Order price 

  * Market order will ignore this field
  * Please check the min price and price precision from [instrument info](/docs/v5/market/instrument#response-parameters) endpoint
  * If you have position, price needs to be better than liquidation price

  
> triggerDirection| false| integer| Conditional order param. Used to identify the expected direction of the conditional order. 

  * `1`: triggered when market price rises to `triggerPrice`
  * `2`: triggered when market price falls to `triggerPrice`

Valid for `linear`  
> orderFilter| false| string| If it is not passed, `Order` by default. 

  * `Order`
  * `tpslOrder`: Spot TP/SL order, the assets are occupied even before the order is triggered
  * `StopOrder`: Spot conditional order, the assets will not be occupied until the price of the underlying asset reaches the trigger price, and the required assets will be occupied after the Conditional order is triggered

Valid for `spot` **only**  
> triggerPrice| false| string| 

  * For Perps & Futures, it is the conditional order trigger price. If you expect the price to rise to trigger your conditional order, make sure:  
_triggerPrice > market price_  
Else, _triggerPrice < market price_
  * For spot, it is the `orderFilter`="tpslOrder", or "StopOrder" trigger price

  
> [triggerBy](/docs/v5/enum#triggerby)| false| string| Conditional order param (Perps & Futures). Trigger price type. `LastPrice`, `IndexPrice`, `MarkPrice`  
> orderIv| false| string| Implied volatility. `option` **only**. Pass the real value, e.g for 10%, 0.1 should be passed. `orderIv` has a higher priority when `price` is passed as well  
> [timeInForce](/docs/v5/enum#timeinforce)| false| string| [Time in force](https://www.bybit.com/en/help-center/article/What-Are-Time-In-Force-TIF-GTC-IOC-FOK)

  * Market order will use `IOC` directly
  * If not passed, `GTC` is used by default

  
> [positionIdx](/docs/v5/enum#positionidx)| false| integer| Used to identify positions in different position modes. Under hedge-mode, this param is **required**

  * `0`: one-way mode
  * `1`: hedge-mode Buy side
  * `2`: hedge-mode Sell side

  
> orderLinkId| false| string| User customised order ID. A max of 36 characters. Combinations of numbers, letters (upper and lower cases), dashes, and underscores are supported.  
_Futures, Perps & Spot: orderLinkId rules:_

  * optional param
  * always unique

 _Options orderLinkId rules:_

  * **required** param
  * always unique

  
> takeProfit| false| string| Take profit price  
> stopLoss| false| string| Stop loss price  
> [tpTriggerBy](/docs/v5/enum#triggerby)| false| string| The price type to trigger take profit. `MarkPrice`, `IndexPrice`, default: `LastPrice`.  
Valid for `linear`, `inverse`  
> [slTriggerBy](/docs/v5/enum#triggerby)| false| string| The price type to trigger stop loss. `MarkPrice`, `IndexPrice`, default: `LastPrice`  
Valid for `linear`, `inverse`  
> reduceOnly| false| boolean| [What is a reduce-only order?](https://www.bybit.com/en/help-center/article/Reduce-Only-Order) `true` means your position can only reduce in size if this order is triggered. 

  * You **must** specify it as `true` when you are about to close/reduce the position
  * When reduceOnly is true, take profit/stop loss cannot be set

Valid for `linear`, `inverse` & `option`  
> closeOnTrigger| false| boolean| [What is a close on trigger order?](https://www.bybit.com/en/help-center/article/Close-On-Trigger-Order) For a closing order. It can only reduce your position, not increase it. If the account has insufficient available balance when the closing order is triggered, then other active orders of similar contracts will be cancelled or reduced. It can be used to ensure your stop loss reduces your position regardless of current available margin.  
Valid for `linear`, `inverse`  
> [smpType](/docs/v5/enum#smptype)| false| string| Smp execution type. [What is SMP?](/docs/v5/smp)  
> mmp| false| boolean| Market maker protection. `option` **only**. `true` means set the order as a market maker protection order. [What is mmp?](/docs/v5/account/set-mmp)  
> tpslMode| false| string| TP/SL mode 

  * `Full`: entire position for TP/SL. Then, tpOrderType or slOrderType must be `Market`
  * `Partial`: partial position tp/sl (as there is no size option, so it will create tp/sl orders with the qty you actually fill). Limit TP/SL order are supported. Note: When create limit tp/sl, tpslMode is **required** and it must be `Partial`

Valid for `linear`, `inverse`  
> tpLimitPrice| false| string| The limit order price when take profit price is triggered 

  * `linear`&`inverse`: only works when tpslMode=Partial and tpOrderType=Limit
  * Spot: it is required when the order has `takeProfit` and `tpOrderType=Limit`

  
> slLimitPrice| false| string| The limit order price when stop loss price is triggered

  * `linear`&`inverse`: only works when tpslMode=Partial and slOrderType=Limit
  * Spot: it is required when the order has `stopLoss` and `slOrderType=Limit`

  
> tpOrderType| false| string| The order type when take profit is triggered 

  * `linear`&`inverse`: `Market`(default), `Limit`. For tpslMode=Full, it only supports tpOrderType=Market
  * Spot:   
`Market`: when you set "takeProfit",   
`Limit`: when you set "takeProfit" and "tpLimitPrice" 

  
> slOrderType| false| string| The order type when stop loss is triggered 

  * `linear`&`inverse`: `Market`(default), `Limit`. For tpslMode=Full, it only supports slOrderType=Market
  * Spot:   
`Market`: when you set "stopLoss",   
`Limit`: when you set "stopLoss" and "slLimitPrice" 

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| Object|   
> list| array| Object  
>> category| string| Product type  
>> symbol| string| Symbol name  
>> orderId| string| Order ID  
>> orderLinkId| string| User customised order ID  
>> createAt| string| Order created time (ms)  
retExtInfo| Object|   
> list| array| Object  
>> code| number| Success/error code  
>> msg| string| Success/error message  
  
info

The acknowledgement of an place order request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

[](/docs/api-explorer/v5/trade/batch-place)

* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/create-batch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672222064519  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "spot",  
        "request": [  
            {  
                "symbol": "BTCUSDT",  
                "side": "Buy",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "0.05",  
                "price": "30000",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-btc-03"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "side": "Sell",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "2",  
                "price": "12",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-atom-03"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.place_batch_order(  
        category="spot",  
        request=[  
            {  
                "symbol": "BTCUSDT",  
                "side": "Buy",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "0.05",  
                "price": "30000",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-btc-03"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "side": "Sell",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "2",  
                "price": "12",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-atom-03"  
            }  
        ]  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "https://github.com/bybit-exchange/bybit.go.api")  
    client := bybit.NewBybitHttpClient("YOUR_API_KEY", "YOUR_API_SECRET", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "option",  
        "request": []map[string]interface{}{  
            {  
                "category":    "option",  
                "symbol":      "BTC-10FEB23-24000-C",  
                "orderType":   "Limit",  
                "side":        "Buy",  
                "qty":         "0.1",  
                "price":       "5",  
                "orderIv":     "0.1",  
                "timeInForce": "GTC",  
                "orderLinkId": "9b381bb1-401",  
                "mmp":         false,  
                "reduceOnly":  false,  
            },  
            {  
                "category":    "option",  
                "symbol":      "BTC-10FEB23-24000-C",  
                "orderType":   "Limit",  
                "side":        "Buy",  
                "qty":         "0.1",  
                "price":       "5",  
                "orderIv":     "0.1",  
                "timeInForce": "GTC",  
                "orderLinkId": "82ee86dd-001",  
                "mmp":         false,  
                "reduceOnly":  false,  
            },  
        },  
    }  
    client.NewUtaBybitServiceWithParams(params).PlaceBatchOrder(context.Background())  
    
    
    
    import com.bybit.api.client.restApi.BybitApiAsyncTradeRestClient;  
    import com.bybit.api.client.domain.ProductType;  
    import com.bybit.api.client.domain.TradeOrderType;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    import java.util.Arrays;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var orderRequests = Arrays.asList(TradeOrderRequest.builder().category(ProductType.OPTION).symbol("BTC-10FEB23-24000-C").side(Side.BUY).orderType(TradeOrderType.LIMIT).qty("0.1")  
                            .price("5").orderIv("0.1").timeInForce(TimeInForce.GOOD_TILL_CANCEL).orderLinkId("9b381bb1-401").mmp(false).reduceOnly(false).build(),  
                    TradeOrderRequest.builder().category(ProductType.OPTION).symbol("BTC-10FEB23-24000-C").side(Side.BUY).orderType(TradeOrderType.LIMIT).qty("0.1")  
                            .price("5").orderIv("0.1").timeInForce(TimeInForce.GOOD_TILL_CANCEL).orderLinkId("82ee86dd-001").mmp(false).reduceOnly(false).build());  
    var createBatchOrders = BatchOrderRequest.builder().category(ProductType.OPTION).request(orderRequests).build();  
    client.createBatchOrder(createBatchOrders, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    var order1 = new OrderRequest { Symbol = "XRPUSDT", OrderType = "Limit", Side = "Buy", Qty = "10", Price = "0.6080", TimeInForce = "GTC" };  
    var order2 = new OrderRequest { Symbol = "BLZUSDT", OrderType = "Limit", Side = "Buy", Qty = "10", Price = "0.6080", TimeInForce = "GTC" };  
    List<OrderRequest> request = new() { order1, order2 };  
    var orderInfoString = await TradeService.PlaceBatchOrder(category: Category.LINEAR, request: request);  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .batchSubmitOrders('spot', [  
            {  
                "symbol": "BTCUSDT",  
                "side": "Buy",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "0.05",  
                "price": "30000",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-btc-03"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "side": "Sell",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "2",  
                "price": "12",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-atom-03"  
            },  
        ])  
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
                    "category": "spot",  
                    "symbol": "BTCUSDT",  
                    "orderId": "1666800494330512128",  
                    "orderLinkId": "spot-btc-03",  
                    "createAt": "1713434102752"  
                },  
                {  
                    "category": "spot",  
                    "symbol": "ATOMUSDT",  
                    "orderId": "1666800494330512129",  
                    "orderLinkId": "spot-atom-03",  
                    "createAt": "1713434102752"  
                }  
            ]  
        },  
        "retExtInfo": {  
            "list": [  
                {  
                    "code": 0,  
                    "msg": "OK"  
                },  
                {  
                    "code": 0,  
                    "msg": "OK"  
                }  
            ]  
        },  
        "time": 1713434102753  
    }

---

# 批量創建委託單

提示

該接口支持批量創建委託單

  * 下單時需確保帳戶內有足夠的資金。一旦下單，根據訂單所需資金，您的帳戶資金將在訂單生命週期內凍結相應額度，被凍結的資金額度取決於訂單屬性。
  * 每個請求包含的訂單數最大是: 20筆(期权), 20筆(反向合約), 20筆(正向合約), 10筆(現貨), 返回的數據列表中分成兩個list，訂單創建的列表和創建結果的信息返回，兩個list的訂單的序列是完全保持一致的。



信息

  * **期權** 批量接口頻率規則: 期權是按照實際發送的請求次數來統計頻率的, 因此如果帳戶頻率是10次/秒, 每次請求發送20筆訂單, 則可以每秒發送200筆訂單;

  * **期貨和現貨** 的批量接口頻率規則: 請從[這裡](/docs/zh-TW/v5/rate-limit#%E6%89%B9%E9%87%8F%E6%8E%A5%E5%8F%A3%E9%99%90%E9%A0%BB%E8%AA%AA%E6%98%8E)查閱其API限頻說明

  * **風控限制提示:**  
Bybit 將針對您的 API 請求進行統計監控，當單日 (UTC 0点 - UTC 24点) 單帳號（母帳號和子帳號整體運算）訂單總数超過一定上限，平台將保留提醒、警告，以及進行必要性限制的權利。 使用API的客戶預設接受本條款並負有配合調整的義務。




### HTTP請求

POST`/v5/order/create-batch`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `option`, `spot`, `inverse`  
request| **true**|  array| Object  
> symbol| **true**|  string| 合約名稱  
> isLeverage| false| integer| 是否走現貨槓桿下單. `0`(default): 否，是幣幣訂單, `1`: 是，是槓桿訂單  
> side| **true**|  string| 方向. `Buy`, `Sell`  
> [orderType](/docs/zh-TW/v5/enum#ordertype)| **true**|  string| 訂單類型. `Market`, `Limit`  
> qty| **true**|  string| 訂單數量 訂單數量 

  * 現貨: 可以通過設置`marketUnit`來表示市價單qty的單位, 市價買單默認是`quoteCoin`, 市價賣單默認是`baseCoin`
  * 期貨和期權: 總是以base coin作為qty的單位
  * 期貨: 如果傳入`qty`="0"以及`reduceOnly`="true", 則可以平掉對應合約可達單個訂單允許的最大qty的倉位, 參照[查詢可交易產品的規格信息](/docs/zh-TW/v5/market/instrument)接口裡的字段`maxMktOrderQty`或者`maxOrderQty`

  
> price| false| string| 訂單價格 

  * 市價單將會忽視該字段
  * 請通過該[接口](/docs/zh-TW/v5/market/instrument#response-parameters)確認最低價格和精度要求
  * 如果有持倉, 確保價格優於強平價格

  
> marketUnit| false| string| **現貨交易** 創建市價單時給入參`qty`指定的單位, 支持orderFilter=Order, tpslOrder 和 StopOrder

  * `baseCoin`: 比如, 買BTCUSDT, 則"qty"的單位是BTC
  * `quoteCoin`: 比如, 賣BTCUSDT, 則"qty"的單位是USDT

  
> triggerDirection| false| integer| 條件單參數. 用於辨別期望的方向. 

  * `1`: 當市場價上漲到了`triggerPrice`時觸發條件單
  * `2`: 當市場價下跌到了`triggerPrice`時觸發條件單

僅`linear`有效  
> orderFilter| false| string| 指定訂單品種, 若不傳, 默認`Order`

  * `Order`: 普通單
  * `tpslOrder`: 止盈止損單
  * `StopOrder`: 條件單

僅對現貨有效  
> triggerPrice| false| string| 

  * 對於期貨, 是條件單觸發價格參數. 若您希望市場價是要上升後觸發, 確保:  
_triggerPrice > 市場價格_  
否則, _triggerPrice < 市場價格_
  * 對於現貨, 這是下止盈止損單(orderFilter=tpslOrder)或者條件單(orderFilter=stopOrder)的觸發價格參數

  
> [triggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 條件單參數. 觸發價格類型. `LastPrice`, `IndexPrice`, `MarkPrice`  
僅`linear`有效  
> orderIv| false| string| 隱含波動率. 僅`option`有效. 按照實際值傳入, e.g., 對於10%, 則傳入0.1. `orderIv`比`price`有更高的優先級  
> [timeInForce](/docs/zh-TW/v5/enum#timeinforce)| false| string| [訂單執行策略](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001044)

  * 市價單，系統直接使用`IOC`
  * 若不傳，默認使用`GTC`

  
> [positionIdx](/docs/zh-TW/v5/enum#positionidx)| false| integer| 倉位標識, 用戶不同倉位模式. 該字段對於雙向持倉模式是**必傳** :

  * `0`: 單向持倉
  * `1`: 買側雙向持倉
  * `2`: 賣側雙向持倉

  
> orderLinkId| false| string| 用戶自定義訂單Id. category=`option`時，該參數必傳  
> takeProfit| false| string| 止盈價格  
> stopLoss| false| string| 止損價格  
> [tpTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 觸發止盈的價格類型 

  * `MarkPrice`
  * `IndexPrice`
  * `LastPrice`(默認)

  
僅對`linear`和`inverse`有效  
> [slTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 觸發止損的價格類型 

  * `MarkPrice`
  * `IndexPrice`
  * `LastPrice`(默認)

  
僅對`linear`和`inverse`有效  
> reduceOnly| false| boolean| [什麼是只減倉?](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001047) `true` 將這筆訂單設為只減倉 

  * 當減倉時, reduceOnly=true**必傳**
  * 只減倉單的止盈止損不生效

  
> closeOnTrigger| false| boolean| [什麼是觸發後平倉委託?](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001050)此選項可以確保您的止損單被用於減倉（平倉）而非加倉，並且在可用保證金不足的情況下，取消其他委託，騰出保證金以確保平倉委託的執行.  
`linear`, `inverse`有效  
> [smpType](/docs/zh-TW/v5/enum#smptype)| false| string| Smp執行類型. [什麼是SMP?](/docs/zh-TW/v5/smp)  
> mmp| false| boolean| 做市商保護. 僅`option`有效. `true` 表示該訂單是做市商保護訂單. [什麼是做市商保護?](/docs/zh-TW/v5/account/set-mmp)  
> tpslMode| false| string| 止盈止損模式 

  * `Full`: 全部倉位止盈止損. 此時, tpOrderType或者slOrderType必須傳`Market`
  * `Partial`: 部分倉位止盈止損(下單時沒有size選項, 實際上創建tpsl訂單時, 是按照實際成交的數量來生成止盈止損). 注意: 創建限價止盈止損時, tpslMode**必傳** 且為Partial

`linear`, `inverse`有效  
> tpLimitPrice| false| string| 觸發止盈後轉換為限價單的價格 

  * `linear` & `inverse`: 僅作用於當tpslMode=Partial以及tpOrderType=Limit時
  * 現貨: 參數必傳當創建訂單時帶了`takeProfit` 和 `tpOrderType=Limit`

  
> slLimitPrice| false| string| 觸發止損後轉換為限價單的價格 

  * `linear` & `inverse`: 僅作用於當tpslMode=Partial以及slOrderType=Limit時
  * 現貨: 參數必傳當創建訂單時帶了`stopLoss` 和 `slOrderType=Limit`

  
> tpOrderType| false| string| 止盈觸發後的訂單類型 

  * category="linear"或"inverse": `Market`(默認), `Limit`  
對於tpslMode=Full, 僅支持tpOrderType=Market


  * 現貨:   
`Market`: 當帶了參數"takeProfit",   
`Limit`: 當帶了參數"takeProfit" 和 "tpLimitPrice" 

  
> slOrderType| false| string| 止損觸發後的訂單類型 

  * category="linear"或"inverse": `Market`(默認), `Limit`  
對於tpslMode=Full, 僅支持slOrderType=Market
  * 現貨:   
`Market`: 當帶了參數"stopLoss",   
`Limit`: 當帶了參數"stopLoss" 和 "slLimitPrice" 

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| Object|   
> list| array| Object  
>> category| string| 產品類型  
>> symbol| string| 合約名稱  
>> orderId| string| 訂單Id  
>> orderLinkId| string| 用戶自定義訂單Id  
>> createAt| string| 訂單創建時間 (毫秒)  
retExtInfo| Object|   
> list| array| Object  
>> code| number| 成功/錯誤碼  
>> msg| string| 成功/錯誤消息  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

[](/docs/zh-TW/api-explorer/v5/trade/batch-place)

* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/create-batch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672222064519  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "spot",  
        "request": [  
            {  
                "symbol": "BTCUSDT",  
                "side": "Buy",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "0.05",  
                "price": "30000",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-btc-03"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "side": "Sell",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "2",  
                "price": "12",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-atom-03"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.place_batch_order(  
        category="spot",  
        request=[  
            {  
                "symbol": "BTCUSDT",  
                "side": "Buy",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "0.05",  
                "price": "30000",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-btc-03"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "side": "Sell",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "2",  
                "price": "12",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-atom-03"  
            }  
        ]  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "https://github.com/bybit-exchange/bybit.go.api")  
    client := bybit.NewBybitHttpClient("YOUR_API_KEY", "YOUR_API_SECRET", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "spot",  
        "request": []map[string]interface{}{  
            {  
                "symbol": "BTCUSDT",  
                "side": "Buy",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "0.05",  
                "price": "30000",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-btc-03"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "side": "Sell",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "2",  
                "price": "12",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-atom-03"  
            },  
        },  
    }  
    client.NewUtaBybitServiceWithParams(params).PlaceBatchOrder(context.Background())  
    
    
    
    import com.bybit.api.client.restApi.BybitApiAsyncTradeRestClient;  
    import com.bybit.api.client.domain.ProductType;  
    import com.bybit.api.client.domain.TradeOrderType;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    import java.util.Arrays;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var orderRequests = Arrays.asList(TradeOrderRequest.builder().category(ProductType.OPTION).symbol("BTC-10FEB23-24000-C").side(Side.BUY).orderType(TradeOrderType.LIMIT).qty("0.1")  
                            .price("5").orderIv("0.1").timeInForce(TimeInForce.GOOD_TILL_CANCEL).orderLinkId("9b381bb1-401").mmp(false).reduceOnly(false).build(),  
                    TradeOrderRequest.builder().category(ProductType.OPTION).symbol("BTC-10FEB23-24000-C").side(Side.BUY).orderType(TradeOrderType.LIMIT).qty("0.1")  
                            .price("5").orderIv("0.1").timeInForce(TimeInForce.GOOD_TILL_CANCEL).orderLinkId("82ee86dd-001").mmp(false).reduceOnly(false).build());  
    var createBatchOrders = BatchOrderRequest.builder().category(ProductType.OPTION).request(orderRequests).build();  
    client.createBatchOrder(createBatchOrders, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    var order1 = new OrderRequest { Symbol = "XRPUSDT", OrderType = "Limit", Side = "Buy", Qty = "10", Price = "0.6080", TimeInForce = "GTC" };  
    var order2 = new OrderRequest { Symbol = "BLZUSDT", OrderType = "Limit", Side = "Buy", Qty = "10", Price = "0.6080", TimeInForce = "GTC" };  
    List<OrderRequest> request = new() { order1, order2 };  
    var orderInfoString = await TradeService.PlaceBatchOrder(category: Category.LINEAR, request: request);  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .batchSubmitOrders('spot', [  
            {  
                "symbol": "BTCUSDT",  
                "side": "Buy",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "0.05",  
                "price": "30000",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-btc-03"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "side": "Sell",  
                "orderType": "Limit",  
                "isLeverage": 0,  
                "qty": "2",  
                "price": "12",  
                "timeInForce": "GTC",  
                "orderLinkId": "spot-atom-03"  
            },  
        ])  
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
                    "category": "spot",  
                    "symbol": "BTCUSDT",  
                    "orderId": "1666800494330512128",  
                    "orderLinkId": "spot-btc-03",  
                    "createAt": "1713434102752"  
                },  
                {  
                    "category": "spot",  
                    "symbol": "ATOMUSDT",  
                    "orderId": "1666800494330512129",  
                    "orderLinkId": "spot-atom-03",  
                    "createAt": "1713434102752"  
                }  
            ]  
        },  
        "retExtInfo": {  
            "list": [  
                {  
                    "code": 0,  
                    "msg": "OK"  
                },  
                {  
                    "code": 0,  
                    "msg": "OK"  
                }  
            ]  
        },  
        "time": 1713434102753  
    }