---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/batch-place
api_type: Trading
updated_at: 2026-08-05 19:06:00.778979
---

# Cancel All Orders

Cancel all open orders

info

  * Support cancel orders by `symbol`/`baseCoin`/`settleCoin`. If you pass multiple of these params, the system will process one of param, which priority is `symbol` > `baseCoin` > `settleCoin`.
  * **NOTE** : category=_option_ , you can cancel all option open orders without passing any of those three params. However, for "linear" and "inverse", you must specify one of those three params.
  * **NOTE** : category=_spot_ , you can cancel all spot open orders (normal order by default) without passing other params.



info

**Spot** : no limit  
**Futures** : cancel up to 500 orders (System **picks up 500 orders randomly to cancel** when you have over 500 orders)  
**Options** : no limit

### HTTP Request

POST`/v5/order/cancel-all`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `linear`, `inverse`, `spot`, `option`  
symbol| false| string| Symbol name, like `BTCUSDT`, uppercase only  
`linear`&`inverse`: **Required** if not passing baseCoin or settleCoin  
baseCoin| false| string| Base coin, uppercase only. `linear` & `inverse`: If cancel all by baseCoin, it will cancel all of the corresponding category's orders. **Required** if not passing symbol or settleCoin  
settleCoin| false| string| Settle coin, uppercase only 

  * `linear` & `inverse`: **Required** if not passing symbol or baseCoin
  * `option`: USDT or USDC
  * Not support `spot`

  
orderFilter| false| string| 

  * category=`spot`, you can pass `Order`, `tpslOrder`, `StopOrder`, `OcoOrder`, `BidirectionalTpslOrder`  
If not passed, `Order` by default
  * category=`linear` or `inverse`, you can pass `Order`, `StopOrder`,`OpenOrder`  
If not passed, all kinds of orders will be cancelled, like active order, conditional order, TP/SL order and trailing stop order
  * category=`option`, you can pass `Order`,`StopOrder`  
