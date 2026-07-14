---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/batch-place
api_type: Trading
updated_at: 2026-07-14 18:55:21.801757
---

# Place Order

This endpoint supports to create the order for Spot, Margin trading, USDT perpetual, USDT futures, USDC perpetual, USDC futures, Inverse Futures and Options.

info

  * **Supported order type (`orderType`):**  
Limit order: `orderType`=_Limit_ , it is necessary to specify order qty and price.  


[Market order](https://www.bybit.com/en/help-center/article/Types-of-Orders-Available-on-Bybit): `orderType`=_Market_ , execute at the best price in the Bybit market until the transaction is completed. When selecting a market order, the "price" can be empty. In the trading system, in order to protect traders against the serious slippage of the Market order, Bybit trading engine will convert the market order into an IOC limit order for matching. If there are no orderbook entries within price slippage limit, the order will not be executed. If there is insufficient liquidity, the order will be cancelled. The slippage threshold refers to the percentage that the order price deviates from the mark price. You can learn more here: [Adjustments to Bybit's Derivative Trading Price Limit Mechanism](https://announcements.bybit.com/en/article/adjustments-to-bybit-s-derivative-trading-limit-order-mechanism-blt469228de1902fff6/)
  * **Supported timeInForce strategy:**  
`GTC`  
`IOC`  
`FOK`  
`PostOnly`: If the order would be filled immediately when submitted, it will be **cancelled**. The purpose of this is to protect your order during the submission process. If the matching system cannot entrust the order to the order book due to price changes on the market, it will be cancelled.  
`RPI`: Retail Price Improvement order. Assigned market maker can place this kind of order, and it is a post only order, only match with the order from Web or APP.

  * **How to create a conditional order:**  
When submitting an order, if `triggerPrice` is set, the order will be automatically converted into a conditional order. In addition, the conditional order does not occupy the margin. If the margin is insufficient after the conditional order is triggered, the order will be cancelled.

  * **[Take profit / Stop loss](https://www.bybit.com/en/help-center/article/Introduction-to-Take-Profit-Stop-Loss-Perpetual-Futures-Contracts)** : You can set TP/SL while placing orders. Besides, you could modify the position's TP/SL.

  * **Order quantity** : The quantity of perpetual contracts you are going to buy/sell. For the order quantity, Bybit only supports positive number at present.

  * **Order price** : Place a limit order, this parameter is **required**. If you have position, the price should be higher than the _liquidation price_. For the minimum unit of the price change, please refer to the `priceFilter` > `tickSize` field in the [instruments-info](/docs/v5/market/instrument) endpoint.

  * **orderLinkId** : You can customize the active order ID. We can link this ID to the order ID in the system. Once the active order is successfully created, we will send the unique order ID in the system to you. Then, you can use this order ID to cancel active orders, and if both orderId and orderLinkId are entered in the parameter input, Bybit will prioritize the orderId to process the corresponding order. Meanwhile, your customized order ID should be no longer than 36 characters and should be **unique**.

  * **Open orders up limit:**  
**Perps & Futures:**   
a) Each account can hold a maximum of _500_ **active** orders simultaneously **per symbol.**  
b) **conditional** orders: each account can hold a maximum of **10 active orders** simultaneously **per symbol**.   
**Spot:** 500 orders in total, including a maximum of 30 open TP/SL orders, a maximum of 30 open conditional orders for each symbol per account  
**Option:** a maximum of 50 open orders in the coin dimension by default. 

  * **Rate limit:**  
