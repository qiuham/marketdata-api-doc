---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
api_type: Market Data
updated_at: 2026-05-27 18:54:30.461526
---

# Trading endpoints

### New order (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade "Direct link to New order \(TRADE\)")
    
    
    POST /api/v3/order  
    

Send in a new order.

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

**Weight:** 1

**Unfilled Order Count:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES| Please see [Enums](/docs/binance-spot-api-docs/enums#side) for supported values.  
type| ENUM| YES| Please see [Enums](/docs/binance-spot-api-docs/enums#ordertypes) for supported values.  
timeInForce| ENUM| NO| Please see [Enums](/docs/binance-spot-api-docs/enums#timeinforce) for supported values.  
quantity| DECIMAL| NO|   
quoteOrderQty| DECIMAL| NO|   
price| DECIMAL| NO|   
newClientOrderId| STRING| NO| A unique id among open orders. Automatically generated if not sent.  
Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.  
strategyId| LONG| NO|   
strategyType| INT| NO| The value cannot be less than `1000000`.  
stopPrice| DECIMAL| NO| Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.  
trailingDelta| LONG| NO| See [Trailing Stop order FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq).  
icebergQty| DECIMAL| NO| Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.  
newOrderRespType| ENUM| NO| Set the response JSON. `ACK`, `RESULT`, or `FULL`; `MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`.  
selfTradePreventionMode| ENUM| NO| The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes).  
pegPriceType| ENUM| NO| `PRIMARY_PEG` or `MARKET_PEG`.   
See [Pegged Orders Info](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pegOffsetValue| INT| NO| Price level to peg the price to (max: 100).   
See [Pegged Orders Info](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pegOffsetType| ENUM| NO| Only `PRICE_LEVEL` is supported.   
See [Pegged Orders Info](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
Some additional mandatory parameters based on order `type`:

Type| Additional mandatory parameters| Additional Information  
---|---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`|   
`MARKET`| `quantity` or `quoteOrderQty`| `MARKET` orders using the `quantity` field specifies the amount of the `base asset` the user wants to buy or sell at the market price.   
E.g. MARKET order on BTCUSDT will specify how much BTC the user is buying or selling.   
  
`MARKET` orders using `quoteOrderQty` specifies the amount the user wants to spend (when buying) or receive (when selling) the `quote` asset; the correct `quantity` will be determined based on the market liquidity and `quoteOrderQty`.   
E.g. Using the symbol BTCUSDT:   
`BUY` side, the order will buy as many BTC as `quoteOrderQty` USDT can.   
`SELL` side, the order will sell as much BTC needed to receive `quoteOrderQty` USDT.  
`STOP_LOSS`| `quantity`, `stopPrice` or `trailingDelta`| This will execute a `MARKET` order when the conditions are met. (e.g. `stopPrice` is met or `trailingDelta` is activated)  
`STOP_LOSS_LIMIT`| `timeInForce`, `quantity`, `price`, `stopPrice` or `trailingDelta`|   
`TAKE_PROFIT`| `quantity`, `stopPrice` or `trailingDelta`| This will execute a `MARKET` order when the conditions are met. (e.g. `stopPrice` is met or `trailingDelta` is activated)  
`TAKE_PROFIT_LIMIT`| `timeInForce`, `quantity`, `price`, `stopPrice` or `trailingDelta`|   
`LIMIT_MAKER`| `quantity`, `price`| This is a `LIMIT` order that will be rejected if the order immediately matches and trades as a taker.   
This is also known as a POST-ONLY order.  
  
Notes on using parameters for Pegged Orders:

  * These parameters are allowed for `LIMIT`, `LIMIT_MAKER`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` orders.
  * If `pegPriceType` is specified, `price` becomes optional. Otherwise, it is still mandatory.
  * `pegPriceType=PRIMARY_PEG` means the primary peg, that is the best price on the same side of the order book as your order.
  * `pegPriceType=MARKET_PEG` means the market peg, that is the best price on the opposite side of the order book from your order.
  * Use `pegOffsetType` and `pegOffsetValue` to request a price level other than the best one. These parameters must be specified together.



Other info:

  * Any `LIMIT` or `LIMIT_MAKER` type order can be made an iceberg order by sending an `icebergQty`.

  * Any order with an `icebergQty` MUST have `timeInForce` set to `GTC`.

  * For `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` and `TAKE_PROFIT` orders, `trailingDelta` can be combined with `stopPrice`.

  * `MARKET` orders using `quoteOrderQty` will not break `LOT_SIZE` filter rules; the order will execute a `quantity` that will have the notional value as close as possible to `quoteOrderQty`. Trigger order price rules against market price for both MARKET and LIMIT versions:

  * Price above market price: `STOP_LOSS` `BUY`, `TAKE_PROFIT` `SELL`

  * Price below market price: `STOP_LOSS` `SELL`, `TAKE_PROFIT` `BUY`




**Data Source:** Matching Engine

**Response - ACK:**
    
    
    {  
        "symbol": "BTCUSDT",  
        "orderId": 28,  
        "orderListId": -1, // Unless it's part of an order list, value will be -1  
        "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",  
        "transactTime": 1507725176595  
    }  
    

**Response - RESULT:**
    
    
    {  
        "symbol": "BTCUSDT",  
        "orderId": 28,  
        "orderListId": -1, // Unless it's part of an order list, value will be -1  
        "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",  
        "transactTime": 1507725176595,  
        "price": "0.00000000",  
        "origQty": "10.00000000",  
        "executedQty": "10.00000000",  
        "origQuoteOrderQty": "0.000000",  
        "cummulativeQuoteQty": "10.00000000",  
        "status": "FILLED",  
        "timeInForce": "GTC",  
        "type": "MARKET",  
        "side": "SELL",  
        "workingTime": 1507725176595,  
        "selfTradePreventionMode": "NONE"  
    }  
    

**Response - FULL:**
    
    
    {  
        "symbol": "BTCUSDT",  
        "orderId": 28,  
        "orderListId": -1, // Unless it's part of an order list, value will be -1  
        "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",  
        "transactTime": 1507725176595,  
        "price": "0.00000000",  
        "origQty": "10.00000000",  
        "executedQty": "10.00000000",  
        "origQuoteOrderQty": "0.000000",  
        "cummulativeQuoteQty": "10.00000000",  
        "status": "FILLED",  
        "timeInForce": "GTC",  
        "type": "MARKET",  
        "side": "SELL",  
        "workingTime": 1507725176595,  
        "selfTradePreventionMode": "NONE",  
        "fills": [  
            {  
                "price": "4000.00000000",  
                "qty": "1.00000000",  
                "commission": "4.00000000",  
                "commissionAsset": "USDT",  
                "tradeId": 56  
            },  
            {  
                "price": "3999.00000000",  
                "qty": "5.00000000",  
                "commission": "19.99500000",  
                "commissionAsset": "USDT",  
                "tradeId": 57  
            },  
            {  
                "price": "3998.00000000",  
                "qty": "2.00000000",  
                "commission": "7.99600000",  
                "commissionAsset": "USDT",  
                "tradeId": 58  
            },  
            {  
                "price": "3997.00000000",  
                "qty": "1.00000000",  
                "commission": "3.99700000",  
                "commissionAsset": "USDT",  
                "tradeId": 59  
            },  
            {  
                "price": "3995.00000000",  
                "qty": "1.00000000",  
                "commission": "3.99500000",  
                "commissionAsset": "USDT",  
                "tradeId": 60  
            }  
        ]  
    }  
    

**Conditional fields in Order Responses**

There are fields in the order responses (e.g. order placement, order query, order cancellation) that appear only if certain conditions are met.

These fields can apply to order lists.

The fields are listed below:

Field| Description| Visibility conditions| Examples  
---|---|---|---  
`icebergQty`| Quantity for the iceberg order| Appears only if the parameter `icebergQty` was sent in the request.| `"icebergQty": "0.00000000"`  
`preventedMatchId`| When used in combination with `symbol`, can be used to query a prevented match.| Appears only if the order expired due to STP.| `"preventedMatchId": 0`  
`preventedQuantity`| Order quantity that expired due to STP| Appears only if the order expired due to STP.| `"preventedQuantity": "1.200000"`  
`stopPrice`| Price when the algorithmic order will be triggered| Appears for `STOP_LOSS`. `TAKE_PROFIT`, `STOP_LOSS_LIMIT` and `TAKE_PROFIT_LIMIT` orders.| `"stopPrice": "23500.00000000"`  
`strategyId`| Can be used to label an order that's part of an order strategy.| Appears if the parameter was populated in the request.| `"strategyId": 37463720`  
`strategyType`| Can be used to label an order that is using an order strategy.| Appears if the parameter was populated in the request.| `"strategyType": 1000000`  
`trailingDelta`| Delta price change required before order activation| Appears for Trailing Stop Orders.| `"trailingDelta": 10`  
`trailingTime`| Time when the trailing order is now active and tracking price changes| Appears only for Trailing Stop Orders.| `"trailingTime": -1`  
`usedSor`| Field that determines whether order used SOR| Appears when placing orders using SOR| `"usedSor": true`  
`workingFloor`| Field that determines whether the order is being filled by the SOR or by the order book the order was submitted to.| Appears when placing orders using SOR| `"workingFloor": "SOR"`  
`pegPriceType`| Price peg type| Only for pegged orders| `"pegPriceType": "PRIMARY_PEG"`  
`pegOffsetType`| Price peg offset type| Only for pegged orders, if requested| `"pegOffsetType": "PRICE_LEVEL"`  
`pegOffsetValue`| Price peg offset value| Only for pegged orders, if requested| `"pegOffsetValue": 5`  
`peggedPrice`| Current price order is pegged at| Only for pegged orders, once determined| `"peggedPrice": "87523.83710000"`  
`expiryReason`| Cause of the order’s expiration| When an order has expired| `"expiryReason": "INSUFFICIENT_LIQUIDITY"`  
  
### Test new order (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#test-new-order-trade "Direct link to Test new order \(TRADE\)")
    
    
    POST /api/v3/order/test  
    

Test new order creation and signature/recvWindow long. Creates and validates a new order but does not send it into the matching engine.

**Weight:**

Condition| Request Weight  
---|---  
Without `computeCommissionRates`| 1  
With `computeCommissionRates`| 20  
  
**Parameters:**

In addition to all parameters accepted by [`POST /api/v3/order`](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade), the following optional parameters are also accepted:

Name| Type| Mandatory| Description  
---|---|---|---  
computeCommissionRates| BOOLEAN| NO| Default: `false`   
See [Commissions FAQ](/docs/binance-spot-api-docs/faqs/commission_faq#test-order-diferences) to learn more.  
  
**Data Source:** Memory

**Response:**

Without `computeCommissionRates`
    
    
    {}  
    

With `computeCommissionRates`
    
    
    {  
        "standardCommissionForOrder": {   // Standard commission rates on trades from the order.  
            "maker": "0.00000112",  
            "taker": "0.00000114"  
        },  
        "specialCommissionForOrder": {    // Special commission rates on trades from the order.  
            "maker": "0.05000000",  
            "taker": "0.06000000"  
        },  
        "taxCommissionForOrder": {        // Tax commission rates for trades from the order.  
            "maker": "0.00000112",  
            "taker": "0.00000114"  
        },  
        "discount": {                     // Discount on standard commissions when paying in BNB.  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"      // Standard commission is reduced by this rate when paying commission in BNB.  
        }  
    }  
    

### Cancel order (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-order-trade "Direct link to Cancel order \(TRADE\)")
    
    
    DELETE /api/v3/order  
    

Cancel an active order.

**Weight:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
newClientOrderId| STRING| NO| Used to uniquely identify this cancel. Automatically generated by default.  
cancelRestrictions| ENUM| NO| Supported values:   
`ONLY_NEW` \- Cancel will succeed if the order status is `NEW`.  
`ONLY_PARTIALLY_FILLED ` \- Cancel will succeed if order status is `PARTIALLY_FILLED`.  
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
Notes:

  * Either `orderId` or `origClientOrderId` must be sent.
  * If both `orderId` and `origClientOrderId` are provided, the `orderId` is searched first, then the `origClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.



**Data Source:** Matching Engine

**Response:**
    
    
    {  
        "symbol": "LTCBTC",  
        "origClientOrderId": "myOrder1",  
        "orderId": 4,  
        "orderListId": -1, // Unless it's part of an order list, value will be -1  
        "clientOrderId": "cancelMyOrder1",  
        "transactTime": 1684804350068,  
        "price": "2.00000000",  
        "origQty": "1.00000000",  
        "executedQty": "0.00000000",  
        "origQuoteOrderQty": "0.000000",  
        "cummulativeQuoteQty": "0.00000000",  
        "status": "CANCELED",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "side": "BUY",  
        "selfTradePreventionMode": "NONE"  
    }  
    

**Notes:**

  * The payload above does not show all fields that can appear in the order response. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses).
  * The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only `orderId` is sent. Sending `origClientOrderId` or both `orderId` \+ `origClientOrderId` will be slower.



**Regarding`cancelRestrictions`**

  * If the `cancelRestrictions` value is not any of the supported values, the error will be:


    
    
    {  
        "code": -1145,  
        "msg": "Invalid cancelRestrictions"  
    }  
    

  * If the order did not pass the conditions for `cancelRestrictions`, the error will be:


    
    
    {  
        "code": -2011,  
        "msg": "Order was not canceled due to cancel restrictions."  
    }  
    

### Cancel All Open Orders on a Symbol (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-all-open-orders-on-a-symbol-trade "Direct link to Cancel All Open Orders on a Symbol \(TRADE\)")
    
    
    DELETE /api/v3/openOrders  
    

Cancels all active orders on a symbol. This includes orders that are part of an order list.

**Weight:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
**Data Source:** Matching Engine

**Response:**
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "E6APeyTJvkMvLMYMqu1KQ4",  
            "orderId": 11,  
            "orderListId": -1,  
            "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
            "transactTime": 1684804350068,  
            "price": "0.089853",  
            "origQty": "0.178622",  
            "executedQty": "0.000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "selfTradePreventionMode": "NONE"  
        },  
        {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "A3EF2HCwxgZPFMrfwbgrhv",  
            "orderId": 13,  
            "orderListId": -1,  
            "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
            "transactTime": 1684804350069,  
            "price": "0.090430",  
            "origQty": "0.178622",  
            "executedQty": "0.000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "selfTradePreventionMode": "NONE"  
        },  
        {  
            "orderListId": 1929,  
            "contingencyType": "OCO",  
            "listStatusType": "ALL_DONE",  
            "listOrderStatus": "ALL_DONE",  
            "listClientOrderId": "2inzWQdDvZLHbbAmAozX2N",  
            "transactionTime": 1585230948299,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 20,  
                    "clientOrderId": "CwOOIPHSmYywx6jZX77TdL"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 21,  
                    "clientOrderId": "461cPg51vQjV3zIMOXNz39"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "CwOOIPHSmYywx6jZX77TdL",  
                    "orderId": 20,  
                    "orderListId": 1929,  
                    "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
                    "transactTime": 1688005070874,  
                    "price": "0.668611",  
                    "origQty": "0.690354",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "BUY",  
                    "stopPrice": "0.378131",  
                    "icebergQty": "0.017083",  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "461cPg51vQjV3zIMOXNz39",  
                    "orderId": 21,  
                    "orderListId": 1929,  
                    "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
                    "transactTime": 1688005070874,  
                    "price": "0.008791",  
                    "origQty": "0.690354",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "BUY",  
                    "icebergQty": "0.639962",  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        }  
    ]  
    

### Cancel an Existing Order and Send a New Order (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-an-existing-order-and-send-a-new-order-trade "Direct link to Cancel an Existing Order and Send a New Order \(TRADE\)")
    
    
    POST /api/v3/order/cancelReplace  
    

  * Cancels an existing order and places a new order on the same symbol.
  * Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.
  * A new order that was not attempted (i.e. when `newOrderResult: NOT_ATTEMPTED`), will still increase the unfilled order count by 1.
  * You can only cancel an individual order from an orderList using this endpoint, but the result is the same as canceling the entire orderList.



**Weight:** 1

**Unfilled Order Count:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES|   
type| ENUM| YES|   
cancelReplaceMode| ENUM| YES| The allowed values are:   
`STOP_ON_FAILURE` \- If the cancel request fails, the new order placement will not be attempted.   
`ALLOW_FAILURE` \- new order placement will be attempted even if cancel request fails.  
timeInForce| ENUM| NO|   
quantity| DECIMAL| NO|   
quoteOrderQty| DECIMAL| NO|   
price| DECIMAL| NO|   
cancelNewClientOrderId| STRING| NO| Used to uniquely identify this cancel. Automatically generated by default.  
cancelOrigClientOrderId| STRING| NO| Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent.   
  
If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order.   
  
If both conditions are not met the request will be rejected.  
cancelOrderId| LONG| NO| Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent.   
  
If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order.   
  
If both conditions are not met the request will be rejected.  
newClientOrderId| STRING| NO| Used to identify the new order.  
strategyId| LONG| NO|   
strategyType| INT| NO| The value cannot be less than `1000000`.  
stopPrice| DECIMAL| NO|   
trailingDelta| LONG| NO| See [Trailing Stop order FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq)  
icebergQty| DECIMAL| NO|   
newOrderRespType| ENUM| NO| Allowed values:   
`ACK`, `RESULT`, `FULL`   
`MARKET` and `LIMIT` orders types default to `FULL`; all other orders default to `ACK`  
selfTradePreventionMode| ENUM| NO| The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes).  
cancelRestrictions| ENUM| NO| Supported values:   
`ONLY_NEW` \- Cancel will succeed if the order status is `NEW`.  
`ONLY_PARTIALLY_FILLED ` \- Cancel will succeed if order status is `PARTIALLY_FILLED`. For more information please refer to [Regarding `cancelRestrictions`](/docs/binance-spot-api-docs/rest-api/trading-endpoints#regarding-cancelrestrictions)  
orderRateLimitExceededMode| ENUM| No| Supported values:   
`DO_NOTHING` (default)- will only attempt to cancel the order if account has not exceeded the unfilled order rate limit  
`CANCEL_ONLY` \- will always cancel the order  
pegPriceType| ENUM| NO| `PRIMARY_PEG` or `MARKET_PEG`   
See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pegOffsetValue| INT| NO| Price level to peg the price to (max: 100)   
See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pegOffsetType| ENUM| NO| Only `PRICE_LEVEL` is supported   
See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
Similar to `POST /api/v3/order`, additional mandatory parameters are determined by `type`.

Response format varies depending on whether the processing of the message succeeded, partially succeeded, or failed.

**Data Source:** Matching Engine

Request | Response  
---|---  
`cancelReplaceMode` | `orderRateLimitExceededMode` | Unfilled Order Count | `cancelResult` | `newOrderResult` | `status`  
`STOP_ON_FAILURE` | `DO_NOTHING` | Within Limits | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ➖ `NOT_ATTEMPTED` | `400`  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
Exceeds Limits | ✅ `SUCCESS` | ✅ `SUCCESS` | N/A  
❌ `FAILURE` | ➖ `NOT_ATTEMPTED` | N/A  
✅ `SUCCESS` | ❌ `FAILURE` | N/A  
`CANCEL_ONLY` | Within Limits | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ➖ `NOT_ATTEMPTED` | `400`  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
Exceeds Limits | ❌ `FAILURE` | ➖ `NOT_ATTEMPTED` | `429`  
✅ `SUCCESS` | ❌ `FAILURE` | `429`  
`ALLOW_FAILURE` | `DO_NOTHING` | Within Limits | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ❌ `FAILURE` | `400`  
❌ `FAILURE` | ✅ `SUCCESS` | `409`  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
Exceeds Limits | ✅ `SUCCESS` | ✅ `SUCCESS` | N/A  
❌ `FAILURE` | ❌ `FAILURE` | N/A  
❌ `FAILURE` | ✅ `SUCCESS` | N/A  
✅ `SUCCESS` | ❌ `FAILURE` | N/A  
`CANCEL_ONLY` | Within Limits | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ❌ `FAILURE` | `400`  
❌ `FAILURE` | ✅ `SUCCESS` | `409`  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
Exceeds Limits | ✅ `SUCCESS` | ✅ `SUCCESS` | `N/A`  
❌ `FAILURE` | ❌ `FAILURE` | `400`  
❌ `FAILURE` | ✅ `SUCCESS` | N/A  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
  
**Response SUCCESS and account has not exceeded the unfilled order count:**
    
    
    // Both the cancel order placement and new order placement succeeded.  
    {  
        "cancelResult": "SUCCESS",  
        "newOrderResult": "SUCCESS",  
        "cancelResponse": {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "DnLo3vTAQcjha43lAZhZ0y",  
            "orderId": 9,  
            "orderListId": -1,  
            "clientOrderId": "osxN3JXAtJvKvCqGeMWMVR",  
            "transactTime": 1684804350068,  
            "price": "0.01000000",  
            "origQty": "0.000100",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL",  
            "selfTradePreventionMode": "NONE"  
        },  
        "newOrderResponse": {  
            "symbol": "BTCUSDT",  
            "orderId": 10,  
            "orderListId": -1,  
            "clientOrderId": "wOceeeOzNORyLiQfw7jd8S",  
            "transactTime": 1652928801803,  
            "price": "0.02000000",  
            "origQty": "0.040000",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "workingTime": 1669277163808,  
            "fills": [],  
            "selfTradePreventionMode": "NONE"  
        }  
    }  
    

**Response when Cancel Order Fails with STOP_ON FAILURE and account has not exceeded their unfilled order count:**
    
    
    {  
        "code": -2022,  
        "msg": "Order cancel-replace failed.",  
        "data": {  
            "cancelResult": "FAILURE",  
            "newOrderResult": "NOT_ATTEMPTED",  
            "cancelResponse": {  
                "code": -2011,  
                "msg": "Unknown order sent."  
            },  
            "newOrderResponse": null  
        }  
    }  
    

**Response when Cancel Order Succeeds but New Order Placement Fails and account has not exceeded their unfilled order count:**
    
    
    {  
        "code": -2021,  
        "msg": "Order cancel-replace partially failed.",  
        "data": {  
            "cancelResult": "SUCCESS",  
            "newOrderResult": "FAILURE",  
            "cancelResponse": {  
                "symbol": "BTCUSDT",  
                "origClientOrderId": "86M8erehfExV8z2RC8Zo8k",  
                "orderId": 3,  
                "orderListId": -1,  
                "clientOrderId": "G1kLo6aDv2KGNTFcjfTSFq",  
                "transactTime": 1684804350068,  
                "price": "0.006123",  
                "origQty": "10000.000000",  
                "executedQty": "0.000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.000000",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "SELL",  
                "selfTradePreventionMode": "NONE"  
            },  
            "newOrderResponse": {  
                "code": -2010,  
                "msg": "Order would immediately match and take."  
            }  
        }  
    }  
    

**Response when Cancel Order fails with ALLOW_FAILURE and account has not exceeded their unfilled order count:**
    
    
    {  
        "code": -2021,  
        "msg": "Order cancel-replace partially failed.",  
        "data": {  
            "cancelResult": "FAILURE",  
            "newOrderResult": "SUCCESS",  
            "cancelResponse": {  
                "code": -2011,  
                "msg": "Unknown order sent."  
            },  
            "newOrderResponse": {  
                "symbol": "BTCUSDT",  
                "orderId": 11,  
                "orderListId": -1,  
                "clientOrderId": "pfojJMg6IMNDKuJqDxvoxN",  
                "transactTime": 1648540168818  
            }  
        }  
    }  
    

**Response when both Cancel Order and New Order Placement fail using`cancelReplaceMode=ALLOW_FAILURE` and account has not exceeded their unfilled order count:**
    
    
    {  
        "code": -2022,  
        "msg": "Order cancel-replace failed.",  
        "data": {  
            "cancelResult": "FAILURE",  
            "newOrderResult": "FAILURE",  
            "cancelResponse": {  
                "code": -2011,  
                "msg": "Unknown order sent."  
            },  
            "newOrderResponse": {  
                "code": -2010,  
                "msg": "Order would immediately match and take."  
            }  
        }  
    }  
    

**Response when using`orderRateLimitExceededMode=DO_NOTHING` and account's unfilled order count has been exceeded:**
    
    
    {  
        "code": -1015,  
        "msg": "Too many new orders; current limit is 1 orders per 10 SECOND."  
    }  
    

**Response when using`orderRateLimitExceededMode=CANCEL_ONLY` and account's unfilled order count has been exceeded:**
    
    
    {  
        "code": -2021,  
        "msg": "Order cancel-replace partially failed.",  
        "data": {  
            "cancelResult": "SUCCESS",  
            "newOrderResult": "FAILURE",  
            "cancelResponse": {  
                "symbol": "LTCBNB",  
                "origClientOrderId": "GKt5zzfOxRDSQLveDYCTkc",  
                "orderId": 64,  
                "orderListId": -1,  
                "clientOrderId": "loehOJF3FjoreUBDmv739R",  
                "transactTime": 1715779007228,  
                "price": "1.00",  
                "origQty": "10.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "selfTradePreventionMode": "NONE"  
            },  
            "newOrderResponse": {  
                "code": -1015,  
                "msg": "Too many new orders; current limit is 1 orders per 10 SECOND."  
            }  
        }  
    }  
    

**Notes:**

  * The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses).
  * The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only `orderId` is sent. Sending `origClientOrderId` or both `orderId` \+ `origClientOrderId` will be slower.



### Order Amend Keep Priority (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#order-amend-keep-priority-trade "Direct link to Order Amend Keep Priority \(TRADE\)")
    
    
    PUT /api/v3/order/amend/keepPriority  
    

Reduce the quantity of an existing open order.

This adds 0 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [Order Amend Keep Priority FAQ](/docs/binance-spot-api-docs/faqs/order_amend_keep_priority) to learn more.

**Weight** : 4

**Unfilled Order Count:** 0

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO*| `orderId` or `origClientOrderId` must be sent  
origClientOrderId| STRING| NO*| `orderId` or `origClientOrderId` must be sent  
newClientOrderId| STRING| NO*| The new client order ID for the order after being amended.   
If not sent, one will be randomly generated.   
It is possible to reuse the current clientOrderId by sending it as the `newClientOrderId`.  
newQty| DECIMAL| YES| `newQty` must be greater than 0 and less than the order's quantity.  
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
**Data Source** : Matching Engine

**Response:** Response for a single order:
    
    
    {  
        "transactTime": 1741926410255,  
        "executionId": 75,  
        "amendedOrder": {  
            "symbol": "BTCUSDT",  
            "orderId": 33,  
            "orderListId": -1,  
            "origClientOrderId": "5xrgbMyg6z36NzBn2pbT8H",  
            "clientOrderId": "PFaq6hIHxqFENGfdtn4J6Q",  
            "price": "6.00000000",  
            "qty": "5.00000000",  
            "executedQty": "0.00000000",  
            "preventedQty": "0.00000000",  
            "quoteOrderQty": "0.00000000",  
            "cumulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL",  
            "workingTime": 1741926410242,  
            "selfTradePreventionMode": "NONE"  
        }  
    }  
    

Response for an order that is part of an Order list:
    
    
    {  
        "transactTime": 1741669661670,  
        "executionId": 22,  
        "amendedOrder": {  
            "symbol": "BTCUSDT",  
            "orderId": 9,  
            "orderListId": 1,  
            "origClientOrderId": "W0fJ9fiLKHOJutovPK3oJp",  
            "clientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi",  
            "price": "0.00000000",  
            "qty": "4.00000000",  
            "executedQty": "0.00000000",  
            "preventedQty": "0.00000000",  
            "quoteOrderQty": "0.00000000",  
            "cumulativeQuoteQty": "0.00000000",  
            "status": "PENDING_NEW",  
            "timeInForce": "GTC",  
            "type": "MARKET",  
            "side": "BUY",  
            "selfTradePreventionMode": "NONE"  
        },  
        "listStatus": {  
            "orderListId": 1,  
            "contingencyType": "OTO",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "AT7FTxZXylVSwRoZs52mt3",  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 8,  
                    "clientOrderId": "GkwwHZUUbFtZOoH1YsZk9Q"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 9,  
                    "clientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi"  
                }  
            ]  
        }  
    }  
    

**Note:** The payloads above do not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses).

### Order lists[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#order-lists "Direct link to Order lists")

#### New OCO - Deprecated (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-oco---deprecated-trade "Direct link to New OCO - Deprecated \(TRADE\)")
    
    
    POST /api/v3/order/oco  
    

Send in a new OCO.

  * Price Restrictions: 
    * `SELL`: Limit Price > Last Price > Stop Price
    * `BUY`: Limit Price < Last Price < Stop Price
  * Quantity Restrictions: 
    * Both legs must have the same quantity.
    * `ICEBERG` quantities however do not have to be the same
  * `OCO` adds **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.



**Weight:** 1

**Unfilled Order Count:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| A unique Id for the entire orderList  
side| ENUM| YES|   
quantity| DECIMAL| YES|   
limitClientOrderId| STRING| NO| A unique Id for the limit order  
price| DECIMAL| YES|   
limitStrategyId| LONG| NO|   
limitStrategyType| INT| NO| The value cannot be less than `1000000`.  
limitIcebergQty| DECIMAL| NO| Used to make the `LIMIT_MAKER` leg an iceberg order.  
trailingDelta| LONG| NO|   
stopClientOrderId| STRING| NO| A unique Id for the stop loss/stop loss limit leg  
stopPrice| DECIMAL| YES|   
stopStrategyId| LONG| NO|   
stopStrategyType| INT| NO| The value cannot be less than `1000000`.  
stopLimitPrice| DECIMAL| NO| If provided, `stopLimitTimeInForce` is required.  
stopIcebergQty| DECIMAL| NO| Used with `STOP_LOSS_LIMIT` leg to make an iceberg order.  
stopLimitTimeInForce| ENUM| NO| Valid values are `GTC`/`FOK`/`IOC`  
newOrderRespType| ENUM| NO| Set the response JSON.  
selfTradePreventionMode| ENUM| NO| The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes).  
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
**Data Source:** Matching Engine

**Response:**
    
    
    {  
        "orderListId": 0,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "JYVpp3F0f5CAG15DhtrqLp",  
        "transactionTime": 1563417480525,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 2,  
                "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 3,  
                "clientOrderId": "xTXKaGYd4bluPVp78IVRvl"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 2,  
                "orderListId": 0,  
                "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos",  
                "transactTime": 1563417480525,  
                "price": "0.000000",  
                "origQty": "0.624363",  
                "executedQty": "0.000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "STOP_LOSS",  
                "side": "BUY",  
                "stopPrice": "0.960664",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 3,  
                "orderListId": 0,  
                "clientOrderId": "xTXKaGYd4bluPVp78IVRvl",  
                "transactTime": 1563417480525,  
                "price": "0.036435",  
                "origQty": "0.624363",  
                "executedQty": "0.000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "BUY",  
                "workingTime": 1563417480525,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

#### New Order list - OCO (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-list---oco-trade "Direct link to New Order list - OCO \(TRADE\)")
    
    
    POST /api/v3/orderList/oco  
    

Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

  * An OCO has 2 orders called the **above order** and **below order**.
  * One of the orders must be a `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` order and the other must be `STOP_LOSS` or `STOP_LOSS_LIMIT` order.
  * Price restrictions 
    * If the OCO is on the `SELL` side: 
      * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
      * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
    * If the OCO is on the `BUY` side: 
      * `LIMIT_MAKER/TAKE_PROFIT_LIMIT price` < Last Traded Price < `stopPrice`
      * `TAKE_PROFIT stopPrice` < Last Traded Price < `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
  * OCOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.



**Weight:** 1

**Unfilled Order Count:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| Yes|   
listClientOrderId| STRING| No| Arbitrary unique ID among open order lists. Automatically generated if not sent.   
A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.   
`listClientOrderId` is distinct from the `aboveClientOrderId` and the `belowCLientOrderId`.  
side| ENUM| Yes| `BUY` or `SELL`  
quantity| DECIMAL| Yes| Quantity for both orders of the order list.  
aboveType| ENUM| Yes| Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
aboveClientOrderId| STRING| No| Arbitrary unique ID among open orders for the above order. Automatically generated if not sent  
aboveIcebergQty| LONG| No| Note that this can only be used if `aboveTimeInForce` is `GTC`.  
abovePrice| DECIMAL| No| Can be used if `aboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.  
aboveStopPrice| DECIMAL| No| Can be used if `aboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.   
Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified.  
aboveTrailingDelta| LONG| No| See [Trailing Stop order FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq).  
aboveTimeInForce| ENUM| No| Required if `aboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`  
aboveStrategyId| LONG| No| Arbitrary numeric value identifying the above order within an order strategy.  
aboveStrategyType| INT| No| Arbitrary numeric value identifying the above order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
abovePegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
abovePegOffsetType| ENUM| NO|   
abovePegOffsetValue| INT| NO|   
belowType| ENUM| Yes| Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`  
belowClientOrderId| STRING| No| Arbitrary unique ID among open orders for the below order. Automatically generated if not sent  
belowIcebergQty| LONG| No| Note that this can only be used if `belowTimeInForce` is `GTC`.  
belowPrice| DECIMAL| No| Can be used if `belowType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.  
belowStopPrice| DECIMAL| No| Can be used if `belowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` or `TAKE_PROFIT_LIMIT`   
Either `belowStopPrice` or `belowTrailingDelta` or both, must be specified.  
belowTrailingDelta| LONG| No| See [Trailing Stop order FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq).  
belowTimeInForce| ENUM| No| Required if `belowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.  
belowStrategyId| LONG| No| Arbitrary numeric value identifying the below order within an order strategy.  
belowStrategyType| INT| No| Arbitrary numeric value identifying the below order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
belowPegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
belowPegOffsetType| ENUM| NO|   
belowPegOffsetValue| INT| NO|   
newOrderRespType| ENUM| No| Select response format: `ACK`, `RESULT`, `FULL`  
selfTradePreventionMode| ENUM| No| The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
recvWindow| DECIMAL| No| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| Yes|   
  
**Data Source:** Matching Engine

**Response:**

Response format for `orderReports` is selected using the `newOrderRespType` parameter. The following example is for the `RESULT` response type. See [`POST /api/v3/order`](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-trade) for more examples.
    
    
    {  
        "orderListId": 1,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "lH1YDkuQKWiXVXHPSKYEIp",  
        "transactionTime": 1710485608839,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 10,  
                "clientOrderId": "44nZvqpemY7sVYgPYbvPih"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 11,  
                "clientOrderId": "NuMp0nVYnciDiFmVqfpBqK"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 10,  
                "orderListId": 1,  
                "clientOrderId": "44nZvqpemY7sVYgPYbvPih",  
                "transactTime": 1710485608839,  
                "price": "1.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "STOP_LOSS_LIMIT",  
                "side": "SELL",  
                "stopPrice": "1.00000000",  
                "workingTime": -1,  
                "icebergQty": "1.00000000",  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 11,  
                "orderListId": 1,  
                "clientOrderId": "NuMp0nVYnciDiFmVqfpBqK",  
                "transactTime": 1710485608839,  
                "price": "3.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "SELL",  
                "workingTime": 1710485608839,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

#### New Order list - OTO (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-list---oto-trade "Direct link to New Order list - OTO \(TRADE\)")
    
    
    POST /api/v3/orderList/oto  
    

Place an OTO.

  * An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.
  * The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
  * The second order is called the **pending order**. It can be any order type except for `MARKET` orders using parameter `quoteOrderQty`. The pending order is only placed on the order book when the working order gets **fully filled**.
  * If either the working order or the pending order is cancelled individually, the other order in the order list will also be canceled or expired.
  * When the order list is placed, if the working order gets **immediately fully filled** , the placement response will show the working order as `FILLED` but the pending order will still appear as `PENDING_NEW`. You need to query the status of the pending order again to see its updated status.
  * OTOs add **2 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.



**Weight:** 1

**Unfilled Order Count:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent.   
A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired.   
`listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.  
newOrderRespType| ENUM| NO| Format of the JSON response. Supported values: [Order Response Type](/docs/binance-spot-api-docs/enums#orderresponsetype)  
selfTradePreventionMode| ENUM| NO| The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
workingType| ENUM| YES| Supported values: `LIMIT`,`LIMIT_MAKER`  
workingSide| ENUM| YES| Supported values: [Order Side](/docs/binance-spot-api-docs/enums#side)  
workingClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the working order.  
Automatically generated if not sent.  
workingPrice| DECIMAL| YES|   
workingQuantity| DECIMAL| YES| Sets the quantity for the working order.  
workingIcebergQty| DECIMAL| NO| This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.  
workingTimeInForce| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
workingStrategyId| LONG| NO| Arbitrary numeric value identifying the working order within an order strategy.  
workingStrategyType| INT| NO| Arbitrary numeric value identifying the working order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
workingPegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
workingPegOffsetType| ENUM| NO|   
workingPegOffsetValue| INT| NO|   
pendingType| ENUM| YES| Supported values: [Order Types](/docs/binance-spot-api-docs/rest-api/trading-endpoints#order-type)  
Note that `MARKET` orders using `quoteOrderQty` are not supported.  
pendingSide| ENUM| YES| Supported values: [Order Side](/docs/binance-spot-api-docs/enums#side)  
pendingClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the pending order.  
Automatically generated if not sent.  
pendingPrice| DECIMAL| NO|   
pendingStopPrice| DECIMAL| NO|   
pendingTrailingDelta| DECIMAL| NO|   
pendingQuantity| DECIMAL| YES| Sets the quantity for the pending order.  
pendingIcebergQty| DECIMAL| NO| This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.  
pendingTimeInForce| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
pendingStrategyId| LONG| NO| Arbitrary numeric value identifying the pending order within an order strategy.  
pendingStrategyType| INT| NO| Arbitrary numeric value identifying the pending order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
pendingPegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingPegOffsetType| ENUM| NO|   
pendingPegOffsetValue| INT| NO|   
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
**Mandatory parameters based on`pendingType` or `workingType`**

Depending on the `pendingType` or `workingType`, some optional parameters will become mandatory.

Type| Additional mandatory parameters| Additional information  
---|---|---  
`workingType` = `LIMIT`| `workingTimeInForce`|   
`pendingType` = `LIMIT`| `pendingPrice`, `pendingTimeInForce`|   
`pendingType` = `STOP_LOSS` or `TAKE_PROFIT`| `pendingStopPrice` and/or `pendingTrailingDelta`|   
`pendingType` = `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`| `pendingPrice`, `pendingStopPrice` and/or `pendingTrailingDelta`, `pendingTimeInForce`|   
  
**Data Source:**

Matching Engine

**Response:**
    
    
    {  
        "orderListId": 0,  
        "contingencyType": "OTO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "yl2ERtcar1o25zcWtqVBTC",  
        "transactionTime": 1712289389158,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 4,  
                "clientOrderId": "Bq17mn9fP6vyCn75Jw1xya"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 5,  
                "clientOrderId": "arLFo0zGJVDE69cvGBaU0d"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 4,  
                "orderListId": 0,  
                "clientOrderId": "Bq17mn9fP6vyCn75Jw1xya",  
                "transactTime": 1712289389158,  
                "price": "1.00000000",  
                "origQty": "1.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "workingTime": 1712289389158,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 5,  
                "orderListId": 0,  
                "clientOrderId": "arLFo0zGJVDE69cvGBaU0d",  
                "transactTime": 1712289389158,  
                "price": "0.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "MARKET",  
                "side": "BUY",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses).

#### New Order list - OTOCO (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-list---otoco-trade "Direct link to New Order list - OTOCO \(TRADE\)")
    
    
    POST /api/v3/orderList/otoco  
    

Place an OTOCO.

  * An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
  * The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book. 
    * The behavior of the working order is the same as the [OTO](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-list---oto-trade).
  * OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only placed on the order book when the working order gets **fully filled**. 
    * The rules of the pending above and pending below follow the same rules as the [Order list OCO](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-list---oco-trade).
  * OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.



**Weight:** 1

**Unfilled Order Count:** 3

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent.   
A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired.   
`listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.  
newOrderRespType| ENUM| NO| Format of the JSON response. Supported values: [Order Response Type](/docs/binance-spot-api-docs/enums#orderresponsetype)  
selfTradePreventionMode| ENUM| NO| The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
workingType| ENUM| YES| Supported values: `LIMIT`, `LIMIT_MAKER`  
workingSide| ENUM| YES| Supported values: [Order side](/docs/binance-spot-api-docs/enums#side)  
workingClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the working order.  
Automatically generated if not sent.  
workingPrice| DECIMAL| YES|   
workingQuantity| DECIMAL| YES|   
workingIcebergQty| DECIMAL| NO| This can only be used if `workingTimeInForce` is `GTC` or if `workingType` is `LIMIT_MAKER`.  
workingTimeInForce| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
workingStrategyId| LONG| NO| Arbitrary numeric value identifying the working order within an order strategy.  
workingStrategyType| INT| NO| Arbitrary numeric value identifying the working order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
workingPegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
workingPegOffsetType| ENUM| NO|   
workingPegOffsetValue| INT| NO|   
pendingSide| ENUM| YES| Supported values: [Order side](/docs/binance-spot-api-docs/enums#side)  
pendingQuantity| DECIMAL| YES|   
pendingAboveType| ENUM| YES| Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
pendingAboveClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the pending above order.  
Automatically generated if not sent.  
pendingAbovePrice| DECIMAL| NO| Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.  
pendingAboveStopPrice| DECIMAL| NO| Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
pendingAboveTrailingDelta| DECIMAL| NO| See [Trailing Stop FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq)  
pendingAboveIcebergQty| DECIMAL| NO| This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`.  
pendingAboveTimeInForce| ENUM| NO|   
pendingAboveStrategyId| LONG| NO| Arbitrary numeric value identifying the pending above order within an order strategy.  
pendingAboveStrategyType| INT| NO| Arbitrary numeric value identifying the pending above order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
pendingAbovePegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingAbovePegOffsetType| ENUM| NO|   
pendingAbovePegOffsetValue| INT| NO|   
pendingBelowType| ENUM| NO| Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`  
pendingBelowClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the pending below order.  
Automatically generated if not sent.  
pendingBelowPrice| DECIMAL| NO| Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify limit price.  
pendingBelowStopPrice| DECIMAL| NO| Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, or `TAKE_PROFIT_LIMIT`.  
Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.  
pendingBelowTrailingDelta| DECIMAL| NO|   
pendingBelowIcebergQty| DECIMAL| NO| This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`.  
pendingBelowTimeInForce| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
pendingBelowStrategyId| LONG| NO| Arbitrary numeric value identifying the pending below order within an order strategy.  
pendingBelowStrategyType| INT| NO| Arbitrary numeric value identifying the pending below order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
pendingBelowPegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingBelowPegOffsetType| ENUM| NO|   
pendingBelowPegOffsetValue| INT| NO|   
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
**Mandatory parameters based on`pendingAboveType`, `pendingBelowType` or `workingType`**

Depending on the `pendingAboveType`/`pendingBelowType` or `workingType`, some optional parameters will become mandatory.

Type| Additional mandatory parameters| Additional information  
---|---|---  
`workingType` = `LIMIT`| `workingTimeInForce`|   
`pendingAboveType`= `LIMIT_MAKER`| `pendingAbovePrice`|   
`pendingAboveType` = `STOP_LOSS/TAKE_PROFIT`| `pendingAboveStopPrice` and/or `pendingAboveTrailingDelta`|   
`pendingAboveType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`| `pendingAbovePrice`, `pendingAboveStopPrice` and/or `pendingAboveTrailingDelta`, `pendingAboveTimeInForce`|   
`pendingBelowType`= `LIMIT_MAKER`| `pendingBelowPrice`|   
`pendingBelowType= STOP_LOSS/TAKE_PROFIT`| `pendingBelowStopPrice` and/or `pendingBelowTrailingDelta`|   
`pendingBelowType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`| `pendingBelowPrice`, `pendingBelowStopPrice` and/or `pendingBelowTrailingDelta`, `pendingBelowTimeInForce`|   
  
**Data Source:**

Matching Engine

**Response:**
    
    
    {  
        "orderListId": 1,  
        "contingencyType": "OTO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "RumwQpBaDctlUu5jyG5rs0",  
        "transactionTime": 1712291372842,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 6,  
                "clientOrderId": "fM9Y4m23IFJVCQmIrlUmMK"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 7,  
                "clientOrderId": "6pcQbFIzTXGZQ1e2MkGDq4"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 8,  
                "clientOrderId": "r4JMv9cwAYYUwwBZfbussx"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 6,  
                "orderListId": 1,  
                "clientOrderId": "fM9Y4m23IFJVCQmIrlUmMK",  
                "transactTime": 1712291372842,  
                "price": "1.00000000",  
                "origQty": "1.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "workingTime": 1712291372842,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 7,  
                "orderListId": 1,  
                "clientOrderId": "6pcQbFIzTXGZQ1e2MkGDq4",  
                "transactTime": 1712291372842,  
                "price": "1.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "IOC",  
                "type": "STOP_LOSS_LIMIT",  
                "side": "BUY",  
                "stopPrice": "6.00000000",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 8,  
                "orderListId": 1,  
                "clientOrderId": "r4JMv9cwAYYUwwBZfbussx",  
                "transactTime": 1712291372842,  
                "price": "3.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "BUY",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses).

#### New Order List - OPO (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-list---opo-trade "Direct link to New Order List - OPO \(TRADE\)")
    
    
    POST /api/v3/orderList/opo  
    

Place an [OPO](/docs/binance-spot-api-docs/faqs/opo).

  * OPOs add 2 orders to the EXCHANGE_MAX_NUM_ORDERS filter and MAX_NUM_ORDERS filter.



**Weight:** 1

**Unfilled Order Count:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.  
newOrderRespType| ENUM| NO| Format of the JSON response. Supported values: [Order Response Type](/docs/binance-spot-api-docs/enums#orderresponsetype)  
selfTradePreventionMode| ENUM| NO| The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
workingType| ENUM| YES| Supported values: `LIMIT`,`LIMIT_MAKER`  
workingSide| ENUM| YES| Supported values: [Order Side](/docs/binance-spot-api-docs/enums#side)  
workingClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.  
workingPrice| DECIMAL| YES|   
workingQuantity| DECIMAL| YES| Sets the quantity for the working order.  
workingIcebergQty| DECIMAL| NO| This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.  
workingTimeInForce| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
workingStrategyId| LONG| NO| Arbitrary numeric value identifying the working order within an order strategy.  
workingStrategyType| INT| NO| Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used.  
workingPegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
workingPegOffsetType| ENUM| NO|   
workingPegOffsetValue| INT| NO|   
pendingType| ENUM| YES| Supported values: [Order Types](/docs/binance-spot-api-docs/rest-api/trading-endpoints#order-type) Note that `MARKET` orders using `quoteOrderQty` are not supported.  
pendingSide| ENUM| YES| Supported values: [Order Side](/docs/binance-spot-api-docs/enums#side)  
pendingClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.  
pendingPrice| DECIMAL| NO|   
pendingStopPrice| DECIMAL| NO|   
pendingTrailingDelta| DECIMAL| NO|   
pendingIcebergQty| DECIMAL| NO| This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.  
pendingTimeInForce| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
pendingStrategyId| LONG| NO| Arbitrary numeric value identifying the pending order within an order strategy.  
pendingStrategyType| INT| NO| Arbitrary numeric value identifying the pending order strategy. Values smaller than 1000000 are reserved and cannot be used.  
pendingPegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingPegOffsetType| ENUM| NO|   
pendingPegOffsetValue| INT| NO|   
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
**Data Source** : Matching Engine

**Response:**
    
    
    {  
        "orderListId": 0,  
        "contingencyType": "OTO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "H94qCqO27P74OEiO4X8HOG",  
        "transactionTime": 1762998011671,  
        "symbol": "BTCUSDT",  
        "orders": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 2,  
                "clientOrderId": "JX6xfdjo0wysiGumfHNmPu"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 3,  
                "clientOrderId": "2ZJCY0IjOhuYIMLGN8kU8S"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 2,  
                "orderListId": 0,  
                "clientOrderId": "JX6xfdjo0wysiGumfHNmPu",  
                "transactTime": 1762998011671,  
                "price": "102264.00000000",  
                "origQty": "0.00060000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "BUY",  
                "workingTime": 1762998011671,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 3,  
                "orderListId": 0,  
                "clientOrderId": "2ZJCY0IjOhuYIMLGN8kU8S",  
                "transactTime": 1762998011671,  
                "price": "0.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "MARKET",  
                "side": "SELL",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses).

#### New Order List - OPOCO (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-list---opoco-trade "Direct link to New Order List - OPOCO \(TRADE\)")
    
    
    POST /api/v3/orderList/opoco  
    

Place an [OPOCO](/docs/binance-spot-api-docs/faqs/opo).

**Weight** : 1

**Unfilled Order Count:** 3

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.  
newOrderRespType| ENUM| NO| Format of the JSON response. Supported values: [Order Response Type](/docs/binance-spot-api-docs/enums#orderresponsetype)  
selfTradePreventionMode| ENUM| NO| The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
workingType| ENUM| YES| Supported values: `LIMIT`, `LIMIT_MAKER`  
workingSide| ENUM| YES| Supported values: [Order side](/docs/binance-spot-api-docs/enums#side)  
workingClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.  
workingPrice| DECIMAL| YES|   
workingQuantity| DECIMAL| YES|   
workingIcebergQty| DECIMAL| NO| This can only be used if `workingTimeInForce` is `GTC` or if `workingType` is `LIMIT_MAKER`.  
workingTimeInForce| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
workingStrategyId| LONG| NO| Arbitrary numeric value identifying the working order within an order strategy.  
workingStrategyType| INT| NO| Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used.  
workingPegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
workingPegOffsetType| ENUM| NO|   
workingPegOffsetValue| INT| NO|   
pendingSide| ENUM| YES| Supported values: [Order side](/docs/binance-spot-api-docs/enums#side)  
pendingAboveType| ENUM| YES| Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
pendingAboveClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.  
pendingAbovePrice| DECIMAL| NO| Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.  
pendingAboveStopPrice| DECIMAL| NO| Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
pendingAboveTrailingDelta| DECIMAL| NO| See [Trailing Stop FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq)  
pendingAboveIcebergQty| DECIMAL| NO| This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`.  
pendingAboveTimeInForce| ENUM| NO|   
pendingAboveStrategyId| LONG| NO| Arbitrary numeric value identifying the pending above order within an order strategy.  
pendingAboveStrategyType| INT| NO| Arbitrary numeric value identifying the pending above order strategy. Values smaller than 1000000 are reserved and cannot be used.  
pendingAbovePegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingAbovePegOffsetType| ENUM| NO|   
pendingAbovePegOffsetValue| INT| NO|   
pendingBelowType| ENUM| NO| Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`  
pendingBelowClientOrderId| STRING| NO| Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.  
pendingBelowPrice| DECIMAL| NO| Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify limit price  
pendingBelowStopPrice| DECIMAL| NO| Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT or TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.  
pendingBelowTrailingDelta| DECIMAL| NO|   
pendingBelowIcebergQty| DECIMAL| NO| This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`.  
pendingBelowTimeInForce| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
pendingBelowStrategyId| LONG| NO| Arbitrary numeric value identifying the pending below order within an order strategy.  
pendingBelowStrategyType| INT| NO| Arbitrary numeric value identifying the pending below order strategy. Values smaller than 1000000 are reserved and cannot be used.  
pendingBelowPegPriceType| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingBelowPegOffsetType| ENUM| NO|   
pendingBelowPegOffsetValue| INT| NO|   
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
**Response**
    
    
    {  
        "orderListId": 2,  
        "contingencyType": "OTO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "bcedxMpQG6nFrZUPQyshoL",  
        "transactionTime": 1763000506354,  
        "symbol": "BTCUSDT",  
        "orders": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 9,  
                "clientOrderId": "OLSBhMWaIlLSzZ9Zm7fnKB"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 10,  
                "clientOrderId": "mfif39yPTHsB3C0FIXznR2"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 11,  
                "clientOrderId": "yINkaXSJeoi3bU5vWMY8Z8"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 9,  
                "orderListId": 2,  
                "clientOrderId": "OLSBhMWaIlLSzZ9Zm7fnKB",  
                "transactTime": 1763000506354,  
                "price": "102496.00000000",  
                "origQty": "0.00170000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "BUY",  
                "workingTime": 1763000506354,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 10,  
                "orderListId": 2,  
                "clientOrderId": "mfif39yPTHsB3C0FIXznR2",  
                "transactTime": 1763000506354,  
                "price": "101613.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "STOP_LOSS_LIMIT",  
                "side": "SELL",  
                "stopPrice": "10100.00000000",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 11,  
                "orderListId": 2,  
                "clientOrderId": "yINkaXSJeoi3bU5vWMY8Z8",  
                "transactTime": 1763000506354,  
                "price": "104261.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "SELL",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses).

#### Cancel Order list (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#cancel-order-list-trade "Direct link to Cancel Order list \(TRADE\)")
    
    
    DELETE /api/v3/orderList  
    

Cancel an entire Order list

**Weight:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
orderListId| LONG| NO| Either `orderListId` or `listClientOrderId` must be provided  
listClientOrderId| STRING| NO| Either `orderListId` or `listClientOrderId` must be provided  
newClientOrderId| STRING| NO| Used to uniquely identify this cancel. Automatically generated by default  
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
**Notes:**

  * Canceling an individual order from an order list will cancel the entire order list.
  * If both `orderListId` and `listClientOrderId` parameters are provided, the `orderListId` is searched first, then the `listClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.



**Data Source:** Matching Engine

**Response:**
    
    
    {  
        "orderListId": 0,  
        "contingencyType": "OCO",  
        "listStatusType": "ALL_DONE",  
        "listOrderStatus": "ALL_DONE",  
        "listClientOrderId": "C3wyj4WVEktd7u9aVBRXcN",  
        "transactionTime": 1574040868128,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 2,  
                "clientOrderId": "pO9ufTiFGg3nw2fOdgeOXa"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 3,  
                "clientOrderId": "TXOvglzXuaubXAaENpaRCB"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "origClientOrderId": "pO9ufTiFGg3nw2fOdgeOXa",  
                "orderId": 2,  
                "orderListId": 0,  
                "clientOrderId": "unfWT8ig8i0uj6lPuYLez6",  
                "transactTime": 1688005070874,  
                "price": "1.00000000",  
                "origQty": "10.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "STOP_LOSS_LIMIT",  
                "side": "SELL",  
                "stopPrice": "1.00000000",  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "origClientOrderId": "TXOvglzXuaubXAaENpaRCB",  
                "orderId": 3,  
                "orderListId": 0,  
                "clientOrderId": "unfWT8ig8i0uj6lPuYLez6",  
                "transactTime": 1688005070874,  
                "price": "3.00000000",  
                "origQty": "10.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "SELL",  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

### SOR[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#sor "Direct link to SOR")

#### New order using SOR (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-using-sor-trade "Direct link to New order using SOR \(TRADE\)")
    
    
    POST /api/v3/sor/order  
    

Places an order using smart order routing (SOR).

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [SOR FAQ](/docs/binance-spot-api-docs/faqs/sor_faq) to learn more.

**Weight:** 1

**Unfilled Order Count:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES|   
type| ENUM| YES|   
timeInForce| ENUM| NO|   
quantity| DECIMAL| YES|   
price| DECIMAL| NO|   
newClientOrderId| STRING| NO| A unique id among open orders. Automatically generated if not sent.  
Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.  
strategyId| LONG| NO|   
strategyType| INT| NO| The value cannot be less than `1000000`.  
icebergQty| DECIMAL| NO| Used with `LIMIT` to create an iceberg order.  
newOrderRespType| ENUM| NO| Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`  
selfTradePreventionMode| ENUM| NO| The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes).  
recvWindow| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
timestamp| LONG| YES|   
  
**Note:** `POST /api/v3/sor/order` only supports `LIMIT` and `MARKET` orders. `quoteOrderQty` is not supported.

**Data Source:** Matching Engine

**Response:**
    
    
    {  
        "symbol": "BTCUSDT",  
        "orderId": 2,  
        "orderListId": -1,  
        "clientOrderId": "sBI1KM6nNtOfj5tccZSKly",  
        "transactTime": 1689149087774,  
        "price": "31000.00000000",  
        "origQty": "0.50000000",  
        "executedQty": "0.50000000",  
        "origQuoteOrderQty": "0.000000",  
        "cummulativeQuoteQty": "14000.00000000",  
        "status": "FILLED",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "side": "BUY",  
        "workingTime": 1689149087774,  
        "fills": [  
            {  
                "matchType": "ONE_PARTY_TRADE_REPORT",  
                "price": "28000.00000000",  
                "qty": "0.50000000",  
                "commission": "0.00000000",  
                "commissionAsset": "BTC",  
                "tradeId": -1,  
                "allocId": 0  
            }  
        ],  
        "workingFloor": "SOR",  
        "selfTradePreventionMode": "NONE",  
        "usedSor": true  
    }  
    

#### Test new order using SOR (TRADE)[​](/docs/binance-spot-api-docs/rest-api/trading-endpoints#test-new-order-using-sor-trade "Direct link to Test new order using SOR \(TRADE\)")
    
    
    POST /api/v3/sor/order/test  
    

Test new order creation and signature/recvWindow using smart order routing (SOR). Creates and validates a new order but does not send it into the matching engine.

**Weight:**

Condition| Request Weight  
---|---  
Without `computeCommissionRates`| 1  
With `computeCommissionRates`| 20  
  
**Parameters:**

In addition to all parameters accepted by [`POST /api/v3/sor/order`](/docs/binance-spot-api-docs/rest-api/trading-endpoints#new-order-using-sor-trade), the following optional parameters are also accepted:

Name| Type| Mandatory| Description  
---|---|---|---  
computeCommissionRates| BOOLEAN| NO| Default: `false`  
  
**Data Source:** Memory

**Response:**

Without `computeCommissionRates`
    
    
    {}  
    

With `computeCommissionRates`
    
    
    {  
        "standardCommissionForOrder": {   // Standard commission rates on trades from the order.  
            "maker": "0.00000112",  
            "taker": "0.00000114"  
        },  
        "taxCommissionForOrder": {        // Tax commission rates for trades from the order  
            "maker": "0.00000112",  
            "taker": "0.00000114"  
        },  
        "discount": {                     // Discount on standard commissions when paying in BNB.  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"      // Standard commission is reduced by this rate when paying commission in BNB.  
        }  
    }

---

# 交易接口

### 下单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#下单-trade "下单 \(TRADE\)的直接链接")
    
    
    POST /api/v3/order  
    

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

**权重:** 1

**未成交的订单计数:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES| 详见枚举定义：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
type| ENUM| YES| 详见枚举定义：[订单类型](/docs/zh-CN/binance-spot-api-docs/enums#ordertypes)  
timeInForce| ENUM| NO| 详见枚举定义：[生效时间](/docs/zh-CN/binance-spot-api-docs/enums_CN.md./general-endpoints#timeinforce)  
quantity| DECIMAL| NO|   
quoteOrderQty| DECIMAL| NO|   
price| DECIMAL| NO|   
newClientOrderId| STRING| NO| 用户自定义的orderid，如空缺系统会自动赋值。  
strategyId| LONG| NO|   
strategyType| INT| NO| 不能低于 `1000000`.  
stopPrice| DECIMAL| NO| 仅 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 需要此参数。  
trailingDelta| LONG| NO| 参见 [追踪止盈止损(Trailing Stop)订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)。  
icebergQty| DECIMAL| NO| 仅有限价单(包括条件限价单与限价做事单)可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。  
newOrderRespType| ENUM| NO| 指定响应类型 `ACK`, `RESULT`, or `FULL`; `MARKET` 与 `LIMIT` 订单默认为`FULL`, 其他默认为`ACK`。  
selfTradePreventionMode| ENUM| NO| 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)。  
pegPriceType| ENUM| NO| `PRIMARY_PEG` 或 `MARKET_PEG`。   
参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pegOffsetValue| INT| NO| 用于挂钩的价格水平（最大值：100）。   
参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pegOffsetType| ENUM| NO| 仅支持 `PRICE_LEVEL`。   
参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
根据 order `type`的不同，某些参数 有强制要求，具体如下:

Type| 强制要求的参数| 其他信息  
---|---|---  
`LIMIT`| `timeInForce`, `quantity`, `price`|   
`MARKET`| `quantity`| 市价买卖单可用`quantity`参数来设置`base asset`数量.  
例如：BTCUSDT 市价单，BTC 买卖数量取决于`quantity`参数.   
  
市价买卖单可用`quoteOrderQty`参数来设置`quote asset`数量. 正确的`quantity`取决于市场的流动性与`quoteOrderQty`  
例如: 市价 `BUY` BTCUSDT，单子会基于`quoteOrderQty`\- USDT 的数量，购买 BTC.  
市价 `SELL` BTCUSDT，单子会卖出 BTC 来满足`quoteOrderQty`\- USDT 的数量.  
`STOP_LOSS`| `quantity`, `stopPrice`, `trailingDelta`| 条件满足后会下`MARKET`单子. (例如：达到`stopPrice`或`trailingDelta`被启动)  
`STOP_LOSS_LIMIT`| `timeInForce`, `quantity`, `price`, `stopPrice`, `trailingDelta`|   
`TAKE_PROFIT`| `quantity`, `stopPrice`, `trailingDelta`| 条件满足后会下`MARKET`单子. (例如：达到`stopPrice`或`trailingDelta`被启动)  
`TAKE_PROFIT_LIMIT`| `timeInForce`, `quantity`, `price`, `stopPrice`, `trailingDelta`|   
`LIMIT_MAKER`| `quantity`, `price`| 订单大部分情况下与普通的限价单没有区别，但是如果在当前价格会立即吃对手单并成交则下单会被拒绝。因此使用这个订单类型可以保证订单一定是挂单方，不会成为吃单方。  
  
关于挂钩订单参数的注意事项：

  * 这些参数仅适用于 `LIMIT`， `LIMIT_MAKER`， `STOP_LOSS_LIMIT` 和 `TAKE_PROFIT_LIMIT` 订单。
  * 如果使用了 `pegPriceType`， 那么 `price` 字段将是可选的。 否则，`price` 字段依旧是必须的。
  * `pegPriceType=PRIMARY_PEG` 就是主要挂钩（`primary`），这是订单簿上与您的订单同一方向的最佳价格。
  * `pegPriceType=MARKET_PEG` 就是市场挂钩（`market`），这是订单簿上与您的订单相反方向的最佳价格。
  * 可以通过使用 `pegOffsetType` 和 `pegOffsetValue` 来获取最佳价格以外的价格水平。 这两个参数必须一起使用。



其他:

  * 任何`LIMIT`或`LIMIT_MAKER`只要填`icebergQty`参数都可以下冰上订单。
  * 冰山订单的 `timeInForce`必须设置为`GTC`。
  * `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` 与 `TAKE_PROFIT` 单子都能同时填上`trailingDelta`与`stopPrice`。
  * 填上`quoteOrderQty`的市价单不会触犯过滤器的`LOT_SIZE`限制。订单的`quantity`会尽量满足`quoteOrderQty`的数量。



条件单的触发价格必须:

  * 比下单时当前市价高: `STOP_LOSS` `BUY`, `TAKE_PROFIT` `SELL`
  * 比下单时当前市价低: `STOP_LOSS` `SELL`, `TAKE_PROFIT` `BUY`



关于 newOrderRespType的三种选择

**数据源:** 撮合引擎

**Response ACK:** 返回速度最快，不包含成交信息，信息量最少
    
    
    {  
        "symbol": "BTCUSDT",  
        "orderId": 28,  
        "orderListId": -1, // 除非此单是订单列表的一部分, 否则此值为 -1  
        "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",  
        "transactTime": 1507725176595  
    }  
    

**Response RESULT:** 返回速度居中，返回吃单成交的少量信息
    
    
    {  
        "symbol": "BTCUSDT",  
        "orderId": 28,  
        "orderListId": -1, // 除非此单是订单列表的一部分, 否则此值为 -1  
        "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",  
        "transactTime": 1507725176595,  
        "price": "1.00000000",  
        "origQty": "10.00000000",  
        "executedQty": "10.00000000",  
        "origQuoteOrderQty": "0.000000",  
        "cummulativeQuoteQty": "10.00000000",  
        "status": "FILLED",  
        "timeInForce": "GTC",  
        "type": "MARKET",  
        "side": "SELL",  
        "workingTime": 1507725176595,  
        "selfTradePreventionMode": "NONE"  
    }  
    

**Response FULL:** 返回速度最慢，返回吃单成交的详细信息
    
    
    {  
        "symbol": "BTCUSDT",  
        "orderId": 28,  
        "orderListId": -1, // 除非此单是订单列表的一部分, 否则此值为 -1  
        "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",  
        "transactTime": 1507725176595,  
        "price": "1.00000000",  
        "origQty": "10.00000000",  
        "executedQty": "10.00000000",  
        "origQuoteOrderQty": "0.000000",  
        "cummulativeQuoteQty": "10.00000000",  
        "status": "FILLED",  
        "timeInForce": "GTC",  
        "type": "MARKET",  
        "side": "SELL",  
        "workingTime": 1507725176595,  
        "selfTradePreventionMode": "NONE",  
        "fills": [  
            {  
                "price": "4000.00000000",  
                "qty": "1.00000000",  
                "commission": "4.00000000",  
                "commissionAsset": "USDT",  
                "tradeId": 56  
            },  
            {  
                "price": "3999.00000000",  
                "qty": "5.00000000",  
                "commission": "19.99500000",  
                "commissionAsset": "USDT",  
                "tradeId": 57  
            },  
            {  
                "price": "3998.00000000",  
                "qty": "2.00000000",  
                "commission": "7.99600000",  
                "commissionAsset": "USDT",  
                "tradeId": 58  
            },  
            {  
                "price": "3997.00000000",  
                "qty": "1.00000000",  
                "commission": "3.99700000",  
                "commissionAsset": "USDT",  
                "tradeId": 59  
            },  
            {  
                "price": "3995.00000000",  
                "qty": "1.00000000",  
                "commission": "3.99500000",  
                "commissionAsset": "USDT",  
                "tradeId": 60  
            }  
        ]  
    }  
    

**订单响应中的特定条件时才会出现的字段**

订单响应中的有一些字段仅在满足特定条件时才会出现。这些订单响应可以来自下订单，查询订单或取消订单，并且可以包括订单列表类型。 下面列出了这些字段：

名称| 描述| 显示的条件| 示例  
---|---|---|---  
`icebergQty`| 冰山订单的数量。| 只有在请求中发送 `icebergQty` 参数时才会出现。| `"icebergQty": "0.00000000"`  
`preventedMatchId`| 与 `symbol` 结合使用时，可用于查询因为 STP 导致订单失效的过期订单。| 只有在因为 STP 导致订单失效时可见。| `"preventedMatchId": 0`  
`preventedQuantity`| 因为 STP 导致订单失效的数量。| 只有在因为 STP 导致订单失效时可见。| `"preventedQuantity": "1.200000"`  
`stopPrice`| 用于设置逻辑订单中的触发价。| `STOP_LOSS`，`TAKE_PROFIT`，`STOP_LOSS_LIMIT` 和 `TAKE_PROFIT_LIMIT` 订单时可见。| `"stopPrice": "23500.00000000"`  
`strategyId`| 策略单ID; 用以关联此订单对应的交易策略。| 如果在请求中添加了参数，则会出现。| `"strategyId": 37463720`  
`strategyType`| 策略单类型; 用以显示此订单对应的交易策略。| 如果在请求中添加了参数，则会出现。| `"strategyType": 1000000`  
`trailingDelta`| 用以定义追踪止盈止损订单被触发的价格差。| 出现在追踪止损订单中。| `"trailingDelta": 10`  
`trailingTime`| 追踪单被激活和跟踪价格变化的时间。| 出现在追踪止损订单中。| `"trailingTime": -1`  
`usedSor`| 用于确定订单是否使用SOR的字段| 在使用SOR下单时出现| `"usedSor": true` ｜  
`workingFloor`| 用以定义订单是通过 SOR 还是由订单提交到的订单薄（order book）成交的。| 出现在使用了 SOR 的订单中。| `"workingFloor": "SOR"`  
`pegPriceType`| 挂钩价格类型| 仅用于挂钩订单| `"pegPriceType": "PRIMARY_PEG"`  
`pegOffsetType`| 挂钩价格偏移类型| 如若需要，仅用于挂钩订单| `"pegOffsetType": "PRICE_LEVEL"`  
`pegOffsetValue`| 挂钩价格偏移值| 如若需要，仅用于挂钩订单| `"pegOffsetValue": 5`  
`peggedPrice`| 订单对应的当前挂钩价格| 一旦确定，仅用于挂钩订单| `"peggedPrice": "87523.83710000"`  
  
### 测试下单接口 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#测试下单接口-trade "测试下单接口 \(TRADE\)的直接链接")
    
    
    POST /api/v3/order/test  
    

用于测试订单请求，但不会提交到撮合引擎

**权重:**

条件| 权重  
---|---  
没有 `computeCommissionRates`| 1  
有 `computeCommissionRates`| 20  
  
**参数:**

除了 [`POST /api/v3/order`](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#%E4%B8%8B%E5%8D%95-trade) 所有参数, 下面参数也支持:

参数名| 类型| 是否必需| 描述  
---|---|---|---  
computeCommissionRates| BOOLEAN| NO| 默认值: `false`   
请参阅[佣金常见问题解答](/docs/zh-CN/binance-spot-api-docs/faqs/commission_faq#test-order-diferences) 了解更多信息。  
  
**数据源:** 缓存

**响应:**

没有 `computeCommissionRates`
    
    
    {}  
    

有 `computeCommissionRates`
    
    
    {  
        "standardCommissionForOrder": {  // 订单交易的标准佣金率  
            "maker": "0.00000112",  
            "taker": "0.00000114"  
        },  
        "specialCommissionForOrder": {   // 订单交易的特殊佣金率  
            "maker": "0.05000000",  
            "taker": "0.06000000"  
        },  
        "taxCommissionForOrder": {       // 订单交易的税率  
            "maker": "0.00000112",  
            "taker": "0.00000114"  
        },  
        "discount": {                    // 以BNB支付时的标准佣金折扣。  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"     // 当用BNB支付佣金时，在标准佣金上按此比率打折  
        }  
    }  
    

### 撤销订单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#撤销订单-trade "撤销订单 \(TRADE\)的直接链接")
    
    
    DELETE /api/v3/order  
    

**权重:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO|   
origClientOrderId| STRING| NO|   
newClientOrderId| STRING| NO| 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。  
cancelRestrictions| ENUM| NO| 支持的值:   
`ONLY_NEW` \- 如果订单状态为 `NEW`，撤销将成功。  
`ONLY_PARTIALLY_FILLED` \- 如果订单状态为 `PARTIALLY_FILLED`，撤销将成功。  
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
**注意:**

  * `orderId` 与 `origClientOrderId` 必须至少发送一个。
  * 当同时提供 `orderId` 和 `origClientOrderId` 两个参数时，系统首先将会使用 `orderId` 来搜索订单。然后， 查找结果中的 `origClientOrderId` 的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。



**数据源:** 撮合引擎

**响应:**
    
    
    {  
        "symbol": "LTCBTC",  
        "orderId": 28,  
        "orderListId": -1, // 除非此单是订单列表的一部分, 否则此值为 -1  
        "origClientOrderId": "myOrder1",  
        "clientOrderId": "cancelMyOrder1",  
        "transactTime": 1507725176595,  
        "price": "1.00000000",  
        "origQty": "10.00000000",  
        "executedQty": "8.00000000",  
        "origQuoteOrderQty": "0.000000",  
        "cummulativeQuoteQty": "8.00000000",  
        "status": "CANCELED",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "side": "SELL",  
        "selfTradePreventionMode": "NONE"  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses) 部分。

  * 当仅发送 `orderId` 时,取消订单的执行(单个 Cancel 或作为 Cancel-Replace 的一部分)总是更快。发送 `origClientOrderId` 或同时发送 `orderId` \+ `origClientOrderId` 会稍慢。



**关于`cancelRestrictions`**

  * 如果 `cancelRestrictions` 值不是任何受支持的值，则错误将是：


    
    
    {  
        "code": -1145,  
        "msg": "Invalid cancelRestrictions"  
    }  
    

  * 如果订单没有通过 `cancelRestrictions` 的条件，错误将是：


    
    
    {  
        "code": -2011,  
        "msg": "Order was not canceled due to cancel restrictions."  
    }  
    

### 撤销单一交易对的所有挂单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#撤销单一交易对的所有挂单-trade "撤销单一交易对的所有挂单 \(TRADE\)的直接链接")
    
    
    DELETE /api/v3/openOrders  
    

撤销单一交易对下所有挂单。这也包括了来自订单列表的挂单。

**权重:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
**数据源:** 撮合引擎

**响应:**
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "E6APeyTJvkMvLMYMqu1KQ4",  
            "orderId": 11,  
            "orderListId": -1,  
            "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
            "transactTime": 1684804350068,  
            "price": "0.089853",  
            "origQty": "0.178622",  
            "executedQty": "0.000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "selfTradePreventionMode": "NONE"  
        },  
        {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "A3EF2HCwxgZPFMrfwbgrhv",  
            "orderId": 13,  
            "orderListId": -1,  
            "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
            "transactTime": 1684804350068,  
            "price": "0.090430",  
            "origQty": "0.178622",  
            "executedQty": "0.000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "selfTradePreventionMode": "NONE"  
        },  
        {  
            "orderListId": 1929,  
            "contingencyType": "OCO",  
            "listStatusType": "ALL_DONE",  
            "listOrderStatus": "ALL_DONE",  
            "listClientOrderId": "2inzWQdDvZLHbbAmAozX2N",  
            "transactionTime": 1585230948299,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 20,  
                    "clientOrderId": "CwOOIPHSmYywx6jZX77TdL"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 21,  
                    "clientOrderId": "461cPg51vQjV3zIMOXNz39"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "CwOOIPHSmYywx6jZX77TdL",  
                    "orderId": 20,  
                    "orderListId": 1929,  
                    "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
                    "transactTime": 1684804350068,  
                    "price": "0.668611",  
                    "origQty": "0.690354",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "BUY",  
                    "stopPrice": "0.378131",  
                    "icebergQty": "0.017083",  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "461cPg51vQjV3zIMOXNz39",  
                    "orderId": 21,  
                    "orderListId": 1929,  
                    "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
                    "transactTime": 1684804350068,  
                    "price": "0.008791",  
                    "origQty": "0.690354",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "BUY",  
                    "icebergQty": "0.639962",  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        }  
    ]  
    

### 撤消挂单再下单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#撤消挂单再下单-trade "撤消挂单再下单 \(TRADE\)的直接链接")
    
    
    POST /api/v3/order/cancelReplace  
    

  * 撤消同一交易对上的一个现有订单并重新下单。
  * 在执行撤单和下单操作之前，会先评估过滤器和订单数量。
  * 即使新订单未被尝试（即 `newOrderResult: NOT_ATTEMPTED`），未成交订单数量仍会增加1。
  * 通过此接口只能撤消订单列表中的单个订单，但结果与撤消整个订单列表相同。



**权重:** 1

**未成交的订单计数:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES|   
type| ENUM| YES|   
cancelReplaceMode| ENUM| YES| 指定类型：`STOP_ON_FAILURE` \- 如果撤消订单失败将不会继续重新下单。  
`ALLOW_FAILURE` \- 不管撤消订单是否成功都会继续重新下单。  
timeInForce| ENUM| NO|   
quantity| DECIMAL| NO|   
quoteOrderQty| DECIMAL| NO|   
price| DECIMAL| NO|   
cancelNewClientOrderId| STRING| NO| 用户自定义的id，如空缺系统会自动赋值  
cancelOrigClientOrderId| STRING| NO| 必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。   
  
当同时提供 `cancelOrderId` 和 `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。  
  
然后， 查找结果中的 `cancelOrigClientOrderId` 的值将会被用来验证订单。  
  
如果两个条件都不满足，则请求将被拒绝。  
cancelOrderId| LONG| NO| 必须提供 `cancelOrderId` 或者 `cancelOrigClientOrderId`。   
  
当同时提供 `cancelOrderId` 和 `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。  
  
然后， 查找结果中的 `cancelOrigClientOrderId` 的值将会被用来验证订单。  
  
如果两个条件都不满足，则请求将被拒绝。  
newClientOrderId| STRING| NO| 用于辨识新订单。  
strategyId| LONG| NO|   
strategyType| INT| NO| 不能低于 `1000000`。  
stopPrice| DECIMAL| NO|   
trailingDelta| LONG| NO| 参考 [追踪止盈止损(Trailing Stop)订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)  
icebergQty| DECIMAL| NO|   
newOrderRespType| ENUM| NO| 指定响应类型:   
指定响应类型 `ACK`, `RESULT`, or `FULL`; `MARKET` 与 `LIMIT` 订单默认为`FULL`， 其他默认为`ACK`。  
selfTradePreventionMode| ENUM| NO| 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)。  
cancelRestrictions| ENUM| NO| 支持的值:   
`ONLY_NEW` \- 如果订单状态为 `NEW`，撤销将成功。  
`ONLY_PARTIALLY_FILLED` \- 如果订单状态为 `PARTIALLY_FILLED`，撤销将成功。  
orderRateLimitExceededMode| ENUM| NO| 支持的值：   
  
`DO_NOTHING`（默认值）- 仅在账户未超过未成交订单频率限制时，会尝试取消订单。  
  
`CANCEL_ONLY` \- 将始终取消订单。  
pegPriceType| ENUM| NO| `PRIMARY_PEG` 或 `MARKET_PEG`。   
参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pegOffsetValue| INT| NO| 用于挂钩的价格水平（最大值：100）。   
参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pegOffsetType| ENUM| NO| 仅支持 `PRICE_LEVEL`。   
参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
如同 `POST /api/v3/order`，额外的强制参数取决于 `type` 。

响应格式根据消息的处理是成功、部分成功还是失败而有所不同。

**数据来源:** 撮合引擎

请求 | 响应  
---|---  
`cancelReplaceMode` | `orderRateLimitExceededMode` | 未成交订单数 | `cancelResult` | `newOrderResult` | `status`  
`STOP_ON_FAILURE` | `DO_NOTHING` | 在限制范围内 | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ➖ `NOT_ATTEMPTED` | `400`  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
超出限制范围 | ✅ `SUCCESS` | ✅ `SUCCESS` | N/A  
❌ `FAILURE` | ➖ `NOT_ATTEMPTED` | N/A  
✅ `SUCCESS` | ❌ `FAILURE` | N/A  
`CANCEL_ONLY` | 在限制范围内 | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ➖ `NOT_ATTEMPTED` | `400`  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
超出限制范围 | ❌ `FAILURE` | ➖ `NOT_ATTEMPTED` | `429`  
✅ `SUCCESS` | ❌ `FAILURE` | `429`  
`ALLOW_FAILURE` | `DO_NOTHING` | 在限制范围内 | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ❌ `FAILURE` | `400`  
❌ `FAILURE` | ✅ `SUCCESS` | `409`  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
超出限制范围 | ✅ `SUCCESS` | ✅ `SUCCESS` | N/A  
❌ `FAILURE` | ❌ `FAILURE` | N/A  
❌ `FAILURE` | ✅ `SUCCESS` | N/A  
✅ `SUCCESS` | ❌ `FAILURE` | N/A  
`CANCEL_ONLY` | 在限制范围内 | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ❌ `FAILURE` | `400`  
❌ `FAILURE` | ✅ `SUCCESS` | `409`  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
超出限制范围 | ✅ `SUCCESS` | ✅ `SUCCESS` | `N/A`  
❌ `FAILURE` | ❌ `FAILURE` | `400`  
❌ `FAILURE` | ✅ `SUCCESS` | N/A  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
  
**响应：账户没有超出未成交订单计数时的 Response SUCCESS**
    
    
    // 撤单和下单都成功  
    {  
        "cancelResult": "SUCCESS",  
        "newOrderResult": "SUCCESS",  
        "cancelResponse": {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "DnLo3vTAQcjha43lAZhZ0y",  
            "orderId": 9,  
            "orderListId": -1,  
            "clientOrderId": "osxN3JXAtJvKvCqGeMWMVR",  
            "transactTime": 1684804350068,  
            "price": "0.01000000",  
            "origQty": "0.000100",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL"  
        },  
        "newOrderResponse": {  
            "symbol": "BTCUSDT",  
            "orderId": 10,  
            "orderListId": -1,  
            "clientOrderId": "wOceeeOzNORyLiQfw7jd8S",  
            "transactTime": 1652928801803,  
            "price": "0.02000000",  
            "origQty": "0.040000",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "fills": []  
        }  
    }  
    

**响应：选择了`STOP_ON_FAILURE` 而且账户没有超出未成交订单计数时, 撤单出现错误**
    
    
    {  
        "code": -2022,  
        "msg": "Order cancel-replace failed.",  
        "data": {  
            "cancelResult": "FAILURE",  
            "newOrderResult": "NOT_ATTEMPTED",  
            "cancelResponse": {  
                "code": -2011,  
                "msg": "Unknown order sent."  
            },  
            "newOrderResponse": null  
        }  
    }  
    

**响应：撤单成功而且账户没有超出未成交订单计数时，下单失败**
    
    
    {  
        "code": -2021,  
        "msg": "Order cancel-replace partially failed.",  
        "data": {  
            "cancelResult": "SUCCESS",  
            "newOrderResult": "FAILURE",  
            "cancelResponse": {  
                "symbol": "BTCUSDT",  
                "origClientOrderId": "86M8erehfExV8z2RC8Zo8k",  
                "orderId": 3,  
                "orderListId": -1,  
                "clientOrderId": "G1kLo6aDv2KGNTFcjfTSFq",  
                "transactTime": 1684804350068,  
                "price": "0.006123",  
                "origQty": "10000.000000",  
                "executedQty": "0.000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.000000",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "SELL"  
            },  
            "newOrderResponse": {  
                "code": -2010,  
                "msg": "Order would immediately match and take."  
            }  
        }  
    }  
    

**响应：选择`ALLOW_FAILURE` 而且账户没有超出未成交订单计数时, 撤单出现错误**
    
    
    {  
        "code": -2021,  
        "msg": "Order cancel-replace partially failed.",  
        "data": {  
            "cancelResult": "FAILURE",  
            "newOrderResult": "SUCCESS",  
            "cancelResponse": {  
                "code": -2011,  
                "msg": "Unknown order sent."  
            },  
            "newOrderResponse": {  
                "symbol": "BTCUSDT",  
                "orderId": 11,  
                "orderListId": -1,  
                "clientOrderId": "pfojJMg6IMNDKuJqDxvoxN",  
                "transactTime": 1648540168818  
            }  
        }  
    }  
    

**响应：选择`cancelReplaceMode=ALLOW_FAILURE` 而且账户没有超出未成交订单计数时, 撤单和下单失败**
    
    
    {  
        "code": -2022,  
        "msg": "Order cancel-replace failed.",  
        "data": {  
            "cancelResult": "FAILURE",  
            "newOrderResult": "FAILURE",  
            "cancelResponse": {  
                "code": -2011,  
                "msg": "Unknown order sent."  
            },  
            "newOrderResponse": {  
                "code": -2010,  
                "msg": "Order would immediately match and take."  
            }  
        }  
    }  
    

**响应：选择`orderRateLimitExceededMode=DO_NOTHING` 而且账户超出未成交订单计数时**
    
    
    {  
        "code": -1015,  
        "msg": "Too many new orders; current limit is 1 orders per 10 SECOND."  
    }  
    

**响应：选择`orderRateLimitExceededMode=CANCEL_ONLY` 而且账户超出未成交订单计数时**
    
    
    {  
        "code": -2021,  
        "msg": "Order cancel-replace partially failed.",  
        "data": {  
            "cancelResult": "SUCCESS",  
            "newOrderResult": "FAILURE",  
            "cancelResponse": {  
                "symbol": "LTCBNB",  
                "origClientOrderId": "GKt5zzfOxRDSQLveDYCTkc",  
                "orderId": 64,  
                "orderListId": -1,  
                "clientOrderId": "loehOJF3FjoreUBDmv739R",  
                "transactTime": 1715779007228,  
                "price": "1.00",  
                "origQty": "10.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "selfTradePreventionMode": "NONE"  
            },  
            "newOrderResponse": {  
                "code": -1015,  
                "msg": "Too many new orders; current limit is 1 orders per 10 SECOND."  
            }  
        }  
    }  
    

**注意:**

  * 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses) 部分。
  * 当仅发送 `orderId` 时,取消订单的执行(单个 Cancel 或作为 Cancel-Replace 的一部分)总是更快。发送 `origClientOrderId` 或同时发送 `orderId` \+ `origClientOrderId` 会稍慢。



### 修改订单并保留优先级 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#修改订单并保留优先级-trade "修改订单并保留优先级 \(TRADE\)的直接链接")
    
    
    PUT /api/v3/order/amend/keepPriority  
    

由客户发送以减少其现有当前订单的原始数量。

这个请求将添加0个订单到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

请阅读 [保留优先权的修改订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority) 了解更多信息。

**权重:** 4

**未成交的订单计数:** 0

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderId| LONG| NO*| 需提供 `orderId` 或 `origClientOrderId`。  
origClientOrderId| STRING| NO*| 需提供 `orderId` 或 `origClientOrderId`。  
newClientOrderId| STRING| NO*| 订单在被修改后被赋予的新 client order ID。   
如果未发送则自动生成。   
可以将当前 clientOrderId 作为 `newClientOrderId` 发送来重用当前 clientOrderId 的值。  
newQty| DECIMAL| YES| 交易的新数量。 `newQty` 必须大于0, 但是必须比订单的原始数量小。  
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
**数据源:** 撮合引擎

**来自单个订单的响应：**
    
    
    {  
        "transactTime": 1741926410255,  
        "executionId": 75,  
        "amendedOrder": {  
            "symbol": "BTCUSDT",  
            "orderId": 33,  
            "orderListId": -1,  
            "origClientOrderId": "5xrgbMyg6z36NzBn2pbT8H",  
            "clientOrderId": "PFaq6hIHxqFENGfdtn4J6Q",  
            "price": "6.00000000",  
            "qty": "5.00000000",  
            "executedQty": "0.00000000",  
            "preventedQty": "0.00000000",  
            "quoteOrderQty": "0.00000000",  
            "cumulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL",  
            "workingTime": 1741926410242,  
            "selfTradePreventionMode": "NONE"  
        }  
    }  
    

**来自订单列表中单个订单的响应：**
    
    
    {  
        "transactTime": 1741669661670,  
        "executionId": 22,  
        "amendedOrder": {  
            "symbol": "BTCUSDT",  
            "orderId": 9,  
            "orderListId": 1,  
            "origClientOrderId": "W0fJ9fiLKHOJutovPK3oJp",  
            "clientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi",  
            "price": "0.00000000",  
            "qty": "4.00000000",  
            "executedQty": "0.00000000",  
            "preventedQty": "0.00000000",  
            "quoteOrderQty": "0.00000000",  
            "cumulativeQuoteQty": "0.00000000",  
            "status": "PENDING_NEW",  
            "timeInForce": "GTC",  
            "type": "MARKET",  
            "side": "BUY",  
            "selfTradePreventionMode": "NONE"  
        },  
        "listStatus": {  
            "orderListId": 1,  
            "contingencyType": "OTO",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "AT7FTxZXylVSwRoZs52mt3",  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 8,  
                    "clientOrderId": "GkwwHZUUbFtZOoH1YsZk9Q"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 9,  
                    "clientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi"  
                }  
            ]  
        }  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses) 部分。

### 订单列表（Order lists）[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#订单列表order-lists "订单列表（Order lists）的直接链接")

#### 发送新 OCO 订单 - 已弃用 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#发送新-oco-订单---已弃用-trade "发送新 OCO 订单 - 已弃用 \(TRADE\)的直接链接")
    
    
    POST /api/v3/order/oco  
    

**权重:** 1

**未成交的订单计数:** 2

发送新的 OCO。

  * 价格限制： 
    * `SELL`： Limit price > 最后交易价格 > stop Price
    * `BUY`： Limit price < 最后交易价格 < stop Price
  * 数量限制： 
    * 两条腿的数量必须相同。
    * 不过， `冰山` 交易的数量不一定相同
  * `OCO` 将**2个订单** 添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。



**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| 整个orderList的唯一ID  
side| ENUM| YES| 详见枚举定义：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
quantity| DECIMAL| YES|   
limitClientOrderId| STRING| NO| 限价单的唯一ID  
price| DECIMAL| YES|   
limitStrategyId| LONG| NO|   
limitStrategyType| INT| NO| 不能低于 `1000000`  
limitIcebergQty| DECIMAL| NO|   
trailingDelta| LONG| NO|   
stopClientOrderId| STRING| NO| 止损/止损限价单的唯一ID  
stopPrice| DECIMAL| YES|   
stopStrategyId| LONG| NO|   
stopStrategyType| INT| NO| 不能低于 `1000000`  
stopLimitPrice| DECIMAL| NO| 如果提供，须配合提交`stopLimitTimeInForce`  
stopIcebergQty| DECIMAL| NO|   
stopLimitTimeInForce| ENUM| NO| 有效值 `GTC`/`FOK`/`IOC`  
newOrderRespType| ENUM| NO| 详见枚举定义：[订单返回类型](/docs/zh-CN/binance-spot-api-docs/enums#orderresponsetype)  
selfTradePreventionMode| ENUM| NO| 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)。  
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
**数据源:** 撮合引擎

**响应**
    
    
    {  
        "orderListId": 0,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "JYVpp3F0f5CAG15DhtrqLp",  
        "transactionTime": 1563417480525,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 2,  
                "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 3,  
                "clientOrderId": "xTXKaGYd4bluPVp78IVRvl"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 2,  
                "orderListId": 0,  
                "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos",  
                "transactTime": 1563417480525,  
                "price": "0.000000",  
                "origQty": "0.624363",  
                "executedQty": "0.000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "STOP_LOSS",  
                "side": "BUY",  
                "stopPrice": "0.960664",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 3,  
                "orderListId": 0,  
                "clientOrderId": "xTXKaGYd4bluPVp78IVRvl",  
                "transactTime": 1563417480525,  
                "price": "0.036435",  
                "origQty": "0.624363",  
                "executedQty": "0.000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "BUY",  
                "workingTime": 1563417480525,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

#### 新订单列表 - OCO (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#新订单列表---oco-trade "新订单列表 - OCO \(TRADE\)的直接链接")
    
    
    POST /api/v3/orderList/oco  
    

发送新 one-cancels-the-other (OCO) 订单，激活其中一个订单会立即取消另一个订单。

  * OCO 包含了两个订单，分别被称为 **上方订单** 和 **下方订单** 。
  * 其中一个订单必须是 `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` 订单，另一个订单必须是 `STOP_LOSS` 或 `STOP_LOSS_LIMIT` 订单。
  * 针对价格限制： 
    * 如果 OCO 订单方向是 `SELL`： 
      * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
      * `TAKE_PROFIT` `stopPrice` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    * 如果 OCO 订单方向是 `BUY`： 
      * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` < 最后交易价格 < `stopPrice`
      * `TAKE_PROFIT` `stopPrice` < 最后交易价格 < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    * OCO 会添加 **2个订单** 到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。



**权重:** 1

**未成交的订单计数:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| Yes|   
listClientOrderId| STRING| No| 整个 OCO order list 的唯一ID。 如果未发送则自动生成。   
仅当前一个订单已填满或完全过期时，才会接受具有相同的`listClientOrderId`。   
`listClientOrderId` 与 `aboveClientOrderId` 和 `belowCLientOrderId` 不同。  
side| ENUM| Yes| 订单方向：`BUY` or `SELL`  
quantity| DECIMAL| Yes| 两个订单的数量。  
aboveType| ENUM| Yes| 支持值：`STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`。  
aboveClientOrderId| STRING| No| 上方订单的唯一ID。 如果未发送则自动生成。  
aboveIcebergQty| LONG| No| 请注意，只有当 `aboveTimeInForce` 为 `GTC` 时才能使用。  
abovePrice| DECIMAL| No| 当 `aboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。  
aboveStopPrice| DECIMAL| No| 如果 `aboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。  
必须指定 `aboveStopPrice` 或 `aboveTrailingDelta` 或两者。  
aboveTrailingDelta| LONG| No| 请看 [追踪止盈止损(Trailing Stop)订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)。  
aboveTimeInForce| ENUM| No| 如果 `aboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。  
aboveStrategyId| LONG| No| 订单策略中上方订单的 ID。  
aboveStrategyType| INT| No| 上方订单策略的任意数值。  
小于 `1000000` 的值被保留，无法使用。  
abovePegPriceType| ENUM| NO| 参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
abovePegOffsetType| ENUM| NO|   
abovePegOffsetValue| INT| NO|   
belowType| ENUM| Yes| 支持值：`STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`。  
belowClientOrderId| STRING| No|   
belowIcebergQty| LONG| No| 请注意，只有当 `belowTimeInForce` 为 `GTC` 时才能使用。  
belowPrice| DECIMAL| No| 当 `belowType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。  
belowStopPrice| DECIMAL| No| 如果 `belowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。  
必须指定 `belowStopPrice` 或 `belowTrailingDelta` 或两者。  
belowTrailingDelta| LONG| No| 请看 [追踪止盈止损(Trailing Stop)订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)。  
belowTimeInForce| ENUM| No| 如果`belowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必须配合提交的值。  
belowStrategyId| LONG| No| 订单策略中下方订单的 ID。  
belowStrategyType| INT| No| 下方订单策略的任意数值。  
小于 `1000000` 的值被保留，无法使用。  
belowPegPriceType| ENUM| NO| 参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
belowPegOffsetType| ENUM| NO|   
belowPegOffsetValue| INT| NO|   
newOrderRespType| ENUM| No| 响应格式可选值: `ACK`, `RESULT`, `FULL`。  
selfTradePreventionMode| ENUM| No| 允许的 ENUM 取决于交易对上的配置。 支持值：[STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)。  
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| Yes|   
  
**数据源:** 撮合引擎

**响应:**

使用 `newOrderRespType` 参数来选择 `orderReports` 的响应格式。以下示例适用于 `RESULT` 响应类型。 请参阅 [`POST /api/v3/order`](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#%E4%B8%8B%E5%8D%95-trade)了解更多 `orderReports` 的响应类型。
    
    
    {  
        "orderListId": 1,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "lH1YDkuQKWiXVXHPSKYEIp",  
        "transactionTime": 1710485608839,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 10,  
                "clientOrderId": "44nZvqpemY7sVYgPYbvPih"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 11,  
                "clientOrderId": "NuMp0nVYnciDiFmVqfpBqK"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 10,  
                "orderListId": 1,  
                "clientOrderId": "44nZvqpemY7sVYgPYbvPih",  
                "transactTime": 1710485608839,  
                "price": "1.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "STOP_LOSS_LIMIT",  
                "side": "SELL",  
                "stopPrice": "1.00000000",  
                "workingTime": -1,  
                "icebergQty": "1.00000000",  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 11,  
                "orderListId": 1,  
                "clientOrderId": "NuMp0nVYnciDiFmVqfpBqK",  
                "transactTime": 1710485608839,  
                "price": "3.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "SELL",  
                "workingTime": 1710485608839,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

#### 新订单列表 - OTO (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#新订单列表---oto-trade "新订单列表 - OTO \(TRADE\)的直接链接")
    
    
    POST /api/v3/orderList/oto  
    

发送一个新的 OTO 订单。

  * 一个 OTO 订单（One-Triggers-the-Other）是一个包含了两个订单的订单列表.
  * 第一个订单被称为**生效订单** ，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。
  * 第二个订单被称为**待处理订单** 。它可以是任何订单类型，但不包括使用参数 `quoteOrderQty` 的 `MARKET` 订单。只有当生效订单**完全成交** 时，待处理订单才会被自动下单。
  * 如果生效订单或者待处理订单中的任意一个被单独取消，订单列表中剩余的那个订单也会被随之取消或过期。
  * 如果生效订单在下订单列表后**立即完全成交** ，则可能会得到订单响应。其中，生效订单的状态为 `FILLED` ，但待处理订单的状态为 `PENDING_NEW`。针对这类情况，如果需要检查当前状态，您可以查询相关的待处理订单。
  * `OTO` 订单将**2 个订单** 添加到 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。



**权重:** 1

**未成交的订单计数:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| 整个订单列表的唯一ID。 如果未发送则自动生成。   
仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。   
`listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。  
newOrderRespType| ENUM| NO| 用于设置JSON响应的格式。 支持的数值： [订单返回类型](/docs/zh-CN/binance-spot-api-docs/enums#orderresponsetype)  
selfTradePreventionMode| ENUM| NO| 允许的数值取决于交易对上的配置。参考 [STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
workingType| ENUM| YES| 支持的数值： `LIMIT`， `LIMIT_MAKER`  
workingSide| ENUM| YES| 支持的数值： [订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
workingClientOrderId| STRING| NO| 用于标识生效订单的唯一ID。   
如果未发送则自动生成。  
workingPrice| DECIMAL| YES|   
workingQuantity| DECIMAL| YES| 用于设置生效订单的数量。  
workingIcebergQty| DECIMAL| NO| 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。  
workingTimeInForce| ENUM| NO| 支持的数值： [生效时间](/docs/zh-CN/binance-spot-api-docs/enums_CN.md./general-endpoints#timeinforce)  
workingStrategyId| LONG| NO| 订单策略中用于标识生效订单的 ID。  
workingStrategyType| INT| NO| 用于标识生效订单策略的任意数值。  
小于 `1000000` 的值被保留，无法使用。  
pendingType| ENUM| YES| 支持的数值： [订单类型](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#order-type)  
请注意，系统不支持使用 `quoteOrderQty` 的 `MARKET` 订单。  
workingPegPriceType| ENUM| NO| 参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
workingPegOffsetType| ENUM| NO|   
workingPegOffsetValue| INT| NO|   
pendingSide| ENUM| YES| 支持的数值： [订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
pendingClientOrderId| STRING| NO| 用于标识待处理订单的唯一ID。   
如果未发送则自动生成。  
pendingPrice| DECIMAL| NO|   
pendingStopPrice| DECIMAL| NO|   
pendingTrailingDelta| DECIMAL| NO|   
pendingQuantity| DECIMAL| YES| 用于设置待处理订单的数量。  
pendingIcebergQty| DECIMAL| NO| 只有当 `pendingTimeInForce` 为 `GTC` 或者当 `pendingType` 为 `LIMIT_MAKER` 时才能使用。  
pendingTimeInForce| ENUM| NO| 支持的数值： [生效时间](/docs/zh-CN/binance-spot-api-docs/enums_CN.md./general-endpoints#timeinforce)  
pendingStrategyId| LONG| NO| 订单策略中用于标识待处理订单的 ID。  
pendingStrategyType| INT| NO| 用于标识待处理订单策略的任意数值。   
小于 `1000000` 的值被保留，无法使用。  
pendingPegPriceType| ENUM| NO| 参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingPegOffsetType| ENUM| NO|   
pendingPegOffsetValue| INT| NO|   
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
**根据`pendingType` 或者 `workingType` 的不同值，对于某些参数的强制要求**

根据 `pendingType` 或者`workingType`的不同值，对于某些可选参数有强制要求，具体如下：

类型| 强制要求的参数| 其他信息  
---|---|---  
`workingType` = `LIMIT`| `workingTimeInForce`|   
`pendingType` = `LIMIT`| `pendingPrice`， `pendingTimeInForce`|   
`pendingType` = `STOP_LOSS` 或 `TAKE_PROFIT`| `pendingStopPrice` 与/或 `pendingTrailingDelta`|   
`pendingType` = `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`| `pendingPrice`， `pendingStopPrice` 与/或 `pendingTrailingDelta`， `pendingTimeInForce`|   
  
**数据源:** 撮合引擎

**响应:**
    
    
    {  
        "orderListId": 0,  
        "contingencyType": "OTO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "yl2ERtcar1o25zcWtqVBTC",  
        "transactionTime": 1712289389158,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 4,  
                "clientOrderId": "Bq17mn9fP6vyCn75Jw1xya"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 5,  
                "clientOrderId": "arLFo0zGJVDE69cvGBaU0d"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 4,  
                "orderListId": 0,  
                "clientOrderId": "Bq17mn9fP6vyCn75Jw1xya",  
                "transactTime": 1712289389158,  
                "price": "1.00000000",  
                "origQty": "1.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "workingTime": 1712289389158,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 5,  
                "orderListId": 0,  
                "clientOrderId": "arLFo0zGJVDE69cvGBaU0d",  
                "transactTime": 1712289389158,  
                "price": "0.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "MARKET",  
                "side": "BUY",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses) 部分。

#### 新订单列表 - OTOCO (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#新订单列表---otoco-trade "新订单列表 - OTOCO \(TRADE\)的直接链接")
    
    
    POST /api/v3/orderList/otoco  
    

发送一个新的 OTOCO 订单。

  * 一个 OTOCO 订单（One-Triggers-One-Cancels-the-Other）是一个包含了三个订单的订单列表。
  * 第一个订单被称为**生效订单** ，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。 
    * 生效订单的行为与此一致 [OTO](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#new-order-list---oto-trade)
  * 一个OTOCO订单有两个待处理订单（pending above 和 pending below），它们构成了一个 OCO 订单列表。只有当生效订单**完全成交** 时，待处理订单们才会被自动下单。 
    * 待处理上方(pending above)订单和待处理下方(pending below)订单都遵循与 OCO 订单列表相同的规则 [Order List OCO](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#new-order-list---oco-trade)。
  * `OTOCO` 在 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器的基础上添加**3个订单** 。



**权重:** 1

**未成交的订单计数:** 3

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| 整个订单列表的唯一ID。 如果未发送则自动生成。   
仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。   
`listClientOrderId` 与 `workingClientOrderId`， `pendingAboveClientOrderId` 以及 `pendingBelowClientOrderId` 不同。  
newOrderRespType| ENUM| NO| 用于设置JSON响应的格式。 支持的数值： [订单返回类型](/docs/zh-CN/binance-spot-api-docs/enums#orderresponsetype)  
selfTradePreventionMode| ENUM| NO| 允许的数值取决于交易对上的配置。参考 [STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
workingType| ENUM| YES| 支持的数值： `LIMIT`， `LIMIT_MAKER`  
workingSide| ENUM| YES| 支持的数值： [订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
workingClientOrderId| STRING| NO| 用于标识生效订单的唯一ID。   
如果未发送则自动生成。  
workingPrice| DECIMAL| YES|   
workingQuantity| DECIMAL| YES|   
workingIcebergQty| DECIMAL| NO| 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。  
workingTimeInForce| ENUM| NO| 支持的数值： [生效时间](/docs/zh-CN/binance-spot-api-docs/enums_CN.md./general-endpoints#timeinforce)  
workingStrategyId| LONG| NO| 订单策略中用于标识生效订单的 ID。  
workingStrategyType| INT| NO| 用于标识生效订单策略的任意数值。  
小于 `1000000` 的值被保留，无法使用。  
workingPegPriceType| ENUM| NO| 参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
workingPegOffsetType| ENUM| NO|   
workingPegOffsetValue| INT| NO|   
pendingSide| ENUM| YES| 支持的数值： [订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
pendingQuantity| DECIMAL| YES|   
pendingAboveType| ENUM| YES| 支持的数值： `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
pendingAboveClientOrderId| STRING| NO| 用于标识待处理上方订单的唯一ID。   
如果未发送则自动生成。  
pendingAbovePrice| DECIMAL| NO| 当 `pendingAboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。  
pendingAboveStopPrice| DECIMAL| NO| 如果 `pendingAboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。  
pendingAboveTrailingDelta| DECIMAL| NO| 参见 [追踪止盈止损(Trailing Stop)订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)  
pendingAboveIcebergQty| DECIMAL| NO| 只有当 `pendingAboveTimeInForce` 为 `GTC` 时才能使用。  
pendingAboveTimeInForce| ENUM| NO|   
pendingAboveStrategyId| LONG| NO| 订单策略中用于标识待处理上方订单的 ID。  
pendingAboveStrategyType| INT| NO| 用于标识待处理上方订单策略的任意数值。   
小于 `1000000` 的值被保留，无法使用。  
pendingAbovePegPriceType| ENUM| NO| 参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingAbovePegOffsetType| ENUM| NO|   
pendingAbovePegOffsetValue| INT| NO|   
pendingBelowType| ENUM| NO| 支持的数值： `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
pendingBelowClientOrderId| STRING| NO| 用于标识待处理下方订单的唯一ID。   
如果未发送则自动生成。  
pendingBelowPrice| DECIMAL| NO| 当 `pendingBelowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。  
pendingBelowStopPrice| DECIMAL| NO| 如果 `pendingBelowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。  
必须指定 `pendingBelowStopPrice` 或 `pendingBelowTrailingDelta` 或两者。  
pendingBelowTrailingDelta| DECIMAL| NO|   
pendingBelowIcebergQty| DECIMAL| NO| 只有当 `pendingBelowTimeInForce` 为 `GTC` 时才能使用。  
pendingBelowTimeInForce| ENUM| NO|   
pendingBelowStrategyId| LONG| NO| 订单策略中用于标识待处理下方订单的 ID。  
pendingBelowStrategyType| INT| NO| 用于标识待处理下方订单策略的任意数值。   
小于 `1000000` 的值被保留，无法使用。  
pendingBelowPegPriceType| ENUM| NO| 参阅 [关于挂钩订单参数的注意事项](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingBelowPegOffsetType| ENUM| NO|   
pendingBelowPegOffsetValue| INT| NO|   
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
**根据`pendingAboveType`， `pendingBelowType` 或者`workingType`的不同值，对于某些参数的强制要求**

根据 `pendingAboveType`， `pendingBelowType` 或者`workingType`的不同值，对于某些可选参数有强制要求，具体如下：

类型| 强制要求的参数| 其他信息  
---|---|---  
`workingType` = `LIMIT`| `workingTimeInForce`|   
`pendingAboveType` = `LIMIT_MAKER`| `pendingAbovePrice`|   
`pendingAboveType` = `STOP_LOSS/TAKE_PROFIT`| `pendingAboveStopPrice` 与/或 `pendingAboveTrailingDelta`|   
`pendingAboveType` = `STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`| `pendingAbovePrice`， `pendingAboveStopPrice` 与/或 `pendingAboveTrailingDelta`， `pendingAboveTimeInForce`|   
`pendingBelowType` = `LIMIT_MAKER`| `pendingBelowPrice`|   
`pendingBelowType` = `STOP_LOSS/TAKE_PROFIT`| `pendingBelowStopPrice` 与/或 `pendingBelowTrailingDelta`|   
`pendingBelowType` = `STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`| `pendingBelowPrice`， `pendingBelowStopPrice` 与/或 `pendingBelowTrailingDelta`， `pendingBelowTimeInForce`|   
  
**数据源:** 撮合引擎

**响应:**
    
    
    {  
        "orderListId": 1,  
        "contingencyType": "OTO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "RumwQpBaDctlUu5jyG5rs0",  
        "transactionTime": 1712291372842,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 6,  
                "clientOrderId": "fM9Y4m23IFJVCQmIrlUmMK"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 7,  
                "clientOrderId": "6pcQbFIzTXGZQ1e2MkGDq4"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 8,  
                "clientOrderId": "r4JMv9cwAYYUwwBZfbussx"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 6,  
                "orderListId": 1,  
                "clientOrderId": "fM9Y4m23IFJVCQmIrlUmMK",  
                "transactTime": 1712291372842,  
                "price": "1.00000000",  
                "origQty": "1.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "workingTime": 1712291372842,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 7,  
                "orderListId": 1,  
                "clientOrderId": "6pcQbFIzTXGZQ1e2MkGDq4",  
                "transactTime": 1712291372842,  
                "price": "1.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "IOC",  
                "type": "STOP_LOSS_LIMIT",  
                "side": "BUY",  
                "stopPrice": "6.00000000",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 8,  
                "orderListId": 1,  
                "clientOrderId": "r4JMv9cwAYYUwwBZfbussx",  
                "transactTime": 1712291372842,  
                "price": "3.00000000",  
                "origQty": "5.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "BUY",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses) 部分。

#### 新订单列表 - OPO（TRADE）[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#新订单列表---opotrade "新订单列表 - OPO（TRADE）的直接链接")
    
    
    POST /api/v3/orderList/opo  
    

发送一个新的 [OPO](/docs/zh-CN/binance-spot-api-docs/faqs/opo) 订单。

  * OPO 会向 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中添加 2 个订单。



**权重:** 1

**未成交订单计数:** 2

**参数:**

名称| 类型| 必填| 描述  
---|---|---|---  
symbol| STRING| YES|   
listClientOrderId| STRING| NO| 订单列表中的唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期后，才接受新的同一 `listClientOrderId` 的订单列表。`listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。  
newOrderRespType| ENUM| NO| JSON 响应格式。支持的数值：[订单返回类型](/docs/zh-CN/binance-spot-api-docs/enums#orderresponsetype)  
selfTradePreventionMode| ENUM| NO| 允许的数值取决于交易对的配置。支持的数值：[STP模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
workingType| ENUM| YES| 支持的数值：`LIMIT`，`LIMIT_MAKER`  
workingSide| ENUM| YES| 支持的数值：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
workingClientOrderId| STRING| NO| 生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。  
workingPrice| DECIMAL| YES| 生效订单价格  
workingQuantity| DECIMAL| YES| 设置生效订单的数量  
workingIcebergQty| DECIMAL| NO| 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用  
workingTimeInForce| ENUM| NO| 支持的数值：[生效时间](/docs/zh-CN/binance-spot-api-docs/enums_CN.md./general-endpoints#timeinforce)  
workingStrategyId| LONG| NO| 用于标识订单策略中生效订单的任意数字值  
workingStrategyType| INT| NO| 用于标识生效订单策略的任意数字值。小于 1000000 的值为保留值，不能使用。  
workingPegPriceType| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
workingPegOffsetType| ENUM| NO|   
workingPegOffsetValue| INT| NO|   
pendingType| ENUM| YES| 支持的数值：[订单类型](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#order-type)。注意，不支持使用 `quoteOrderQty` 的 `MARKET` 订单。  
pendingSide| ENUM| YES| 支持的数值：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
pendingClientOrderId| STRING| NO| 待执行订单中挂单的任意唯一 ID。如果未发送，则自动生成。  
pendingPrice| DECIMAL| NO| 待执行订单价格  
pendingStopPrice| DECIMAL| NO| 待执行订单止损价格  
pendingTrailingDelta| DECIMAL| NO| 待执行订单跟踪止损差值  
pendingIcebergQty| DECIMAL| NO| 仅当 `pendingTimeInForce` 为 `GTC` 或 `pendingType` 为 `LIMIT_MAKER` 时可用  
pendingTimeInForce| ENUM| NO| 支持的数值：[生效时间](/docs/zh-CN/binance-spot-api-docs/enums_CN.md./general-endpoints#timeinforce)  
pendingStrategyId| LONG| NO| 用于标识订单策略中待执行订单的任意数字值  
pendingStrategyType| INT| NO| 用于标识待执行订单策略的任意数字值。小于 1000000 的值为保留值，不能使用。  
pendingPegPriceType| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingPegOffsetType| ENUM| NO|   
pendingPegOffsetValue| INT| NO|   
recvWindow| DECIMAL| NO| 该值不能大于 `60000`。支持最多三位小数精度（例如 6000.346），以便指定微秒。  
timestamp| LONG| YES| 时间戳  
  
**数据来源** ：撮合引擎

**响应示例:**
    
    
    {  
        "orderListId": 0,  
        "contingencyType": "OTO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "H94qCqO27P74OEiO4X8HOG",  
        "transactionTime": 1762998011671,  
        "symbol": "BTCUSDT",  
        "orders": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 2,  
                "clientOrderId": "JX6xfdjo0wysiGumfHNmPu"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 3,  
                "clientOrderId": "2ZJCY0IjOhuYIMLGN8kU8S"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 2,  
                "orderListId": 0,  
                "clientOrderId": "JX6xfdjo0wysiGumfHNmPu",  
                "transactTime": 1762998011671,  
                "price": "102264.00000000",  
                "origQty": "0.00060000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "BUY",  
                "workingTime": 1762998011671,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 3,  
                "orderListId": 0,  
                "clientOrderId": "2ZJCY0IjOhuYIMLGN8kU8S",  
                "transactTime": 1762998011671,  
                "price": "0.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "MARKET",  
                "side": "SELL",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses) 部分。

#### 新订单列表 - OPOCO (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#新订单列表---opoco-trade "新订单列表 - OPOCO \(TRADE\)的直接链接")
    
    
    POST /api/v3/orderList/opoco  
    

发送一个 [OPOCO](/docs/zh-CN/binance-spot-api-docs/https://github.com/binance/binance-spot-api-docs/blob/master/faqs/opo) 订单。

**权重** : 1

**未成交订单计数:** 3

**参数:**

名称| 类型| 必填| 描述  
---|---|---|---  
symbol| STRING| YES| 交易对符号  
listClientOrderId| STRING| NO| 订单列表中的任意唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期时，才接受新的同一 `listClientOrderId` 的订单列表。`listClientOrderId` 与 `workingClientOrderId`、`pendingAboveClientOrderId` 和 `pendingBelowClientOrderId` 不同。  
newOrderRespType| ENUM| NO| JSON 响应格式。支持的数值：[订单返回类型](/docs/zh-CN/binance-spot-api-docs/enums#orderresponsetype)  
selfTradePreventionMode| ENUM| NO| 允许的值取决于交易对的配置。支持的数值：[STP模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
workingType| ENUM| YES| 支持的数值：`LIMIT`，`LIMIT_MAKER`  
workingSide| ENUM| YES| 支持的数值：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
workingClientOrderId| STRING| NO| 生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。  
workingPrice| DECIMAL| YES| 生效订单价格  
workingQuantity| DECIMAL| YES| 生效订单数量  
workingIcebergQty| DECIMAL| NO| 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用  
workingTimeInForce| ENUM| NO| 支持的数值：[生效时间](/docs/zh-CN/binance-spot-api-docs/enums_CN.md./general-endpoints#timeinforce)  
workingStrategyId| LONG| NO| 用于标识订单策略中生效订单的任意数字值  
workingStrategyType| INT| NO| 用于标识生效订单策略的任意数字值。小于 1000000 的值为保留值，不能使用。  
workingPegPriceType| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
workingPegOffsetType| ENUM| NO|   
workingPegOffsetValue| INT| NO|   
pendingSide| ENUM| YES| 支持的数值：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
pendingAboveType| ENUM| YES| 支持的数值：`STOP_LOSS_LIMIT`，`STOP_LOSS`，`LIMIT_MAKER`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`  
pendingAboveClientOrderId| STRING| NO| 待执行“上方”订单中开放订单的任意唯一 ID。如果未发送，则自动生成。  
pendingAbovePrice| DECIMAL| NO| 当 `pendingAboveType` 为 `STOP_LOSS_LIMIT`、`LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。  
pendingAboveStopPrice| DECIMAL| NO| 当 `pendingAboveType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT`、`TAKE_PROFIT_LIMIT` 时可用。  
pendingAboveTrailingDelta| DECIMAL| NO| 详见 [追踪止盈止损常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)  
pendingAboveIcebergQty| DECIMAL| NO| 仅当 `pendingAboveTimeInForce` 为 `GTC` 或 `pendingAboveType` 为 `LIMIT_MAKER` 时可用。  
pendingAboveTimeInForce| ENUM| NO|   
pendingAboveStrategyId| LONG| NO| 用于标识订单策略中待执行上方订单的任意数字值。  
pendingAboveStrategyType| INT| NO| 用于标识待执行上方订单策略的任意数字值。小于 1000000 的值为保留值，不能使用。  
pendingAbovePegPriceType| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingAbovePegOffsetType| ENUM| NO|   
pendingAbovePegOffsetValue| INT| NO|   
pendingBelowType| ENUM| NO| 支持的数值：`STOP_LOSS`，`STOP_LOSS_LIMIT`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`  
pendingBelowClientOrderId| STRING| NO| 待执行“下方”订单中开放订单的任意唯一 ID。如果未发送，则自动生成。  
pendingBelowPrice| DECIMAL| NO| 当 `pendingBelowType` 为 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。  
pendingBelowStopPrice| DECIMAL| NO| 当 `pendingBelowType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 时可用。`pendingBelowStopPrice`、`pendingBelowTrailingDelta` 或两者之一必须被指定。  
pendingBelowTrailingDelta| DECIMAL| NO|   
pendingBelowIcebergQty| DECIMAL| NO| 仅当 `pendingBelowTimeInForce` 为 `GTC` 或 `pendingBelowType` 为 `LIMIT_MAKER` 时可用。  
pendingBelowTimeInForce| ENUM| NO| 支持的数值：[生效时间](/docs/zh-CN/binance-spot-api-docs/enums_CN.md./general-endpoints#timeinforce)  
pendingBelowStrategyId| LONG| NO| 用于标识订单策略中待执行下方订单的任意数字值。  
pendingBelowStrategyType| INT| NO| 用于标识待执行下方订单策略的任意数字值。小于 1000000 为保留值，不能使用。  
pendingBelowPegPriceType| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#pegged-orders-info)  
pendingBelowPegOffsetType| ENUM| NO|   
pendingBelowPegOffsetValue| INT| NO|   
recvWindow| DECIMAL| NO| 该值不能大于 `60000`。支持最多三位小数精度（例如 6000.346），以便指定微秒。  
timestamp| LONG| YES| 时间戳  
  
**响应:**
    
    
    {  
        "orderListId": 2,  
        "contingencyType": "OTO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "bcedxMpQG6nFrZUPQyshoL",  
        "transactionTime": 1763000506354,  
        "symbol": "BTCUSDT",  
        "orders": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 9,  
                "clientOrderId": "OLSBhMWaIlLSzZ9Zm7fnKB"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 10,  
                "clientOrderId": "mfif39yPTHsB3C0FIXznR2"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 11,  
                "clientOrderId": "yINkaXSJeoi3bU5vWMY8Z8"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 9,  
                "orderListId": 2,  
                "clientOrderId": "OLSBhMWaIlLSzZ9Zm7fnKB",  
                "transactTime": 1763000506354,  
                "price": "102496.00000000",  
                "origQty": "0.00170000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "BUY",  
                "workingTime": 1763000506354,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 10,  
                "orderListId": 2,  
                "clientOrderId": "mfif39yPTHsB3C0FIXznR2",  
                "transactTime": 1763000506354,  
                "price": "101613.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "STOP_LOSS_LIMIT",  
                "side": "SELL",  
                "stopPrice": "10100.00000000",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "symbol": "BTCUSDT",  
                "orderId": 11,  
                "orderListId": 2,  
                "clientOrderId": "yINkaXSJeoi3bU5vWMY8Z8",  
                "transactTime": 1763000506354,  
                "price": "104261.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.00000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "PENDING_NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "SELL",  
                "workingTime": -1,  
                "selfTradePreventionMode": "NONE"  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#conditional-fields-in-order-responses) 部分。

#### 取消订单列表 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#取消订单列表-trade "取消订单列表 \(TRADE\)的直接链接")
    
    
    DELETE /api/v3/orderList  
    

取消整个订单列表。

**权重:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
orderListId| LONG| NO| `orderListId` 或 `listClientOrderId` 必须被提供  
listClientOrderId| STRING| NO| `orderListId` 或 `listClientOrderId` 必须被提供  
newClientOrderId| STRING| NO| 用户自定义的本次撤销操作的ID(注意不是被撤销的订单的自定义ID)。如无指定会自动赋值。  
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
其他注意点:

  * 取消订单列表中的单个订单将取消整个订单列表.
  * 当同时提供 `orderListId` 和 `listClientOrderId` 两个参数时，系统首先将会使用 `orderListId` 来搜索订单。然后， 查找结果中的 `listClientOrderId` 的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。



**数据源:** 撮合引擎

**响应:**
    
    
    {  
        "orderListId": 0,  
        "contingencyType": "OCO",  
        "listStatusType": "ALL_DONE",  
        "listOrderStatus": "ALL_DONE",  
        "listClientOrderId": "C3wyj4WVEktd7u9aVBRXcN",  
        "transactionTime": 1574040868128,  
        "symbol": "LTCBTC",  
        "orders": [  
            {  
                "symbol": "LTCBTC",  
                "orderId": 2,  
                "clientOrderId": "pO9ufTiFGg3nw2fOdgeOXa"  
            },  
            {  
                "symbol": "LTCBTC",  
                "orderId": 3,  
                "clientOrderId": "TXOvglzXuaubXAaENpaRCB"  
            }  
        ],  
        "orderReports": [  
            {  
                "symbol": "LTCBTC",  
                "origClientOrderId": "pO9ufTiFGg3nw2fOdgeOXa",  
                "orderId": 2,  
                "orderListId": 0,  
                "clientOrderId": "unfWT8ig8i0uj6lPuYLez6",  
                "transactTime": 1688005070874,  
                "price": "1.00000000",  
                "origQty": "10.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "STOP_LOSS_LIMIT",  
                "side": "SELL",  
                "stopPrice": "1.00000000"  
            },  
            {  
                "symbol": "LTCBTC",  
                "origClientOrderId": "TXOvglzXuaubXAaENpaRCB",  
                "orderId": 3,  
                "orderListId": 0,  
                "clientOrderId": "unfWT8ig8i0uj6lPuYLez6",  
                "transactTime": 1688005070874,  
                "price": "3.00000000",  
                "origQty": "10.00000000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT_MAKER",  
                "side": "SELL"  
            }  
        ]  
    }  
    

### SOR[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#sor "SOR的直接链接")

#### 下 SOR 订单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#下-sor-订单-trade "下 SOR 订单 \(TRADE\)的直接链接")
    
    
    POST /api/v3/sor/order  
    

发送使用智能订单路由 (SOR) 的新订单。

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

参阅 [智能指令路由 (SOR)](/docs/zh-CN/binance-spot-api-docs/faqs/sor_faq) 了解更多详情。

**权重:** 1

**未成交的订单计数:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
side| ENUM| YES|   
type| ENUM| YES|   
timeInForce| ENUM| NO|   
quantity| DECIMAL| YES|   
price| DECIMAL| NO|   
newClientOrderId| STRING| NO| 用户自定义的orderid，如空缺系统会自动赋值。如果几个订单具有相同的 `newClientOrderID` 赋值，  
那么只有在前一个订单成交后才可以接受下一个订单，否则该订单将被拒绝。  
strategyId| LONG| NO|   
strategyType| INT| NO| 赋值不能小于 `1000000`.  
icebergQty| DECIMAL| NO| 仅有限价单可以使用该参数，含义为创建冰山订单并指定冰山订单的数量。  
newOrderRespType| ENUM| NO| 指定响应类型:  
指定响应类型 `ACK`, `RESULT` 或 `FULL`; 默认为 `FULL`。| | |   
selfTradePreventionMode| ENUM| NO| 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)。  
recvWindow| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
timestamp| LONG| YES|   
  
**请注意:** `POST /api/v3/sor/order` 只支持 `限价` 和 `市场` 单， 并不支持 `quoteOrderQty`。

**数据源:** 撮合引擎

**响应:**
    
    
    {  
        "symbol": "BTCUSDT",  
        "orderId": 2,  
        "orderListId": -1,  
        "clientOrderId": "sBI1KM6nNtOfj5tccZSKly",  
        "transactTime": 1689149087774,  
        "price": "31000.00000000",  
        "origQty": "0.50000000",  
        "executedQty": "0.50000000",  
        "origQuoteOrderQty": "0.000000",  
        "cummulativeQuoteQty": "14000.00000000",  
        "status": "FILLED",  
        "timeInForce": "GTC",  
        "type": "LIMIT",  
        "side": "BUY",  
        "workingTime": 1689149087774,  
        "fills": [  
            {  
                "matchType": "ONE_PARTY_TRADE_REPORT",  
                "price": "28000.00000000",  
                "qty": "0.50000000",  
                "commission": "0.00000000",  
                "commissionAsset": "BTC",  
                "tradeId": -1,  
                "allocId": 0  
            }  
        ],  
        "workingFloor": "SOR",  
        "selfTradePreventionMode": "NONE",  
        "usedSor": true  
    }  
    

#### 测试 SOR 下单接口 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#测试-sor-下单接口-trade "测试 SOR 下单接口 \(TRADE\)的直接链接")
    
    
    POST /api/v3/sor/order/test  
    

用于测试使用智能订单路由 (SOR) 的订单请求，但不会提交到撮合引擎

**权重:**

条件| 请求权重  
---|---  
没有 `computeCommissionRates`| 1  
有 `computeCommissionRates`| 20  
  
**参数:**

除了 [`POST /api/v3/sor/order`](/docs/zh-CN/binance-spot-api-docs/rest-api/trading-endpoints#sor-order) 所有参数, 如下参数也接受:

参数名| 类型| 是否必需| 描述  
---|---|---|---  
computeCommissionRates| BOOLEAN| NO| 默认值: `false`  
  
**数据源:** 缓存

**响应:**

没有 `computeCommissionRates`
    
    
    {}  
    

有 `computeCommissionRates`
    
    
    {  
        "standardCommissionForOrder": {  // 订单交易的标准佣金率。  
            "maker": "0.00000112",  
            "taker": "0.00000114"  
        },  
        "taxCommissionForOrder": {       // 订单交易的税率。  
            "maker": "0.00000112",  
            "taker": "0.00000114"  
        },  
        "discount": {                    // 以BNB支付时的标准佣金折扣。  
            "enabledForAccount": true,  
            "enabledForSymbol": true,  
            "discountAsset": "BNB",  
            "discount": "0.25000000"     // 当用BNB支付佣金时，在标准佣金上按此比率打折。  
        }  
    }