If not passed, all kinds of orders will be cancelled, like active order, conditional order, TP/SL order and trailing stop order

  
[stopOrderType](/docs/v5/enum#stopordertype)| false| string| Stop order type `Stop`

  * Only used for category=`linear` or `inverse` and orderFilter=`StopOrder`,you can cancel conditional orders except TP/SL order and Trailing stop orders with this param

  
  
info

The acknowledgement of create/amend/cancel order requests indicates that the request was sucessfully accepted. The request is asynchronous so please use the websocket to confirm the order status.

[](/docs/api-explorer/v5/trade/cancel-all)

* * *

### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> orderId| string| Order ID  
> orderLinkId| string| User customised order ID  
success| string| "1": success, "0": fail. [UTA1.0](/docs/v5/acct-mode#uta-10) (inverse) does not return this field  
  
### Request Example

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/cancel-all HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672219779140  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
      "category": "linear",  
      "symbol": null,  
      "settleCoin": "USDT"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_all_orders(  
        category="linear",  
        settleCoin="USDT",  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiTradeRestClient;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var cancelAllOrdersRequest = TradeOrderRequest.builder().category(ProductType.LINEAR).baseCoin("USDT").build();  
    client.cancelAllOrder(cancelAllOrdersRequest, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    BybitTradeService tradeService = new(apiKey: "xxxxxxxxxxxxxx", apiSecret: "xxxxxxxxxxxxxxxxxxxxx");  
    var orderInfoString = await TradeService.CancelAllOrder(category: Category.LINEAR, baseCoin:"USDT");  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .cancelAllOrders({  
        category: 'linear',  
        settleCoin: 'USDT',  
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
                    "orderId": "1616024329462743808",  
                    "orderLinkId": "1616024329462743809"  
                },  
                {  
                    "orderId": "1616024287544869632",  
                    "orderLinkId": "1616024287544869633"  
                }  
            ],  
            "success": "1"  
        },  
        "retExtInfo": {},  
        "time": 1707381118116  
    }

---

# 撤銷所有訂單

信息

  * 支持按照symbol/baseCoin/settleCoin撤銷訂單，若您傳入了多個參數組合, 系統僅會處理其中一個參數，其中優先級為`symbol` > `baseCoin` > `settleCoin`.
  * **注意** : 當`category`=_option_ , 您可以不傳人三個參數中的任何一個，就能取消所有期權的委託單。但是, 對於`linear`和`inverse`, 您必需指定三個參數的其中一個。
  * **注意** : 當`category`=_spot_ , 您可以不傳人任何參數，就能取消所有現貨的委託單 (默認普通單)。



信息

**現貨** : 無限制  
**期貨** : 最多取消500單 (當您訂單數量超過500單時, 系統會**隨機挑選500單** 進行取消)  
**期權** : 統無限制

### HTTP請求

POST`/v5/order/cancel-all`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `spot`, `linear`, `inverse`, `option`  
symbol| false| string| 合約名稱  
對於`linear` & `inverse`: 若不傳`baseCoin`和`settleCoin`, 該字段**必傳**  
baseCoin| false| string| 交易幣種 

  * `linear` & `inverse`: 當通過baseCoin來全部撤單時, 會將對應category的訂單全部撤掉。若不傳`symbol`和`baseCoin`, 則該字段**必傳**

  
settleCoin| false| string| 結算幣種 

  * 對於`linear` & `inverse`: 該字段**必傳** , 若不傳`symbol`和`baseCoin`
  * `option`: USDC或者USDT
  * 該字段不支持`spot`

  
orderFilter| false| string| 

  * category=`spot`, 該字段可以傳:   
`Order`(普通單), `tpslOrder`(止盈止損單)  
`StopOrder`(條件單), `OcoOrder`  
`BidirectionalTpslOrder`(現貨雙向止盈止損訂單)  
若不傳, 則默認是撤掉`Order`單
  * 當category=`linear` 或者 `inverse`, 該字段可以傳`Order`(普通單), `StopOrder`(條件單, 包括止盈止損單和追蹤出場單), `OpenOrder`(僅取消開倉單). 若不傳, 則所有類型的訂單都會被撤掉
  * 當category=`option`, 該字段可以傳`Order`,`StopOrder`, 若不傳, 則撤掉這兩種類型下所有訂單

  
[stopOrderType](/docs/zh-TW/v5/enum#stopordertype)| false| string| 條件單類型, `Stop`

  * 僅用於當category=`linear` 或者 `inverse`以及orderFilter=`StopOrder`時, 若想僅取消條件單 (不包括止盈止損單和追蹤出場單), 則可以傳入該字段

  
[](/docs/zh-TW/api-explorer/v5/trade/cancel-all)

* * *

### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> orderId| string| 訂單ID  
> orderLinkId| string| 用戶自定義的訂單ID  
success| string| "1": 成功, "0": 失敗  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

### 請求示例

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/cancel-all HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672219779140  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
      "category": "linear",  
      "symbol": null,  
      "settleCoin": "USDT"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_all_orders(  
        category="linear",  
        settleCoin="USDT",  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiTradeRestClient;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var cancelAllOrdersRequest = TradeOrderRequest.builder().category(ProductType.LINEAR).baseCoin("USDT").build();  
    client.cancelAllOrder(cancelAllOrdersRequest, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    BybitTradeService tradeService = new(apiKey: "xxxxxxxxxxxxxx", apiSecret: "xxxxxxxxxxxxxxxxxxxxx");  
    var orderInfoString = await TradeService.CancelAllOrder(category: Category.LINEAR, baseCoin:"USDT");  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .cancelAllOrders({  
        category: 'linear',  
        settleCoin: 'USDT',  
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
                    "orderId": "1616024329462743808",  
                    "orderLinkId": "1616024329462743809"  
                },  
                {  
                    "orderId": "1616024287544869632",  
                    "orderLinkId": "1616024287544869633"  
                }  
            ],  
            "success": "1"  
        },  
        "retExtInfo": {},  
        "time": 1707381118116  
    }