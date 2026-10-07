---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/max-loan-amt
api_type: REST
updated_at: 2026-10-07 18:53:29.115312
---

# Amend Order

info

You can only modify **unfilled** or **partially filled** orders.

### HTTP Request

POST`/v5/order/amend`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `inverse`, `spot`, `option`  
symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
orderId| false| string| Order ID. Either `orderId` or `orderLinkId` is required  
orderLinkId| false| string| User customised order ID. Either `orderId` or `orderLinkId` is required  
orderIv| false| string| Implied volatility. `option` **only**. Pass the real value, e.g for 10%, 0.1 should be passed  
triggerPrice| false| string| 

  * For Perps & Futures, it is the conditional order trigger price. If you expect the price to rise to trigger your conditional order, make sure:  
_triggerPrice > market price_  
Else, _triggerPrice < market price_
  * For spot, it is the TP/SL and Conditional order trigger price

  
qty| false| string| Order quantity after modification. Do not pass it if not modify the qty  
price| false| string| Order price after modification. Do not pass it if not modify the price  
tpslMode| false| string| TP/SL mode 

  * `Full`: entire position for TP/SL. Then, tpOrderType or slOrderType must be `Market`
  * `Partial`: partial position tp/sl. Limit TP/SL order are supported. Note: When create limit tp/sl, tpslMode is **required** and it must be `Partial`

