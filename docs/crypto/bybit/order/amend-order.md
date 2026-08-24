---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/amend-order
api_type: Trading
updated_at: 2026-08-24 18:45:34.654069
---

# Batch Cancel Order

This endpoint allows you to cancel more than one open order in a single request.

important

  * You must specify `orderId` or `orderLinkId`.
  * If `orderId` and `orderLinkId` is not matched, the system will process `orderId` first.
  * You can cancel **unfilled** or **partially filled** orders.
  * A maximum of 20 orders (option), 20 orders (inverse), 20 orders (linear), 10 orders (spot) can be cancelled per request.



### HTTP Request

POST`/v5/order/cancel-batch`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `option`, `spot`, `inverse`  
request| **true**|  array| Object  
> symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
> orderId| false| string| Order ID. Either `orderId` or `orderLinkId` is required  
> orderLinkId| false| string| User customised order ID. Either `orderId` or `orderLinkId` is required  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| Object|   
> list| array| Object  
>> category| string| Product type  
>> symbol| string| Symbol name  
>> orderId| string| Order ID  
>> orderLinkId| string| User customised order ID  
retExtInfo| Object|   
> list| array| Object  
>> code| number| Success/error code  
>> msg| string| Success/error message  
  
info

The acknowledgement of an cancel order request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

[](/docs/api-explorer/v5/trade/batch-cancel)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/cancel-batch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672223356634  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "spot",  
        "request": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": "1666800494330512128"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "orderLinkId": "1666800494330512129"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_batch_order(  
        category="spot",  
        request=[  
            {  
                "symbol": "BTCUSDT",  
                "orderId": "1666800494330512128"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "orderLinkId": "1666800494330512129"  
            }  
        ]  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiTradeRestClient;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var cancelOrderRequests = Arrays.asList(TradeOrderRequest.builder().symbol("BTC-10FEB23-24000-C").orderLinkId("9b381bb1-401").build(),  
                    TradeOrderRequest.builder().symbol("BTC-10FEB23-24000-C").orderLinkId("82ee86dd-001").build());  
    var cancelBatchOrders = BatchOrderRequest.builder().category(ProductType.OPTION).request(cancelOrderRequests).build();  
    client.createBatchOrder(cancelBatchOrders, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    var order1 = new OrderRequest { Symbol = "BTC-10FEB23-24000-C", OrderLinkId = "9b381bb1-401" };  
    var order2 = new OrderRequest { Symbol = "BTC-10FEB23-24000-C", OrderLinkId = "82ee86dd-001" };  
    var orderInfoString = await TradeService.CancelBatchOrder(category: Category.LINEAR, request: new List<OrderRequest> { order1, order2 });  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .batchCancelOrders('spot', [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": "1666800494330512128"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "orderLinkId": "1666800494330512129"  
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
                    "orderLinkId": "spot-btc-03"  
                },  
                {  
                    "category": "spot",  
                    "symbol": "ATOMUSDT",  
                    "orderId": "",  
                    "orderLinkId": "1666800494330512129"  
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
                    "code": 170213,  
                    "msg": "Order does not exist."  
                }  
            ]  
        },  
        "time": 1713434299047  
    }

---

# 批量撤銷委託單

該接口可以批量撤銷多筆訂單

重要

  * 您必須指定`orderId`或者`orderLinkId`.
  * 若`orderId`和`orderLinkId`之間不匹配, 系統將會優先處理`orderId`.
  * 您只能撤銷未成交和部分成交的訂單.
  * 最多支持單個請求中撤銷, 期權: 20個訂單, 反向合約: 20個訂單, 正向合約: 20个訂單, 現貨: 10個訂單.



### HTTP請求

POST`/v5/order/cancel-batch`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `option`, `spot`, `inverse`  
request| **true**|  array| Object  
> symbol| **true**|  string| 合約名稱  
> orderId| false| string| 訂單Id. `orderId`和`orderLinkId`必傳其中一個  
> orderLinkId| false| string| 用戶自定義訂單Id. `orderId`和`orderLinkId`必傳其中一個  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| Object|   
> list| array| Object  
>> category| string| 產品類型  
>> symbol| string| 合約名稱  
>> orderId| string| 訂單Id  
>> orderLinkId| string| 用戶自定義訂單Id  
retExtInfo| Object|   
> list| array| Object  
>> code| number| 成功/錯誤碼  
>> msg| string| 成功/錯誤信息  
  
信息

ack僅表示請求被成功接受. 請使用websocket-order推送來確認訂單狀態

[](/docs/zh-TW/api-explorer/v5/trade/batch-cancel)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/cancel-batch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672223356634  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "spot",  
        "request": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": "1666800494330512128"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "orderLinkId": "1666800494330512129"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.cancel_batch_order(  
        category="spot",  
        request=[  
            {  
                "symbol": "BTCUSDT",  
                "orderId": "1666800494330512128"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "orderLinkId": "1666800494330512129"  
            }  
        ]  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiTradeRestClient;  
    import com.bybit.api.client.domain.*;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var cancelOrderRequests = Arrays.asList(TradeOrderRequest.builder().symbol("BTC-10FEB23-24000-C").orderLinkId("9b381bb1-401").build(),  
                    TradeOrderRequest.builder().symbol("BTC-10FEB23-24000-C").orderLinkId("82ee86dd-001").build());  
    var cancelBatchOrders = BatchOrderRequest.builder().category(ProductType.OPTION).request(cancelOrderRequests).build();  
    client.createBatchOrder(cancelBatchOrders, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    var order1 = new OrderRequest { Symbol = "BTC-10FEB23-24000-C", OrderLinkId = "9b381bb1-401" };  
    var order2 = new OrderRequest { Symbol = "BTC-10FEB23-24000-C", OrderLinkId = "82ee86dd-001" };  
    var orderInfoString = await TradeService.CancelBatchOrder(category: Category.LINEAR, request: new List<OrderRequest> { order1, order2 });  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .batchCancelOrders('spot', [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": "1666800494330512128"  
            },  
            {  
                "symbol": "ATOMUSDT",  
                "orderLinkId": "1666800494330512129"  
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
                    "orderLinkId": "spot-btc-03"  
                },  
                {  
                    "category": "spot",  
                    "symbol": "ATOMUSDT",  
                    "orderId": "",  
                    "orderLinkId": "1666800494330512129"  
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
                    "code": 170213,  
                    "msg": "Order does not exist."  
                }  
            ]  
        },  
        "time": 1713434299047  
    }