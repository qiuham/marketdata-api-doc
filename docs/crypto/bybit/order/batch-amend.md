---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/order/batch-amend
api_type: Trading
updated_at: 2026-07-04 19:08:49.751137
---

# Batch Amend Order

tip

This endpoint allows you to amend more than one open order in a single request.

  * You can modify **unfilled** or **partially filled** orders. Conditional orders are not supported.
  * A maximum of 20 orders (option), 20 orders (inverse), 20 orders (linear), 10 orders (spot) can be amended per request.



### HTTP Request

POST`/v5/order/amend-batch`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type `linear`, `option`, `spot`, `inverse`  
request| **true**|  array| Object  
> symbol| **true**|  string| Symbol name, like `BTCUSDT`, uppercase only  
> orderId| false| string| Order ID. Either `orderId` or `orderLinkId` is required  
> orderLinkId| false| string| User customised order ID. Either `orderId` or `orderLinkId` is required  
> orderIv| false| string| Implied volatility. `option` **only**. Pass the real value, e.g for 10%, 0.1 should be passed  
> triggerPrice| false| string| 

  * For Perps & Futures, it is the conditional order trigger price. If you expect the price to rise to trigger your conditional order, make sure:  
_triggerPrice > market price_  
Else, _triggerPrice < market price_
  * For spot, it is for tpslOrder or stopOrder trigger price

  
> qty| false| string| Order quantity after modification. Do not pass it if not modify the qty  
> price| false| string| Order price after modification. Do not pass it if not modify the price  
> tpslMode| false| string| TP/SL mode 

  * `Full`: entire position for TP/SL. Then, tpOrderType or slOrderType must be `Market`
  * `Partial`: partial position tp/sl. Limit TP/SL order are supported. Note: When create limit tp/sl, tpslMode is **required** and it must be `Partial`

  