Valid for `linear` & `inverse`  
takeProfit| false| string| Take profit price after modification. If pass "0", it means cancel the existing take profit of the order. Do not pass it if you do not want to modify the take profit  
stopLoss| false| string| Stop loss price after modification. If pass "0", it means cancel the existing stop loss of the order. Do not pass it if you do not want to modify the stop loss  
[tpTriggerBy](/docs/v5/enum#triggerby)| false| string| The price type to trigger take profit. When set a take profit, this param is **required** if no initial value for the order  
[slTriggerBy](/docs/v5/enum#triggerby)| false| string| The price type to trigger stop loss. When set a take profit, this param is **required** if no initial value for the order  
[triggerBy](/docs/v5/enum#triggerby)| false| string| Trigger price type  
tpLimitPrice| false| string| Limit order price when take profit is triggered. Only working when original order sets partial limit tp/sl. _Option not supported_  
slLimitPrice| false| string| Limit order price when stop loss is triggered. Only working when original order sets partial limit tp/sl. _Option not supported`_  
  
info

The acknowledgement of an amend order request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

[](/docs/api-explorer/v5/trade/amend-order)

* * *

### Response Parameters

Parameter| Type| Comments  
---|---|---  
orderId| string| Order ID  
orderLinkId| string| User customised order ID  
  
### Request Example

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/amend HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672217108106  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "linear",  
        "symbol": "ETHPERP",  
        "orderLinkId": "linear-004",  
        "triggerPrice": "1145",  
        "qty": "0.15",  
        "price": "1050",  
        "takeProfit": "0",  
        "stopLoss": "0"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.amend_order(  
        category="linear",  
        symbol="ETHPERP",  
        orderLinkId="linear-004",  
        triggerPrice="1145",  
        qty="0.15",  
        price="1050",  
        takeProfit="0",  
        stopLoss="0",  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiTradeRestClient;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var amendOrderRequest = TradeOrderRequest.builder().orderId("1523347543495541248").category(ProductType.LINEAR).symbol("XRPUSDT")  
                            .price("0.5")  // setting a new price, for example  
                            .qty("15")  // and a new quantity  
                            .build();  
    var amendedOrder = client.amendOrder(amendOrderRequest);  
    System.out.println(amendedOrder);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    BybitTradeService tradeService = new(apiKey: "xxxxxxxxxxxxxx", apiSecret: "xxxxxxxxxxxxxxxxxxxxx");  
    var orderInfoString = await TradeService.AmendOrder(orderId: "1523347543495541248", category:Category.LINEAR, symbol: "XRPUSDT", price:"0.5", qty:"15");  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .amendOrder({  
            category: 'linear',  
            symbol: 'ETHPERP',  
            orderLinkId: 'linear-004',  
            triggerPrice: '1145',  
            qty: '0.15',  
            price: '1050',  
            takeProfit: '0',  
            stopLoss: '0',  
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
        "time": 1672217093461  
    }

---

# 修改委託單

important

您只能修改那些**未成交** 或者**部分成交** 的訂單。

### HTTP請求

POST`/v5/order/amend`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `inverse`, `spot`, `option`  
symbol| **true**|  string| 合約名稱  
orderId| false| string| 訂單Id. `orderId`和`orderLinkId`必傳其中一個  
orderLinkId| false| string| 用戶自定義訂單Id. `orderId`和`orderLinkId`必傳其中一個  
orderIv| false| string| 隱含波動率. 僅`option`有效. 按照實際值傳入, e.g., 對於10%, 則傳入0.1  
triggerPrice| false| string| 

  * 對於期貨, 是條件單觸發價格參數. 若您希望市場價是要上升後觸發, 確保:  
_triggerPrice > 市場價格_  
否則, _triggerPrice < 市場價格_
  * 對於現貨, 這是下止盈止損單或者條件單的觸發價格參數

  
qty| false| string| 修改後的訂單數量. 若不修改，請不要傳該字段  
price| false| string| 修改後的訂單價格. 若不修改，請不要傳該字段  
tpslMode| false| string| 止盈止損模式 

  * `Full`: 全部倉位止盈止損. 此時, tpOrderType或者slOrderType必須傳`Market`
  * `Partial`: 部分倉位止盈止損. 支持創建限價止盈止損. 注意: 創建限價止盈止損時, tpslMode**必傳** 且為Partial

僅對`linear`和`inverse`有效  
takeProfit| false| string| 修改後的止盈價格. 當傳"0"時, 表示取消當前訂單上設置的止盈. 若不修改，請不要傳該字段  
  
stopLoss| false| string| 修改後的止損價格. 當傳"0"時, 表示取消當前訂單上設置的止損. 若不修改，請不要傳該字段  
  
[tpTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 止盈價格觸發類型. 若下單時未設置該值，則調用該接口修改止盈價格時，該字段**必傳**  
[slTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 止損價格觸發類型. 若下單時未設置該值，則調用該接口修改止損價格時，該字段**必傳**  
[triggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 觸發價格的觸發類型  
tpLimitPrice| false| string| 觸發止盈後轉換為限價單的價格  
當且僅當原始訂單下單時創建的是部分止盈止損限價單, 本字段才有效  
  
slLimitPrice| false| string| 觸發止損後轉換為限價單的價格  
當且僅當原始訂單下單時創建的是部分止盈止損限價單, 本字段才有效  
  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

[](/docs/zh-TW/api-explorer/v5/trade/amend-order)

* * *

### 響應參數

參數| 類型| 說明  
---|---|---  
orderId| string| 訂單Id  
orderLinkId| string| 用戶自定義訂單Id  
  
### 請求示例

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/amend HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672217108106  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "linear",  
        "symbol": "ETHPERP",  
        "orderLinkId": "linear-004",  
        "triggerPrice": "1145",  
        "qty": "0.15",  
        "price": "1050",  
        "takeProfit": "0",  
        "stopLoss": "0"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.amend_order(  
        category="linear",  
        symbol="ETHPERP",  
        orderLinkId="linear-004",  
        triggerPrice="1145",  
        qty="0.15",  
        price="1050",  
        takeProfit="0",  
        stopLoss="0",  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiTradeRestClient;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var amendOrderRequest = TradeOrderRequest.builder().orderId("1523347543495541248").category(ProductType.LINEAR).symbol("XRPUSDT")  
                            .price("0.5")  // setting a new price, for example  
                            .qty("15")  // and a new quantity  
                            .build();  
    var amendedOrder = client.amendOrder(amendOrderRequest);  
    System.out.println(amendedOrder);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    BybitTradeService tradeService = new(apiKey: "xxxxxxxxxxxxxx", apiSecret: "xxxxxxxxxxxxxxxxxxxxx");  
    var orderInfoString = await TradeService.AmendOrder(orderId: "1523347543495541248", category:Category.LINEAR, symbol: "XRPUSDT", price:"0.5", qty:"15");  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .amendOrder({  
            category: 'linear',  
            symbol: 'ETHPERP',  
            orderLinkId: 'linear-004',  
            triggerPrice: '1145',  
            qty: '0.15',  
            price: '1050',  
            takeProfit: '0',  
            stopLoss: '0',  
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
        "time": 1672217093461  
    }