Please refer to [rate limit table](/docs/v5/rate-limit#trade). If you need to raise the rate limit, please contact your client manager or submit an application via [here](https://www.bybit.com/en/institutional)

  * **Risk control limit notice:**  
Bybit will monitor on your API requests. When the total number of orders of a single user (aggregated the number of orders across main account and subaccounts) within a day (UTC 0 - UTC 24) exceeds a certain upper limit, the platform will reserve the right to remind, warn, and impose necessary restrictions. Customers who use API default to acceptance of these terms and have the obligation to cooperate with adjustments.

  * **Reduce only orders:**  
If reduceOnly=true and order qty > max order qty, the order will automatically be split up into multiple orders.




### HTTP Request

POST`/v5/order/create`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| Product type `linear`, `inverse`, `spot`, `option`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
isLeverage| false| integer| Whether to borrow. 

  * `0`(default): false, spot trading
  * `1`: true, margin trading, _make sure you turn on margin trading, and set the relevant currency as collateral_

  
side| **true**|  string| `Buy`, `Sell`  
[orderType](/docs/v5/enum#ordertype)| **true**|  string| `Market`, `Limit`  
qty| **true**|  string| Order quantity 

  * Spot: Market Buy order by value by default, you can set `marketUnit` field to choose order by value or qty for market orders
  * Perps, Futures & Option: always order by qty
  * Perps & Futures: if you pass `qty`="0" and specify `reduceOnly`=true&`closeOnTrigger`=true, you can close the position up to `maxMktOrderQty` or `maxOrderQty` shown on [Get Instruments Info](/docs/v5/market/instrument) of current symbol

  
marketUnit| false| string| Select the unit for `qty` when create **Spot market** orders

  * `baseCoin`: for example, buy BTCUSDT, then "qty" unit is BTC
  * `quoteCoin`: for example, sell BTCUSDT, then "qty" unit is USDT

  
rpiTakerAccess| false| boolean| `true`: Your order will be eligible to match against RPI quotes, `false`: not eligible. Please read the [RPI taker feature](https://announcements.bybit.com/en/article/rpi-liquidity-now-available-to-api-taker-orders-bltb943887bfa4c4d17/)  
slippageToleranceType| false| string| Slippage tolerance Type for **market order** , `TickSize`, `Percent`

  * take profit, stoploss, conditional orders are not supported
  * **TickSize** :   
the highest price of Buy order = ask1 + `slippageTolerance` x tickSize;   
the lowest price of Sell order = bid1 - `slippageTolerance` x tickSize
  * **Percent** :   
the highest price of Buy order = ask1 x (1 + `slippageTolerance` x 0.01);   
the lowest price of Sell order = bid1 x (1 - `slippageTolerance` x 0.01)
  * Learn more about slippage tolerance in the [help centre](https://www.bybit.com/en/help-center/article/Market-Order-with-Slippage-Tolerance)

  
slippageTolerance| false| string| Slippage tolerance value 

  * `TickSize`: range is [1, 10000], integer only
  * `Percent`: range is [0.01, 10], up to 2 decimals

  
price| false| string| Order price 

  * Market order will ignore this field
  * Please check the min price and price precision from [instrument info](/docs/v5/market/instrument#response-parameters) endpoint
  * If you have position, price needs to be better than liquidation price

  
triggerDirection| false| integer| Conditional order param. Used to identify the expected direction of the conditional order. 

  * `1`: triggered when market price rises to `triggerPrice`
  * `2`: triggered when market price falls to `triggerPrice`

Valid for `linear` & `inverse`  
orderFilter| false| string| If it is not passed, `Order` by default. 

  * `Order`
  * `tpslOrder`: Spot TP/SL order, the assets are occupied even before the order is triggered
  * `StopOrder`: Spot conditional order, the assets will not be occupied until the price of the underlying asset reaches the trigger price, and the required assets will be occupied after the Conditional order is triggered

Valid for `spot` **only**  
triggerPrice| false| string| 

  * For Perps & Futures, it is the conditional order trigger price. If you expect the price to rise to trigger your conditional order, make sure:  
_triggerPrice > market price_  
Else, _triggerPrice < market price_
  * For spot, it is the TP/SL and Conditional order trigger price

  
[triggerBy](/docs/v5/enum#triggerby)| false| string| Trigger price type, Conditional order param for Perps & Futures. 

  * `LastPrice`
  * `IndexPrice`
  * `MarkPrice`

Valid for `linear` & `inverse`  
orderIv| false| string| Implied volatility. `option` **only**. Pass the real value, e.g for 10%, 0.1 should be passed. `orderIv` has a higher priority when `price` is passed as well  
[timeInForce](/docs/v5/enum#timeinforce)| false| string| [Time in force](https://www.bybit.com/en/help-center/article/What-Are-Time-In-Force-TIF-GTC-IOC-FOK)

  * Market order will always use `IOC`
  * If not passed, `GTC` is used by default

  
[positionIdx](/docs/v5/enum#positionidx)| false| integer| Used to identify positions in different position modes. Under hedge-mode, this param is **required**

  * `0`: one-way mode
  * `1`: hedge-mode Buy side
  * `2`: hedge-mode Sell side

  
orderLinkId| false| string| User customised order ID. A max of 36 characters. Combinations of numbers, letters (upper and lower cases), dashes, and underscores are supported.  
_Futures, Perps & Spot: orderLinkId rules:_

  * optional param
  * always unique

 _Options orderLinkId rules:_

  * **required** param
  * always unique

  
takeProfit| false| string| Take profit price

  * Spot Limit order supports take profit, stop loss or limit take profit, limit stop loss when creating an order
  * Option order supports full size market take profit

  
stopLoss| false| string| Stop loss price 

  * Spot Limit order supports take profit, stop loss or limit take profit, limit stop loss when creating an order
  * Option order supports full size market stop loss

  
[tpTriggerBy](/docs/v5/enum#triggerby)| false| string| The price type to trigger take profit. `MarkPrice`, `IndexPrice`, default: `LastPrice`. Valid for `linear` & `inverse`  
[slTriggerBy](/docs/v5/enum#triggerby)| false| string| The price type to trigger stop loss. `MarkPrice`, `IndexPrice`, default: `LastPrice`. Valid for `linear` & `inverse`  
reduceOnly| false| boolean| [What is a reduce-only order?](https://www.bybit.com/en/help-center/article/Reduce-Only-Order) `true` means your position can only reduce in size if this order is triggered. 

  * You **must** specify it as `true` when you are about to close/reduce the position
  * When reduceOnly is true, take profit/stop loss cannot be set

Valid for `linear`, `inverse` & `option`  
closeOnTrigger| false| boolean| [What is a close on trigger order?](https://www.bybit.com/en/help-center/article/Close-On-Trigger-Order) For a closing order. It can only reduce your position, not increase it. If the account has insufficient available balance when the closing order is triggered, then other active orders of similar contracts will be cancelled or reduced. It can be used to ensure your stop loss reduces your position regardless of current available margin.  
Valid for `linear` & `inverse`  
[smpType](/docs/v5/enum#smptype)| false| string| Smp execution type. [What is SMP?](/docs/v5/smp)  
mmp| false| boolean| Market maker protection. `option` **only**. `true` means set the order as a market maker protection order. [What is mmp?](/docs/v5/account/set-mmp)  
tpslMode| false| string| TP/SL mode 

  * `Full`: entire position for TP/SL. Then, tpOrderType or slOrderType must be `Market`
  * `Partial`: partial position tp/sl (as there is no size option, so it will create tp/sl orders with the qty you actually fill). Limit TP/SL order are supported. Note: When create limit tp/sl, tpslMode is **required** and it must be `Partial`

Valid for `linear` & `inverse`  
tpLimitPrice| false| string| The limit order price when take profit price is triggered 

  * `linear` & `inverse`: only works when tpslMode=Partial and tpOrderType=Limit
  * Spot: it is required when the order has `takeProfit` and "tpOrderType"=`Limit`

  
slLimitPrice| false| string| The limit order price when stop loss price is triggered

  * `linear` & `inverse`: only works when tpslMode=Partial and slOrderType=Limit
  * Spot: it is required when the order has `stopLoss` and "slOrderType"=`Limit`

  
tpOrderType| false| string| The order type when take profit is triggered 

  * `linear` & `inverse`: `Market`(default), `Limit`. For tpslMode=Full, it only supports tpOrderType=Market
  * Spot:   
`Market`: when you set "takeProfit",   
`Limit`: when you set "takeProfit" and "tpLimitPrice" 

  
slOrderType| false| string| The order type when stop loss is triggered 

  * `linear` & `inverse`: `Market`(default), `Limit`. For tpslMode=Full, it only supports slOrderType=Market
  * Spot:   
`Market`: when you set "stopLoss",   
`Limit`: when you set "stopLoss" and "slLimitPrice" 

  
bboSideType| false| string| 

  * `Queue`: use the order price on the orderbook in the same direction as the `side`
  * `Counterparty`: use the order price on the orderbook in the opposite direction as the `side`

Valid for `linear` & `inverse`  
bboLevel| false| string| `1`,`2`,`3`,`4`,`5` Valid for `linear` & `inverse`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Order ID  
orderLinkId| string| User customised order ID  
  
info

The acknowledgement of an place order request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

[](/docs/api-explorer/v5/trade/create-order)

* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    // Spot Limit order with market tp sl  
    {"category": "spot","symbol": "BTCUSDT","side": "Buy","orderType": "Limit","qty": "0.01","price": "28000","timeInForce": "PostOnly","takeProfit": "35000","stopLoss": "27000","tpOrderType": "Market","slOrderType": "Market"}  
      
    // Spot Limit order with limit tp sl  
    {"category": "spot","symbol": "BTCUSDT","side": "Buy","orderType": "Limit","qty": "0.01","price": "28000","timeInForce": "PostOnly","takeProfit": "35000","stopLoss": "27000","tpLimitPrice": "36000","slLimitPrice": "27500","tpOrderType": "Limit","slOrderType": "Limit"}  
      
    // Spot PostOnly normal order  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","timeInForce":"PostOnly","orderLinkId":"spot-test-01","isLeverage":0,"orderFilter":"Order"}  
      
    // Spot TP/SL order  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","triggerPrice": "15000", "timeInForce":"Limit","orderLinkId":"spot-test-02","isLeverage":0,"orderFilter":"tpslOrder"}  
      
    // Spot margin normal order (UTA)  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","timeInForce":"GTC","orderLinkId":"spot-test-limit","isLeverage":1,"orderFilter":"Order"}  
      
    // Spot Market Buy order, qty is quote currency  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"200","timeInForce":"IOC","orderLinkId":"spot-test-04","isLeverage":0,"orderFilter":"Order"}  
      
      
    // USDT Perp open long position (one-way mode)  
    {"category":"linear","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"1","price":"25000","timeInForce":"GTC","positionIdx":0,"orderLinkId":"usdt-test-01","reduceOnly":false,"takeProfit":"28000","stopLoss":"20000","tpslMode":"Partial","tpOrderType":"Limit","slOrderType":"Limit","tpLimitPrice":"27500","slLimitPrice":"20500"}  
      
    // USDT Perp close long position (one-way mode)  
    {"category": "linear", "symbol": "BTCUSDT", "side": "Sell", "orderType": "Limit", "qty": "1", "price": "30000", "timeInForce": "GTC", "positionIdx": 0, "orderLinkId": "usdt-test-02", "reduceOnly": true}  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.place_order(  
        category="spot",  
        symbol="BTCUSDT",  
        side="Buy",  
        orderType="Limit",  
        qty="0.1",  
        price="15600",  
        timeInForce="PostOnly",  
        orderLinkId="spot-test-postonly",  
        isLeverage=0,  
        orderFilter="Order",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "https://github.com/bybit-exchange/bybit.go.api")  
    client := bybit.NewBybitHttpClient("YOUR_API_KEY", "YOUR_API_SECRET", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{  
            "category":    "linear",  
            "symbol":      "BTCUSDT",  
            "side":        "Buy",  
            "positionIdx": 0,  
            "orderType":   "Limit",  
            "qty":         "0.001",  
            "price":       "10000",  
            "timeInForce": "GTC",  
        }  
    client.NewUtaBybitServiceWithParams(params).PlaceOrder(context.Background())  
    
    
    
    import com.bybit.api.client.restApi.BybitApiAsyncTradeRestClient;  
    import com.bybit.api.client.domain.ProductType;  
    import com.bybit.api.client.domain.TradeOrderType;  
    import com.bybit.api.client.domain.trade.PositionIdx;  
    import com.bybit.api.client.domain.trade.Side;  
    import com.bybit.api.client.domain.trade.TimeInForce;  
    import com.bybit.api.client.domain.trade.TradeOrderRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    import java.util.Map;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    Map<String, Object> order =Map.of(  
                      "category", "option",  
                      "symbol", "BTC-29DEC23-10000-P",  
                      "side", "Buy",  
                      "orderType", "Limit",  
                      "orderIv", "0.1",  
                      "qty", "0.1",  
                      "price", "5",  
                      "orderLinkId", "test_orderLinkId_1"  
                    );  
    client.createOrder(order, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    BybitTradeService tradeService = new(apiKey: "xxxxxxxxxxxxxx", apiSecret: "xxxxxxxxxxxxxxxxxxxxx");  
    var orderInfo = await tradeService.PlaceOrder(category: Category.LINEAR, symbol: "BLZUSDT", side: Side.BUY, orderType: OrderType.MARKET, qty: "15", timeInForce: TimeInForce.GTC);  
    Console.WriteLine(orderInfo);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    // Submit a market order  
    client  
      .submitOrder({  
        category: 'spot',  
        symbol: 'BTCUSDT',  
        side: 'Buy',  
        orderType: 'Market',  
        qty: '1',  
      })  
      .then((response) => {  
        console.log('Market order result', response);  
      })  
      .catch((error) => {  
        console.error('Market order error', error);  
      });  
      
    // Submit a limit order  
    client  
      .submitOrder({  
        category: 'spot',  
        symbol: 'BTCUSDT',  
        side: 'Buy',  
        orderType: 'Limit',  
        qty: '1',  
        price: '55000',  
      })  
      .then((response) => {  
        console.log('Limit order result', response);  
      })  
      .catch((error) => {  
        console.error('Limit order error', error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "orderId": "1321003749386327552",  
            "orderLinkId": "spot-test-postonly"  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }

---

# 創建委託單

本接口提供幣幣交易，現貨槓桿交易，合約以及期權的訂單創建

信息

  * **支持的訂單類型 (`orderType`):**  
限價單: `orderType`=_Limit_ , 需要指定訂單數量和價格.  


[市價單](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001135): `orderType`=_Market_ , 以Bybit市場內最優的價格一直執行到成交. 選擇市價單時，price 參數為空。在交易系統中，為了保護市價單產生嚴重的滑點，Bybit 交易系統會將市價單轉為限價單進行撮合，如果市場價格轉限價時，超過滑點設置的閾值，該筆市場價格訂單將會被取消。滑點閾值是指訂單價格偏離最新成交價格的百分比，目前閾值設置為：BTC 合約3%，其他合約5%。
  * **支持的timeInForce策略:**  
`GTC` 一直有效至取消  
`IOC` 立即成交或取消  
`FOK` 完全成交或取消  
`PostOnly`: 被動委托類型，如果該訂單在提交時會被立即執行成交，它將被**取消**. 這樣做的目的是為了保護您的訂單在提交的過程中，如果因為場內的價格變化，而撮合系統無法委託該筆訂單到訂單簿，因此會被取消。針對 PostOnly 訂單類型，單筆訂單可提交的數量比其他類型的訂單更多，請參考該[接口](/docs/zh-TW/v5/market/instrument)中的`lotSizeFilter > postOnlyMaxOrderQty`參數.  
`RPI`: 提升零售訂單價格流動訂單; 指定做市商允許下此類訂單; 本身具有post only屬性, 但是此訂單僅和來自網頁或者APP端的訂單成交

  * **如何創建條件單:**  
在提交訂單時，如果設置了**triggerPrice** ，則該訂單會自動轉為條件單。另外條件單不佔用保證金，如果條件單觸發後，保證金不足，則該筆訂單會被取消。

  * **[止盈 / 止損](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001138)** : 您可以在下單時設置止盈止損。另外，您可以通過[設置止盈止損](/docs/zh-TW/v5/position/trading-stop)接口修改持倉時的止盈止損價格。

  * **訂單數量** : 訂單數量，只支持正數。

  * **訂單價格** : 下限價單，價格字段**必傳** 。若您有倉位, 下單價格需要高於強平價. 對於設置價格的步長，請參閱該[接口](/docs/zh-TW/v5/market/instrument)中的`priceFilter` > `tickSize`.

  * **用戶自定義訂單Id** : 最大長度不超過36個字符且唯一。您可以自定義設置的订单ID(`orderLinkId`)，我们会为您关联到Bybit系统的唯一订单ID，并把唯一订单ID在活动委托创建成功后一并返回给您（包括Websocket），您可以使用 Bybit 的订单ID 和 orderLinkId 去獲取和取消訂單，如果在參數輸入中同時輸入 orderId 和 orderLinkId，Bybit 會優先以 orderId 為准來處理對應訂單.

  * **訂單持有上限:**  
**期貨:** 單個账户针对合约可持有每个 symbol 最多可同时持有500个普通活动订单。針對**條件單** ，單個帳戶針對合約可持有每個 symbol 最多同時持有 **10** 個條件單  
**現貨:** 單帳戶單交易對: 總計支持500個掛單，包括最多持有30個止盈止損委託單和30個條件單委託單  
**期權:** 單帳戶單幣種維度默認最多可持有50個委託單

  * **API限頻:**  
請參見[接口頻率限制表](/docs/zh-TW/v5/rate-limit#%E4%BA%A4%E6%98%93)，如需要提高請求頻率，請聯繫您對應的客戶經理或通過點擊[這裡](https://www.bybit.com/en/institutional)提交

  * **風控限制提示:**  
Bybit 將針對您的 API 請求進行統計監控，當單日 (UTC 0点 - UTC 24点) 單帳號（母帳號和子帳號整體運算）訂單總数超過一定上限，平台將保留提醒、警告，以及進行必要性限制的權利。 使用API的客戶預設接受本條款並負有配合調整的義務。

  * **只減倉訂單:**  
如果 reduceOnly=true 且訂單數量 > 最大訂單數量，則系統會自動拆分為多個訂單




### HTTP請求

POST`/v5/order/create`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
category| **true**|  string| 產品類型 `spot`, `linear`, `inverse`, `option`  
symbol| **true**|  string| 合約名稱  
isLeverage| false| integer| 是否走現貨槓桿下單. `0`(default): 否，則是幣幣訂單, `1`: 是，則是槓桿訂單  
side| **true**|  string| `Buy`, `Sell`  
[orderType](/docs/zh-TW/v5/enum#ordertype)| **true**|  string| 訂單類型. `Market`, `Limit`  
qty| **true**|  string| 訂單數量 

  * 現貨: 可以通過設置`marketUnit`來表示市價單qty的單位, 市價買單默認是`quoteCoin`, 市價賣單默認是`baseCoin`
  * 期貨和期權: 總是以base coin作為qty的單位
  * 期貨: 如果傳入`qty`="0"以及`reduceOnly`="true", 則可以平掉對應合約可達單個訂單允許的最大qty的倉位, 參照[查詢可交易產品的規格信息](/docs/zh-TW/v5/market/instrument)接口裡的字段`maxMktOrderQty`或者`maxOrderQty`

  
marketUnit| false| string| **現貨交易** 創建市價單時給入參`qty`指定的單位, 支持orderFilter=Order, tpslOrder 和 StopOrder

  * `baseCoin`: 比如, 買BTCUSDT, 則"qty"的單位是BTC
  * `quoteCoin`: 比如, 賣BTCUSDT, 則"qty"的單位是USDT

  
rpiTakerAccess| false| boolean| `true`: 您的訂單可以和RPI報價撮合, `false`: 不能和RPI報價撮合. 請先仔細閱讀[RPI Taker](https://announcements.bybit.com/en/article/rpi-liquidity-now-available-to-api-taker-orders-bltb943887bfa4c4d17/)的特性  
slippageToleranceType| false| string| 市價單滑點容差類型, `TickSize`, `Percent`

  * 不支持止盈止損、條件單
  * **TickSize** :   
限制買單最高價格 = ask1 + `slippageTolerance` x tickSize;   
限制賣單最低價格 = bid1 - `slippageTolerance` x tickSize
  * **Percent** :   
限制買單最高價格 = ask1 x (1 + `slippageTolerance` x 0.01);   
限制賣單最低價格 = bid1 x (1 - `slippageTolerance` x 0.01)

  
slippageTolerance| false| string| 滑點容差數值 

  * `TickSize`: 範圍是[1, 10000], 僅整數
  * `Percent`: 範圍是[0.01, 10], 最多2位小數

  
price| false| string| 訂單價格. 

  * 市價單將會忽視該字段
  * 請通過該[接口](/docs/zh-TW/v5/market/instrument#response-parameters)確認最低價格和精度要求
  * 如果有持倉, 確保價格優於強平價格

  
triggerDirection| false| integer| 條件單參數. 用於辨別期望的方向. 

  * `1`: 當市場價上漲到了`triggerPrice`時觸發條件單
  * `2`: 當市場價下跌到了`triggerPrice`時觸發條件單

對`linear`和`inverse`有效  
orderFilter| false| string| 指定訂單品種. `Order`: 普通單,`tpslOrder`: 止盈止損單,`StopOrder`: 條件單. 若不傳, 默認`Order`  
僅對現貨有效  
triggerPrice| false| string| 

  * 對於期貨, 是條件單觸發價格參數. 若您希望市場價是要上升後觸發, 確保:  
_triggerPrice > 市場價格_  
否則, _triggerPrice < 市場價格_
  * 對於現貨, 這是下止盈止損單或者條件單的觸發價格參數

  
[triggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 條件單參數. 觸發價格類型. `LastPrice`, `IndexPrice`, `MarkPrice`  
僅對`linear`和`inverse`有效  
orderIv| false| string| 隱含波動率. 僅`option`有效. 按照實際值傳入, e.g., 對於10%, 則傳入0.1. `orderIv`比`price`有更高的優先級  
[timeInForce](/docs/zh-TW/v5/enum#timeinforce)| false| string| [訂單執行策略](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001044)

  * 市價單，系統直接使用`IOC`
  * 若不傳，默認使用`GTC`

  
[positionIdx](/docs/zh-TW/v5/enum#positionidx)| false| integer| 倉位標識, 用戶不同倉位模式. 該字段對於雙向持倉模式是**必傳** :

  * `0`: 單向持倉
  * `1`: 買側雙向持倉
  * `2`: 賣側雙向持倉

  
orderLinkId| false| string| 用戶自定義訂單Id 

  * category=`option`時，該參數必傳

  
takeProfit| false| string| 止盈價格 

  * 支持期貨、現貨和期權

  
stopLoss| false| string| 止損價格 

  * 支持期貨、現貨和期權

  
[tpTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 觸發止盈的價格類型 

  * `MarkPrice`
  * `IndexPrice`
  * `LastPrice`(默認)

  
僅對`linear`和`inverse`有效  
[slTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 觸發止損的價格類型 

  * `MarkPrice`
  * `IndexPrice`
  * `LastPrice`(默認)

  
僅對`linear`和`inverse`有效  
reduceOnly| false| boolean| [什麼是只減倉?](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001047) `true` 將這筆訂單設為只減倉 

  * 當減倉時, reduceOnly=true**必傳**
  * 只減倉單的止盈止損不生效

對`linear`, `inverse`和`option`有效  
closeOnTrigger| false| boolean| [什麼是觸發後平倉委託?](https://www.bybit.com/zh-TW/help-center/bybitHC_Article?language=zh_TW&id=000001050)此選項可以確保您的止損單被用於減倉（平倉）而非加倉，並且在可用保證金不足的情況下，取消其他委託，騰出保證金以確保平倉委託的執行.  
僅對`linear`和`inverse`有效  
[smpType](/docs/zh-TW/v5/enum#smptype)| false| string| Smp執行類型. [什麼是SMP?](/docs/zh-TW/v5/smp)  
mmp| false| boolean| 做市商保護, `true` 表示該訂單是做市商保護訂單. [什麼是做市商保護?](/docs/zh-TW/v5/account/set-mmp)

  * 僅`option`有效

  
tpslMode| false| string| 止盈止損模式 

  * `Full`: 全部倉位止盈止損. 此時, tpOrderType或者slOrderType必須傳`Market`
  * `Partial`: 部分倉位止盈止損(下單時沒有size選項, 實際上創建tpsl訂單時, 是按照實際成交的數量來生成止盈止損). 支持創建限價止盈止損. 注意: 創建限價止盈止損時, tpslMode**必傳** 且為Partial

僅對`linear`和`inverse`有效  
tpLimitPrice| false| string| 觸發止盈後轉換為限價單的價格 

  * `linear` & `inverse`: 僅作用於當tpslMode=Partial以及tpOrderType=Limit時
  * 現貨: 參數必傳當創建訂單時帶了`takeProfit` 和 `tpOrderType=Limit`

  
slLimitPrice| false| string| 觸發止損後轉換為限價單的價格 

  * `linear` & `inverse`: 僅作用於當tpslMode=Partial以及slOrderType=Limit時
  * 現貨: 參數必傳當創建訂單時帶了`stopLoss` 和 `slOrderType=Limit`

  
tpOrderType| false| string| 止盈觸發後的訂單類型 

category="linear"或"inverse": `Market`(默認), `Limit`  
對於tpslMode=Full, 僅支持tpOrderType=Market
    * 現貨:   
`Market`: 當帶了參數"takeProfit",   
`Limit`: 當帶了參數"takeProfit" 和 "tpLimitPrice" 

  
slOrderType| false| string| 止損觸發後的訂單類型 

  * category="linear"或"inverse": `Market`(默認), `Limit`  
對於tpslMode=Full, 僅支持slOrderType=Market
  * 現貨:   
`Market`: 當帶了參數"stopLoss",   
`Limit`: 當帶了參數"stopLoss" 和 "slLimitPrice" 

  
bboSideType| false| string| 

  * `Queue`: 用orderbook 上與`side`同向的order price掛單 
  * `Counterparty`: 用orderbook 上與`side`異向的order price掛單 

對`linear`和`inverse`有效  
bboLevel| false| string| `1`,`2`,`3`,`4`,`5` 對`linear`和`inverse`有效  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 訂單ID  
orderLinkId| string| 用戶自定義訂單ID  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

[](/docs/zh-TW/api-explorer/v5/trade/create-order)

* * *

### 請求示例

  * HTTP
  * Python
  * Go
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/create HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672211928338  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    // 現貨下僅maker單  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","timeInForce":"PostOnly","orderLinkId":"spot-test-01","isLeverage":0,"orderFilter":"Order"}  
      
    // 槓桿交易單  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"0.1","price":"15600","timeInForce":"GTC","orderLinkId":"spot-test-limit","isLeverage":1,"orderFilter":"Order"}  
      
    // 現貨市價單, qty為報價幣種金額  
    {"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"200","timeInForce":"IOC","orderLinkId":"spot-test-04","isLeverage":0,"orderFilter":"Order"}  
      
    // USDT永續開多倉訂單 (單向持倉)  
    {"category":"linear","symbol":"BTCUSDT","side":"Buy","orderType":"Limit","qty":"1","price":"25000","timeInForce":"GTC","positionIdx":0,"orderLinkId":"usdt-test-01","reduceOnly":false,"takeProfit":"28000","stopLoss":"20000","tpslMode":"Partial","tpOrderType":"Limit","slOrderType":"Limit","tpLimitPrice":"27500","slLimitPrice":"20500"}  
      
    // USDT永續平多倉訂單 (單向持倉)  
    {"category": "linear", "symbol": "BTCUSDT", "side": "Sell", "orderType": "Limit", "qty": "1", "price": "30000", "timeInForce": "GTC", "positionIdx": 0, "orderLinkId": "usdt-test-02", "reduceOnly": true}  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.place_order(  
        category="spot",  
        symbol="BTCUSDT",  
        side="Buy",  
        orderType="Limit",  
        qty="0.1",  
        price="15600",  
        timeInForce="PostOnly",  
        orderLinkId="spot-test-postonly",  
        isLeverage=0,  
        orderFilter="Order",  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "https://github.com/bybit-exchange/bybit.go.api")  
    client := bybit.NewBybitHttpClient("YOUR_API_KEY", "YOUR_API_SECRET", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{  
                "category":    "linear",  
                "symbol":      "BTCUSDT",  
                "side":        "Buy",  
                "positionIdx": 0,  
                "orderType":   "Limit",  
                "qty":         "0.001",  
                "price":       "10000",  
                "timeInForce": "GTC",  
            }  
    client.NewUtaBybitServiceWithParams(params).PlaceOrder(context.Background())  
    
    
    
    import com.bybit.api.client.restApi.BybitApiAsyncTradeRestClient;  
    import com.bybit.api.client.domain.ProductType;  
    import com.bybit.api.client.domain.TradeOrderType;  
    import com.bybit.api.client.domain.trade.PositionIdx;  
    import com.bybit.api.client.domain.trade.Side;  
    import com.bybit.api.client.domain.trade.TimeInForce;  
    import com.bybit.api.client.domain.trade.TradeOrderRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    import java.util.Map;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var newOrderRequest = TradeOrderRequest.builder().category(ProductType.LINEAR).symbol("XRPUSDT")  
                    .side(Side.BUY).orderType(TradeOrderType.MARKET).qty("10").timeInForce(TimeInForce.IMMEDIATE_OR_CANCEL)  
                    .positionIdx(PositionIdx.ONE_WAY_MODE).build();  
    client.createOrder(newOrderRequest, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    BybitTradeService tradeService = new(apiKey: "xxxxxxxxxxxxxx", apiSecret: "xxxxxxxxxxxxxxxxxxxxx");  
    var orderInfo = await tradeService.PlaceOrder(category: Category.LINEAR, symbol: "BLZUSDT", side: Side.BUY, orderType: OrderType.MARKET, qty: "15", timeInForce: TimeInForce.GTC);  
    Console.WriteLine(orderInfo);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .submitOrder({  
            category: 'spot',  
            symbol: 'BTCUSDT',  
            side: 'Buy',  
            orderType: 'Market',  
            qty: '0.1',  
            price: '15600',  
            timeInForce: 'PostOnly',  
            orderLinkId: 'spot-test-postonly',  
            isLeverage: 0,  
            orderFilter: 'Order',  
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
            "orderId": "1321003749386327552",  
            "orderLinkId": "spot-test-postonly"  
        },  
        "retExtInfo": {},  
        "time": 1672211918471  
    }