> takeProfit| false| string| Take profit price after modification. If pass "0", it means cancel the existing take profit of the order. Do not pass it if you do not want to modify the take profit  
> stopLoss| false| string| Stop loss price after modification. If pass "0", it means cancel the existing stop loss of the order. Do not pass it if you do not want to modify the stop loss  
> [tpTriggerBy](/docs/v5/enum#triggerby)| false| string| The price type to trigger take profit. When set a take profit, this param is **required** if no initial value for the order  
> [slTriggerBy](/docs/v5/enum#triggerby)| false| string| The price type to trigger stop loss. When set a take profit, this param is **required** if no initial value for the order  
> [triggerBy](/docs/v5/enum#triggerby)| false| string| Trigger price type  
> tpLimitPrice| false| string| Limit order price when take profit is triggered. Only working when original order sets partial limit tp/sl  
> slLimitPrice| false| string| Limit order price when stop loss is triggered. Only working when original order sets partial limit tp/sl  
  
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

The acknowledgement of an amend order request indicates that the request was sucessfully accepted. This request is asynchronous so please use the websocket to confirm the order status.

[](/docs/api-explorer/v5/trade/batch-amend)

* * *

### Request Example

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/amend-batch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672222935987  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "option",  
        "request": [  
            {  
                "symbol": "ETH-30DEC22-500-C",  
                "qty": null,  
                "price": null,  
                "orderIv": "6.8",  
                "orderId": "b551f227-7059-4fb5-a6a6-699c04dbd2f2"  
            },  
            {  
                "symbol": "ETH-30DEC22-700-C",  
                "qty": null,  
                "price": "650",  
                "orderIv": null,  
                "orderId": "fa6a595f-1a57-483f-b9d3-30e9c8235a52"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.amend_batch_order(  
        category="option",  
        request=[  
            {  
                "category": "option",  
                "symbol": "ETH-30DEC22-500-C",  
                "orderIv": "6.8",  
                "orderId": "b551f227-7059-4fb5-a6a6-699c04dbd2f2"  
            },  
            {  
                "category": "option",  
                "symbol": "ETH-30DEC22-700-C",  
                "price": "650",  
                "orderId": "fa6a595f-1a57-483f-b9d3-30e9c8235a52"  
            }  
        ]  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiAsyncTradeRestClient;  
    import com.bybit.api.client.domain.ProductType;  
    import com.bybit.api.client.domain.TradeOrderType;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    import java.util.Arrays;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var amendOrderRequests = Arrays.asList(TradeOrderRequest.builder().symbol("BTC-10FEB23-24000-C").qty("0.1").price("5").orderLinkId("9b381bb1-401").build(),  
                    TradeOrderRequest.builder().symbol("BTC-10FEB23-24000-C").qty("0.1").price("5").orderLinkId("82ee86dd-001").build());  
    var amendBatchOrders = BatchOrderRequest.builder().category(ProductType.OPTION).request(amendOrderRequests).build();  
    client.createBatchOrder(amendBatchOrders, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    var order1 = new OrderRequest { Symbol = "XRPUSDT", OrderId = "xxxxxxxxxx", Qty = "10", Price = "0.6080" };  
    var order2 = new OrderRequest { Symbol = "BLZUSDT", OrderId = "xxxxxxxxxx", Qty = "15", Price = "0.6090" };  
    var orderInfoString = await TradeService.AmendBatchOrder(category:Category.LINEAR, request: new List<OrderRequest> { order1, order2 });  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .batchAmendOrders('option', [  
            {  
                symbol: 'ETH-30DEC22-500-C',  
                orderIv: '6.8',  
                orderId: 'b551f227-7059-4fb5-a6a6-699c04dbd2f2',  
            },  
            {  
                symbol: 'ETH-30DEC22-700-C',  
                price: '650',  
                orderId: 'fa6a595f-1a57-483f-b9d3-30e9c8235a52',  
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
                    "category": "option",  
                    "symbol": "ETH-30DEC22-500-C",  
                    "orderId": "b551f227-7059-4fb5-a6a6-699c04dbd2f2",  
                    "orderLinkId": ""  
                },  
                {  
                    "category": "option",  
                    "symbol": "ETH-30DEC22-700-C",  
                    "orderId": "fa6a595f-1a57-483f-b9d3-30e9c8235a52",  
                    "orderLinkId": ""  
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
        "time": 1672222808060  
    }

---

# 批量修改委託單

提示

該接口支持批量修改委託單

  * 您只能修改那些**未成交** 或**部分成交** 的訂單. 條件單不支持批量修改.
  * 最多支持單個請求中修改, 期權: 20個訂單, 反向合約: 20個訂單, 正向合約: 20个訂單, 現貨: 10個訂單.



### HTTP請求

POST`/v5/order/amend-batch`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型 `linear`, `option`, `spot`, `inverse`  
request| **true**|  array| Object  
> symbol| **true**|  string| 合約名稱  
> orderId| false| string| 訂單Id. `orderId`和`orderLinkId`必傳其中一個  
> orderLinkId| false| string| 用戶自定義訂單Id. `orderId`和`orderLinkId`必傳其中一個  
> orderIv| false| string| 隱含波動率. 僅`option`有效. 按照實際值傳入, e.g., 對於10%, 則傳入0.1  
> triggerPrice| false| string| 

  * 對於期貨, 是條件單觸發價格參數. 若您希望市場價是要上升後觸發, 確保:  
_triggerPrice > 市場價格_  
否則, _triggerPrice < 市場價格_
  * 對於現貨, 這是下止盈止損單(tpslOrder)或者條件單(stopOrder)的觸發價格參數

  
> qty| false| string| 修改後的訂單數量. 若不修改，請不要傳該字段  
> price| false| string| 修改後的訂單價格. 若不修改，請不要傳該字段  
> tpslMode| false| string| 止盈止損模式 

  * `Full`: 全部倉位止盈止損. 此時, tpOrderType或者slOrderType必須傳`Market`
  * `Partial`: 部分倉位止盈止損. 支持創建限價止盈止損. 注意: 創建限價止盈止損時, tpslMode**必傳** 且為Partial

  
> takeProfit| false| string| 修改後的止盈價格. 當傳"0"時, 表示取消當前訂單上設置的止盈. 若不修改，請不要傳該字段  
> stopLoss| false| string| 修改後的止損價格. 當傳"0"時, 表示取消當前訂單上設置的止損. 若不修改，請不要傳該字段  
> [tpTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 止盈價格觸發類型. 若下單時未設置該值，則調用該接口修改止盈價格時，該字段**必傳**  
> [slTriggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 止損價格觸發類型. 若下單時未設置該值，則調用該接口修改止損價格時，該字段**必傳**  
> [triggerBy](/docs/zh-TW/v5/enum#triggerby)| false| string| 觸發價格的觸發類型  
> tpLimitPrice| false| string| 觸發止盈後轉換為限價單的價格. 當且僅當原始訂單下單時創建的是部分止盈止損限價單, 本字段才有效  
> slLimitPrice| false| string| 觸發止損後轉換為限價單的價格. 當且僅當原始訂單下單時創建的是部分止盈止損限價單, 本字段才有效  
  
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

[](/docs/zh-TW/api-explorer/v5/trade/batch-amend)

* * *

### 請求示例

  * HTTP
  * Python
  * Java
  * .Net
  * Node.js


    
    
    POST /v5/order/amend-batch HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1672222935987  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "category": "option",  
        "request": [  
            {  
                "symbol": "ETH-30DEC22-500-C",  
                "qty": null,  
                "price": null,  
                "orderIv": "6.8",  
                "orderId": "b551f227-7059-4fb5-a6a6-699c04dbd2f2"  
            },  
            {  
                "symbol": "ETH-30DEC22-700-C",  
                "qty": null,  
                "price": "650",  
                "orderIv": null,  
                "orderId": "fa6a595f-1a57-483f-b9d3-30e9c8235a52"  
            }  
        ]  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.amend_batch_order(  
        category="option",  
        request=[  
            {  
                "category": "option",  
                "symbol": "ETH-30DEC22-500-C",  
                "orderIv": "6.8",  
                "orderId": "b551f227-7059-4fb5-a6a6-699c04dbd2f2"  
            },  
            {  
                "category": "option",  
                "symbol": "ETH-30DEC22-700-C",  
                "price": "650",  
                "orderId": "fa6a595f-1a57-483f-b9d3-30e9c8235a52"  
            }  
        ]  
    ))  
    
    
    
    import com.bybit.api.client.restApi.BybitApiAsyncTradeRestClient;  
    import com.bybit.api.client.domain.ProductType;  
    import com.bybit.api.client.domain.TradeOrderType;  
    import com.bybit.api.client.domain.trade.*;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    import java.util.Arrays;  
    BybitApiClientFactory factory = BybitApiClientFactory.newInstance("YOUR_API_KEY", "YOUR_API_SECRET");  
    BybitApiAsyncTradeRestClient client = factory.newAsyncTradeRestClient();  
    var amendOrderRequests = Arrays.asList(TradeOrderRequest.builder().symbol("BTC-10FEB23-24000-C").qty("0.1").price("5").orderLinkId("9b381bb1-401").build(),  
                    TradeOrderRequest.builder().symbol("BTC-10FEB23-24000-C").qty("0.1").price("5").orderLinkId("82ee86dd-001").build());  
    var amendBatchOrders = BatchOrderRequest.builder().category(ProductType.OPTION).request(amendOrderRequests).build();  
    client.createBatchOrder(amendBatchOrders, System.out::println);  
    
    
    
    using bybit.net.api.ApiServiceImp;  
    using bybit.net.api.Models.Trade;  
    var order1 = new OrderRequest { Symbol = "XRPUSDT", OrderId = "xxxxxxxxxx", Qty = "10", Price = "0.6080" };  
    var order2 = new OrderRequest { Symbol = "BLZUSDT", OrderId = "xxxxxxxxxx", Qty = "15", Price = "0.6090" };  
    var orderInfoString = await TradeService.AmendBatchOrder(category:Category.LINEAR, request: new List<OrderRequest> { order1, order2 });  
    Console.WriteLine(orderInfoString);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
        key: 'xxxxxxxxxxxxxxxxxx',  
        secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
        .batchAmendOrders('option', [  
            {  
                symbol: 'ETH-30DEC22-500-C',  
                orderIv: '6.8',  
                orderId: 'b551f227-7059-4fb5-a6a6-699c04dbd2f2',  
            },  
            {  
                symbol: 'ETH-30DEC22-700-C',  
                price: '650',  
                orderId: 'fa6a595f-1a57-483f-b9d3-30e9c8235a52',  
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
                    "category": "option",  
                    "symbol": "ETH-30DEC22-500-C",  
                    "orderId": "b551f227-7059-4fb5-a6a6-699c04dbd2f2",  
                    "orderLinkId": ""  
                },  
                {  
                    "category": "option",  
                    "symbol": "ETH-30DEC22-700-C",  
                    "orderId": "fa6a595f-1a57-483f-b9d3-30e9c8235a52",  
                    "orderLinkId": ""  
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
        "time": 1672222808060  
    }