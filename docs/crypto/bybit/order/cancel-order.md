---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/cancel-order
api_type: Trading
updated_at: 2026-05-27 19:20:45.749704
---

# Cancel Order

important

  * You must specify `orderId` or `orderLinkId` to cancel the order.
  * If `orderId` and `orderLinkId` do not match, the system will process `orderId` first.
  * You can only cancel **unfilled** or **partially filled** orders.



### HTTP Request

POST`/v5/order/cancel`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `linear`, `inverse`, `spot`, `option`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
orderId| false| string| Order ID. Either `orderId` or `orderLinkId` is **required**  
orderLinkId| false| string| User customised order ID. Either `orderId` or `orderLinkId` is **required**  
orderFilter| false| string| Spot trading **only**

  * `Order`
  * `tpslOrder`
  * `StopOrder`

If not passed, `Order` by default  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Order ID  
orderLinkId| string| User customised order ID  
  
info

The acknowledgement of an cancel order request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

[](/docs/api-explorer/v5/trade/cancel-order)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672217376681  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
      "category": "linear",  
      "symbol": "BTCPERP",  
      "orderLinkId": null,  
      "orderId":"c6f055d9-7f21-4079-913d-e6523a9cfffa"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_order(  
        category="linear",  
        symbol="BTCPERP",  
        orderId="c6f055d9-7f21-4079-913d-e6523a9cfffa",  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiTradeRestClient;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var cancelOrderRequest = TradeOrderRequest.builder().category(ProductType.SPOT).symbol("XRPUSDT").orderId("1523347543495541248").build();  
    var canceledOrder = client.cancelOrder(cancelOrderRequest);  
    System.out.println(canceledOrder);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    BybitTradeService tradeService = new(apiKey: "xxxxxxxxxxxxxx", apiSecret: "xxxxxxxxxxxxxxxxxxxxx");  
    var orderInfoString = await TradeService.CancelOrder(orderId: "1523347543495541248", category: Category.SPOT, symbol: "XRPUSDT");  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .cancelOrder({  
            category: 'linear',  
            symbol: 'BTCPERP',  
            orderId: 'c6f055d9-7f21-4079-913d-e6523a9cfffa',  
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
            "orderId": "c6f055d9-7f21-4079-913d-e6523a9cfffa",  
            "orderLinkId": "linear-004"  
        },  
        "retExtInfo": {},  
        "time": 1672217377164  
    }

---

# 撤銷委託單

重要

  * 您必須指定`orderId`或者`orderLinkId`.
  * 若`orderId`和`orderLinkId`之間不匹配, 系統將會優先處理`orderId`.
  * 您只能撤銷未成交和部分成交的訂單.



### HTTP請求

POST`/v5/order/cancel`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `spot`, `linear`, `inverse`, `option`  
symbol| **true**|  string| 合約名稱  
orderId| false| string| 訂單Id. `orderId`和`orderLinkId`**必傳** 其中一個  
orderLinkId| false| string| 用戶自定義訂單Id. `orderId`和`orderLinkId`**必傳** 其中一個  
orderFilter| false| string| 僅現貨交易有效

  * `Order`: 普通單
  * `tpslOrder`: 止盈止損單
  * `StopOrder`: 條件單

若不傳, 默認是`Order`  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 訂單Id  
orderLinkId| string| 用戶自定義訂單Id  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

[](/docs/zh-TW/api-explorer/v5/trade/cancel-order)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/cancel HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672217376681  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
      "category": "linear",  
      "symbol": "BTCPERP",  
      "orderLinkId": null,  
      "orderId":"c6f055d9-7f21-4079-913d-e6523a9cfffa"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_order(  
        category="linear",  
        symbol="BTCPERP",  
        orderId="c6f055d9-7f21-4079-913d-e6523a9cfffa",  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiTradeRestClient;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var cancelOrderRequest = TradeOrderRequest.builder().category(ProductType.SPOT).symbol("XRPUSDT").orderId("1523347543495541248").build();  
    var canceledOrder = client.cancelOrder(cancelOrderRequest);  
    System.out.println(canceledOrder);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    BybitTradeService tradeService = new(apiKey: "xxxxxxxxxxxxxx", apiSecret: "xxxxxxxxxxxxxxxxxxxxx");  
    var orderInfoString = await TradeService.CancelOrder(orderId: "1523347543495541248", category: Category.SPOT, symbol: "XRPUSDT");  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .cancelOrder({  
            category: 'linear',  
            symbol: 'BTCPERP',  
            orderId: 'c6f055d9-7f21-4079-913d-e6523a9cfffa',  
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
            "orderId": "c6f055d9-7f21-4079-913d-e6523a9cfffa",  
            "orderLinkId": "linear-004"  
        },  
        "retExtInfo": {},  
        "time": 1672217377164  
    }