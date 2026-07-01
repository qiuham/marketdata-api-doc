---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/session-authentication
api_type: WebSocket
updated_at: 2026-07-01 19:07:12.019951
---

# Trading requests

### Place new order (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-trade "Direct link to Place new order \(TRADE\)")
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "price": "23416.10000000",  
            "quantity": "0.00847000",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",  
            "timestamp": 1660801715431  
        }  
    }  
    

Send in a new order.

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

**Weight:** 1

**Unfilled Order Count:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`side`| ENUM| YES| `BUY` or `SELL`  
`type`| ENUM| YES|   
`timeInForce`| ENUM| NO *|   
`price`| DECIMAL| NO *|   
`quantity`| DECIMAL| NO *|   
`quoteOrderQty`| DECIMAL| NO *|   
`newClientOrderId`| STRING| NO| Arbitrary unique ID among open orders. Automatically generated if not sent  
`newOrderRespType`| ENUM| NO| Select response format: `ACK`, `RESULT`, `FULL`.`MARKET` and `LIMIT` orders use `FULL` by default, other order types default to `ACK`.  
`stopPrice`| DECIMAL| NO *|   
`trailingDelta`| INT| NO *| See [Trailing Stop order FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq)  
`icebergQty`| DECIMAL| NO|   
`strategyId`| LONG| NO| Arbitrary numeric value identifying the order within an order strategy.  
`strategyType`| INT| NO| Arbitrary numeric value identifying the order strategy.Values smaller than `1000000` are reserved and cannot be used.  
`selfTradePreventionMode`| ENUM| NO| The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
`pegPriceType`| ENUM| NO| `PRIMARY_PEG` or `MARKET_PEG`   
See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pegOffsetValue`| INT| NO| Price level to peg the price to (max: 100)   
See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pegOffsetType`| ENUM| NO| Only `PRICE_LEVEL` is supported   
See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`signature`| STRING| YES|   
`timestamp`| LONG| YES|   
  
Certain parameters (*) become mandatory based on the order `type`:

Order `type` | Mandatory parameters  
---|---  
`LIMIT` | 

  * `timeInForce`
  * `price`
  * `quantity`

  
`LIMIT_MAKER` | 

  * `price`
  * `quantity`

  
`MARKET` | 

  * `quantity` or `quoteOrderQty`

  
`STOP_LOSS` | 

  * `quantity`
  * `stopPrice` or `trailingDelta`

  
`STOP_LOSS_LIMIT` | 

  * `timeInForce`
  * `price`
  * `quantity`
  * `stopPrice` or `trailingDelta`

  
`TAKE_PROFIT` | 

  * `quantity`
  * `stopPrice` or `trailingDelta`

  
`TAKE_PROFIT_LIMIT` | 

  * `timeInForce`
  * `price`
  * `quantity`
  * `stopPrice` or `trailingDelta`

  
  
Supported order types:

Order `type` | Description  
---|---  
`LIMIT` |  Buy or sell `quantity` at the specified `price` or better.   
`LIMIT_MAKER` |  `LIMIT` order that will be rejected if it immediately matches and trades as a taker.  This order type is also known as a POST-ONLY order.   
`MARKET` |  Buy or sell at the best available market price. 

  * `MARKET` order with `quantity` parameter specifies the amount of the _base asset_ you want to buy or sell. Actually executed quantity of the quote asset will be determined by available market liquidity.  E.g., a MARKET BUY order on BTCUSDT for `"quantity": "0.1000"` specifies that you want to buy 0.1 BTC at the best available price. If there is not enough BTC at the best price, keep buying at the next best price, until either your order is filled, or you run out of USDT, or market runs out of BTC. 
  * `MARKET` order with `quoteOrderQty` parameter specifies the amount of the _quote asset_ you want to spend (when buying) or receive (when selling). Actually executed quantity of the base asset will be determined by available market liquidity.  E.g., a MARKET BUY on BTCUSDT for `"quoteOrderQty": "100.00"` specifies that you want to buy as much BTC as you can for 100 USDT at the best available price. Similarly, a SELL order will sell as much available BTC as needed for you to receive 100 USDT (before commission). 

  
`STOP_LOSS` |  Execute a `MARKET` order for given `quantity` when specified conditions are met.  I.e., when `stopPrice` is reached, or when `trailingDelta` is activated.   
`STOP_LOSS_LIMIT` |  Place a `LIMIT` order with given parameters when specified conditions are met.   
`TAKE_PROFIT` |  Like `STOP_LOSS` but activates when market price moves in the favorable direction.   
`TAKE_PROFIT_LIMIT` |  Like `STOP_LOSS_LIMIT` but activates when market price moves in the favorable direction.   
  
Notes on using parameters for Pegged Orders:

  * These parameters are allowed for `LIMIT`, `LIMIT_MAKER`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` orders.
  * If `pegPriceType` is specified, `price` becomes optional. Otherwise, it is still mandatory.
  * `pegPriceType=PRIMARY_PEG` means the primary peg, that is the best price on the same side of the order book as your order.
  * `pegPriceType=MARKET_PEG` means the market peg, that is the best price on the opposite side of the order book from your order.
  * Use `pegOffsetType` and `pegOffsetValue` to request a price level other than the best one. These parameters must be specified together.



Available `timeInForce` options, setting how long the order should be active before expiration:

TIF| Description  
---|---  
`GTC`| **Good 'til Canceled** – the order will remain on the book until you cancel it, or the order is completely filled.  
`IOC`| **Immediate or Cancel** – the order will be filled for as much as possible, the unfilled quantity immediately expires.  
`FOK`| **Fill or Kill** – the order will expire unless it cannot be immediately filled for the entire quantity.  
  
Notes:

  * `newClientOrderId` specifies `clientOrderId` value for the order.

A new order with the same `clientOrderId` is accepted only when the previous one is filled or expired.

  * Any `LIMIT` or `LIMIT_MAKER` order can be made into an iceberg order by specifying the `icebergQty`.

An order with an `icebergQty` must have `timeInForce` set to `GTC`.

  * Trigger order price rules for `STOP_LOSS`/`TAKE_PROFIT` orders:

    * `stopPrice` must be above market price: `STOP_LOSS BUY`, `TAKE_PROFIT SELL`
    * `stopPrice` must be below market price: `STOP_LOSS SELL`, `TAKE_PROFIT BUY`
  * `MARKET` orders using `quoteOrderQty` follow [`LOT_SIZE`](/docs/binance-spot-api-docs/filters#lot_size) filter rules.

The order will execute a quantity that has notional value as close as possible to requested `quoteOrderQty`.




**Data Source:** Matching Engine

**Response:**

Response format is selected by using the `newOrderRespType` parameter.

`ACK` response type:
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12569099453,  
            "orderListId": -1, // always -1 for singular orders  
            "clientOrderId": "4d96324ff9d44481926157ec08158a40",  
            "transactTime": 1660801715639  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

`RESULT` response type:
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12569099453,  
            "orderListId": -1, // always -1 for singular orders  
            "clientOrderId": "4d96324ff9d44481926157ec08158a40",  
            "transactTime": 1660801715639,  
            "price": "23416.10000000",  
            "origQty": "0.00847000",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL",  
            "workingTime": 1660801715639,  
            "selfTradePreventionMode": "NONE"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

`FULL` response type:
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12569099453,  
            "orderListId": -1,  
            "clientOrderId": "4d96324ff9d44481926157ec08158a40",  
            "transactTime": 1660801715793,  
            "price": "23416.10000000",  
            "origQty": "0.00847000",  
            "executedQty": "0.00847000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "198.33521500",  
            "status": "FILLED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL",  
            "workingTime": 1660801715793,  
            // FULL response is identical to RESULT response, with the same optional fields  
            // based on the order type and parameters. FULL response additionally includes  
            // the list of trades which immediately filled the order.  
            "fills": [  
                {  
                    "price": "23416.10000000",  
                    "qty": "0.00635000",  
                    "commission": "0.000000",  
                    "commissionAsset": "BNB",  
                    "tradeId": 1650422481  
                },  
                {  
                    "price": "23416.50000000",  
                    "qty": "0.00212000",  
                    "commission": "0.000000",  
                    "commissionAsset": "BNB",  
                    "tradeId": 1650422482  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

**Conditional fields in Order Responses**

There are fields in the order responses (e.g. order placement, order query, order cancellation) that appear only if certain conditions are met.

These fields can apply to Order lists.

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
  
### Test new order (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#test-new-order-trade "Direct link to Test new order \(TRADE\)")
    
    
    {  
        "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",  
        "method": "order.test",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "price": "23416.10000000",  
            "quantity": "0.00847000",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",  
            "timestamp": 1660801715431  
        }  
    }  
    

Test order placement.

Validates new order parameters and verifies your signature but does not send the order into the matching engine.

**Weight:**

Condition| Request Weight  
---|---  
Without `computeCommissionRates`| 1  
With `computeCommissionRates`| 20  
  
**Parameters:**

In addition to all parameters accepted by [`order.place`](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-trade), the following optional parameters are also accepted:

Name| Type| Mandatory| Description  
---|---|---|---  
`computeCommissionRates`| BOOLEAN| NO| Default: `false`   
See [Commissions FAQ](/docs/binance-spot-api-docs/faqs/commission_faq#test-order-diferences) to learn more.  
  
**Data Source:** Memory

**Response:**

Without `computeCommissionRates`:
    
    
    {  
        "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",  
        "status": 200,  
        "result": {},  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

With `computeCommissionRates`:
    
    
    {  
        "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",  
        "status": 200,  
        "result": {  
            "standardCommissionForOrder": {  // Standard commission rates on trades from the order.  
                "maker": "0.00000112",  
                "taker": "0.00000114"  
            },  
            "specialCommissionForOrder": {   // Special commission rates on trades from the order.  
                "maker": "0.05000000",  
                "taker": "0.06000000"  
            },  
            "taxCommissionForOrder": {       // Tax commission rates for trades from the order  
                "maker": "0.00000112",  
                "taker": "0.00000114"  
            },  
            "discount": {                    // Discount on standard commissions when paying in BNB.  
                "enabledForAccount": true,  
                "enabledForSymbol": true,  
                "discountAsset": "BNB",  
                "discount": "0.25000000"     // Standard commission is reduced by this rate when paying in BNB.  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 20  
            }  
        ]  
    }  
    

### Cancel order (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-order-trade "Direct link to Cancel order \(TRADE\)")
    
    
    {  
        "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
        "method": "order.cancel",  
        "params": {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "4d96324ff9d44481926157",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "33d5b721f278ae17a52f004a82a6f68a70c68e7dd6776ed0be77a455ab855282",  
            "timestamp": 1660801715830  
        }  
    }  
    

Cancel an active order.

**Weight:** 1

**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
`symbol` | STRING | YES |   
`orderId` | LONG | YES | Cancel order by `orderId`  
`origClientOrderId` | STRING | Cancel order by `clientOrderId`  
`newClientOrderId` | STRING | NO | New ID for the canceled order. Automatically generated if not sent  
`cancelRestrictions` | ENUM | NO | Supported values:   
`ONLY_NEW` \- Cancel will succeed if the order status is `NEW`.  
`ONLY_PARTIALLY_FILLED` \- Cancel will succeed if order status is `PARTIALLY_FILLED`.  
`apiKey` | STRING | YES |   
`recvWindow` | DECIMAL | NO | The value cannot be greater than `60000`.  
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`signature` | STRING | YES |   
`timestamp` | LONG | YES |   
  
Notes:

  * If both `orderId` and `origClientOrderId` parameters are provided, the `orderId` is searched first, then the `origClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.

  * `newClientOrderId` will replace `clientOrderId` of the canceled order, freeing it up for new orders.

  * If you cancel an order that is a part of an order list, the entire order list is canceled.

  * The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only `orderId` is sent. Sending `origClientOrderId` or both `orderId` \+ `origClientOrderId` will be slower.




**Data Source:** Matching Engine

**Response:**

When an individual order is canceled:
    
    
    {  
        "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "4d96324ff9d44481926157",     // clientOrderId that was canceled  
            "orderId": 12569099453,  
            "orderListId": -1,                                 // set only for legs of an order list  
            "clientOrderId": "91fe37ce9e69c90d6358c0",         // newClientOrderId from request  
            "transactTime": 1684804350068,  
            "price": "23416.10000000",  
            "origQty": "0.00847000",  
            "executedQty": "0.00001000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.23416100",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL",  
            "stopPrice": "0.00000000",                         // present only if stopPrice set for the order  
            "trailingDelta": 0,                                // present only if trailingDelta set for the order  
            "icebergQty": "0.00000000",                        // present only if icebergQty set for the order  
            "strategyId": 37463720,                            // present only if strategyId set for the order  
            "strategyType": 1000000,                           // present only if strategyType set for the order  
            "selfTradePreventionMode": "NONE"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

When an order list is canceled:
    
    
    {  
        "id": "16eaf097-bbec-44b9-96ff-e97e6e875870",  
        "status": 200,  
        "result": {  
            "orderListId": 19431,  
            "contingencyType": "OCO",  
            "listStatusType": "ALL_DONE",  
            "listOrderStatus": "ALL_DONE",  
            "listClientOrderId": "iuVNVJYYrByz6C4yGOPPK0",  
            "transactionTime": 1660803702431,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569099453,  
                    "clientOrderId": "bX5wROblo6YeDwa9iTLeyY"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569099454,  
                    "clientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW"  
                }  
            ],  
            // order list order's status format is the same as for individual orders.  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "bX5wROblo6YeDwa9iTLeyY",  
                    "orderId": 12569099453,  
                    "orderListId": 19431,  
                    "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",  
                    "transactTime": 1684804350068,  
                    "price": "23450.50000000",  
                    "origQty": "0.00850000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "BUY",  
                    "stopPrice": "23430.00000000",  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW",  
                    "orderId": 12569099454,  
                    "orderListId": 19431,  
                    "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",  
                    "transactTime": 1684804350068,  
                    "price": "23400.00000000",  
                    "origQty": "0.00850000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "BUY",  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses).

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
    

### Cancel and replace order (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-and-replace-order-trade "Direct link to Cancel and replace order \(TRADE\)")
    
    
    {  
        "id": "99de1036-b5e2-4e0f-9b5c-13d751c93a1a",  
        "method": "order.cancelReplace",  
        "params": {  
            "symbol": "BTCUSDT",  
            "cancelReplaceMode": "ALLOW_FAILURE",  
            "cancelOrigClientOrderId": "4d96324ff9d44481926157",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "price": "23416.10000000",  
            "quantity": "0.00847000",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "7028fdc187868754d25e42c37ccfa5ba2bab1d180ad55d4c3a7e2de643943dc5",  
            "timestamp": 1660813156900  
        }  
    }  
    

  * Cancel an existing order and immediately place a new order instead of the canceled one.
  * A new order that was not attempted (i.e. when `newOrderResult: NOT_ATTEMPTED`), will still increase the unfilled order count by 1.
  * You can only cancel an individual order from an orderList using this method, but the result is the same as canceling the entire orderList.



**Weight:** 1

**Unfilled Order Count:** 1

**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
`symbol` | STRING | YES |   
`cancelReplaceMode` | ENUM | YES |   
`cancelOrderId` | LONG | YES | Cancel order by `orderId`  
`cancelOrigClientOrderId` | STRING | Cancel order by `clientOrderId`  
`cancelNewClientOrderId` | STRING | NO | New ID for the canceled order. Automatically generated if not sent  
`side` | ENUM | YES | `BUY` or `SELL`  
`type` | ENUM | YES |   
`timeInForce` | ENUM | NO * |   
`price` | DECIMAL | NO * |   
`quantity` | DECIMAL | NO * |   
`quoteOrderQty` | DECIMAL | NO * |   
`newClientOrderId` | STRING | NO | Arbitrary unique ID among open orders. Automatically generated if not sent  
`newOrderRespType` | ENUM | NO |  Select response format: `ACK`, `RESULT`, `FULL`. `MARKET` and `LIMIT` orders produce `FULL` response by default, other order types default to `ACK`.   
`stopPrice` | DECIMAL | NO * |   
`trailingDelta` | DECIMAL | NO * | See [Trailing Stop order FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq)  
`icebergQty` | DECIMAL | NO |   
`strategyId` | LONG | NO | Arbitrary numeric value identifying the order within an order strategy.  
`strategyType` | INT | NO |  Arbitrary numeric value identifying the order strategy. Values smaller than `1000000` are reserved and cannot be used.  
`selfTradePreventionMode` | ENUM | NO |  The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums.md#stpmodes).  
`cancelRestrictions` | ENUM | NO | Supported values:   
`ONLY_NEW` \- Cancel will succeed if the order status is `NEW`.  
`ONLY_PARTIALLY_FILLED` \- Cancel will succeed if order status is `PARTIALLY_FILLED`. For more information please refer to [Regarding `cancelRestrictions`](/docs/binance-spot-api-docs/websocket-api/trading-requests#regarding-cancelrestrictions).  
`apiKey` | STRING | YES |   
`orderRateLimitExceededMode` | ENUM | NO | Supported values:   
`DO_NOTHING` (default)- will only attempt to cancel the order if account has not exceeded the unfilled order rate limit  
`CANCEL_ONLY` \- will always cancel the order.  
`pegPriceType` | ENUM | NO | `PRIMARY_PEG` or `MARKET_PEG`.   
See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)"  
`pegOffsetValue` | INT | NO | Price level to peg the price to (max: 100)   
See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pegOffsetType` | ENUM | NO | Only `PRICE_LEVEL` is supported  
See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`recvWindow` | DECIMAL | NO | The value cannot be greater than `60000`.  
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`signature` | STRING | YES |   
`timestamp` | LONG | YES |   
  
Similar to the [`order.place`](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-trade) request, additional mandatory parameters (*) are determined by the new order [`type`](/docs/binance-spot-api-docs/websocket-api/trading-requests#order-type).

Available `cancelReplaceMode` options:

  * `STOP_ON_FAILURE` – if cancellation request fails, new order placement will not be attempted.
  * `ALLOW_FAILURE` – new order placement will be attempted even if the cancel request fails.

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
Exceeds Limits | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ❌ `FAILURE` | `400`  
❌ `FAILURE` | ✅ `SUCCESS` | N/A  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
  
Notes:

  * If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.

  * `cancelNewClientOrderId` will replace `clientOrderId` of the canceled order, freeing it up for new orders.

  * `newClientOrderId` specifies `clientOrderId` value for the placed order.

A new order with the same `clientOrderId` is accepted only when the previous one is filled or expired.

The new order can reuse old `clientOrderId` of the canceled order.

  * This cancel-replace operation is **not transactional**.

If one operation succeeds but the other one fails, the successful operation is still executed.

For example, in `STOP_ON_FAILURE` mode, if the new order placement fails, the old order is still canceled.

  * Filters and order count limits are evaluated before cancellation and order placement occurs.

  * If new order placement is not attempted, your order count is still incremented.

  * Like [`order.cancel`](/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-order-trade), if you cancel an individual order from an order list, the entire order list is canceled.

  * The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only `orderId` is sent. Sending `origClientOrderId` or both `orderId` \+ `origClientOrderId` will be slower.




**Data Source:** Matching Engine

**Response:**

If both cancel and placement succeed, you get the following response with `"status": 200`:
    
    
    {  
        "id": "99de1036-b5e2-4e0f-9b5c-13d751c93a1a",  
        "status": 200,  
        "result": {  
            "cancelResult": "SUCCESS",  
            "newOrderResult": "SUCCESS",  
            // Format is identical to "order.cancel" format.  
            // Some fields are optional and are included only for orders that set them.  
            "cancelResponse": {  
                "symbol": "BTCUSDT",  
                "origClientOrderId": "4d96324ff9d44481926157",     // cancelOrigClientOrderId from request  
                "orderId": 125690984230,  
                "orderListId": -1,  
                "clientOrderId": "91fe37ce9e69c90d6358c0",         // cancelNewClientOrderId from request  
                "transactTime": 1684804350068,  
                "price": "23450.00000000",  
                "origQty": "0.00847000",  
                "executedQty": "0.00001000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.23450000",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "selfTradePreventionMode": "NONE"  
            },  
            // Format is identical to "order.place" format, affected by "newOrderRespType".  
            // Some fields are optional and are included only for orders that set them.  
            "newOrderResponse": {  
                "symbol": "BTCUSDT",  
                "orderId": 12569099453,  
                "orderListId": -1,  
                "clientOrderId": "bX5wROblo6YeDwa9iTLeyY",         // newClientOrderId from request  
                "transactTime": 1660813156959,  
                "price": "23416.10000000",  
                "origQty": "0.00847000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "selfTradePreventionMode": "NONE"  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

In `STOP_ON_FAILURE` mode, failed order cancellation prevents new order from being placed and returns the following response with `"status": 400`:
    
    
    {  
        "id": "27e1bf9f-0539-4fb0-85c6-06183d36f66c",  
        "status": 400,  
        "error": {  
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
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

If cancel-replace mode allows failure and one of the operations fails, you get a response with `"status": 409`, and the `"data"` field detailing which operation succeeded, which failed, and why:
    
    
    {  
        "id": "b220edfe-f3c4-4a3a-9d13-b35473783a25",  
        "status": 409,  
        "error": {  
            "code": -2021,  
            "msg": "Order cancel-replace partially failed.",  
            "data": {  
                "cancelResult": "SUCCESS",  
                "newOrderResult": "FAILURE",  
                "cancelResponse": {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "4d96324ff9d44481926157",  
                    "orderId": 125690984230,  
                    "orderListId": -1,  
                    "clientOrderId": "91fe37ce9e69c90d6358c0",  
                    "transactTime": 1684804350068,  
                    "price": "23450.00000000",  
                    "origQty": "0.00847000",  
                    "executedQty": "0.00001000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.23450000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "SELL",  
                    "selfTradePreventionMode": "NONE"  
                },  
                "newOrderResponse": {  
                    "code": -2010,  
                    "msg": "Order would immediately match and take."  
                }  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    
    
    
    {  
        "id": "ce641763-ff74-41ac-b9f7-db7cbe5e93b1",  
        "status": 409,  
        "error": {  
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
                    "orderId": 12569099453,  
                    "orderListId": -1,  
                    "clientOrderId": "bX5wROblo6YeDwa9iTLeyY",  
                    "transactTime": 1660813156959,  
                    "price": "23416.10000000",  
                    "origQty": "0.00847000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "SELL",  
                    "workingTime": 1669693344508,  
                    "fills": [],  
                    "selfTradePreventionMode": "NONE"  
                }  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

If both operations fail, response will have `"status": 400`:
    
    
    {  
        "id": "3b3ac45c-1002-4c7d-88e8-630c408ecd87",  
        "status": 400,  
        "error": {  
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
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

If `orderRateLimitExceededMode` is `DO_NOTHING` regardless of `cancelReplaceMode`, and you have exceeded your unfilled order count, you will get status `429` with the following error:
    
    
    {  
        "id": "3b3ac45c-1002-4c7d-88e8-630c408ecd87",  
        "status": 429,  
        "error": {  
            "code": -1015,  
            "msg": "Too many new orders; current limit is 50 orders per 10 SECOND."  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 50  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 50  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

If `orderRateLimitExceededMode` is `CANCEL_ONLY` regardless of `cancelReplaceMode`, and you have exceeded your unfilled order count, you will get status `409` with the following error:
    
    
    {  
        "id": "3b3ac45c-1002-4c7d-88e8-630c408ecd87",  
        "status": 409,  
        "error": {  
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
                    "msg": "Too many new orders; current limit is 50 orders per 10 SECOND."  
                }  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 50  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 50  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses).

### Order Amend Keep Priority (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#order-amend-keep-priority-trade "Direct link to Order Amend Keep Priority \(TRADE\)")
    
    
    {  
        "id": "56374a46-3061-486b-a311-89ee972eb648",  
        "method": "order.amend.keepPriority",  
        "params": {  
            "newQty": "5",  
            "origClientOrderId": "my_test_order1",  
            "recvWindow": 5000,  
            "symbol": "BTCUSDT",  
            "timestamp": 1741922620419,  
            "apiKey": "Rl1KOMDCpSg6xviMYOkNk9ENUB5QOTnufXukVe0Ijd40yduAlpHn78at3rJyJN4F",  
            "signature": "fa49c0c4ebc331c6ebd3fcb20deb387f60081ea858eebe6e35aa6fcdf2a82e08"  
        }  
    }  
    

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

**Response:**

Response for a single order:
    
    
    {  
        "id": "56374a46-3061-486b-a311-89ee972eb648",  
        "status": 200,  
        "result": {  
            "transactTime": 1741923284382,  
            "executionId": 16,  
            "amendedOrder": {  
                "symbol": "BTCUSDT",  
                "orderId": 12,  
                "orderListId": -1,  
                "origClientOrderId": "my_test_order1",  
                "clientOrderId": "4zR9HFcEq8gM1tWUqPEUHc",  
                "price": "5.00000000",  
                "qty": "5.00000000",  
                "executedQty": "0.00000000",  
                "preventedQty": "0.00000000",  
                "quoteOrderQty": "0.00000000",  
                "cumulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "BUY",  
                "workingTime": 1741923284364,  
                "selfTradePreventionMode": "NONE"  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

Response for an order which is part of an Order list:
    
    
    {  
        "id": "56374b46-3061-486b-a311-89ee972eb648",  
        "status": 200,  
        "result": {  
            "transactTime": 1741924229819,  
            "executionId": 60,  
            "amendedOrder": {  
                "symbol": "BTUCSDT",  
                "orderId": 23,  
                "orderListId": 4,  
                "origClientOrderId": "my_pending_order",  
                "clientOrderId": "xbxXh5SSwaHS7oUEOCI88B",  
                "price": "1.00000000",  
                "qty": "5.00000000",  
                "executedQty": "0.00000000",  
                "preventedQty": "0.00000000",  
                "quoteOrderQty": "0.00000000",  
                "cumulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "BUY",  
                "workingTime": 1741924204920,  
                "selfTradePreventionMode": "NONE"  
            },  
            "listStatus": {  
                "orderListId": 4,  
                "contingencyType": "OTO",  
                "listOrderStatus": "EXECUTING",  
                "listClientOrderId": "8nOGLLawudj1QoOiwbroRH",  
                "symbol": "BTCUSDT",  
                "orders": [  
                    {  
                        "symbol": "BTCUSDT",  
                        "orderId": 22,  
                        "clientOrderId": "g04EWsjaackzedjC9wRkWD"  
                    },  
                    {  
                        "symbol": "BTCUSDT",  
                        "orderId": 23,  
                        "clientOrderId": "xbxXh5SSwaHS7oUEOCI88B"  
                    }  
                ]  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

**Note:** The payloads above do not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses).

### Cancel open orders (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-open-orders-trade "Direct link to Cancel open orders \(TRADE\)")
    
    
    {  
        "id": "778f938f-9041-4b88-9914-efbf64eeacc8",  
        "method": "openOrders.cancelAll",  
        "params": {  
            "symbol": "BTCUSDT",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "773f01b6e3c2c9e0c1d217bc043ce383c1ddd6f0e25f8d6070f2b66a6ceaf3a5",  
            "timestamp": 1660805557200  
        }  
    }  
    

Cancel all open orders on a symbol. This includes orders that are part of an order list.

**Weight:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`signature`| STRING| YES|   
`timestamp`| LONG| YES|   
  
**Data Source:** Matching Engine

**Response:**

Cancellation reports for orders and order lists have the same format as in [`order.cancel`](/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-order-trade).
    
    
    {  
        "id": "778f938f-9041-4b88-9914-efbf64eeacc8",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BTCUSDT",  
                "origClientOrderId": "4d96324ff9d44481926157",  
                "orderId": 12569099453,  
                "orderListId": -1,  
                "clientOrderId": "91fe37ce9e69c90d6358c0",  
                "transactTime": 1684804350068,  
                "price": "23416.10000000",  
                "origQty": "0.00847000",  
                "executedQty": "0.00001000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.23416100",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "stopPrice": "0.00000000",  
                "trailingDelta": 0,  
                "trailingTime": -1,  
                "icebergQty": "0.00000000",  
                "strategyId": 37463720,  
                "strategyType": 1000000,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "orderListId": 19431,  
                "contingencyType": "OCO",  
                "listStatusType": "ALL_DONE",  
                "listOrderStatus": "ALL_DONE",  
                "listClientOrderId": "iuVNVJYYrByz6C4yGOPPK0",  
                "transactionTime": 1660803702431,  
                "symbol": "BTCUSDT",  
                "orders": [  
                    {  
                        "symbol": "BTCUSDT",  
                        "orderId": 12569099453,  
                        "clientOrderId": "bX5wROblo6YeDwa9iTLeyY"  
                    },  
                    {  
                        "symbol": "BTCUSDT",  
                        "orderId": 12569099454,  
                        "clientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW"  
                    }  
                ],  
                "orderReports": [  
                    {  
                        "symbol": "BTCUSDT",  
                        "origClientOrderId": "bX5wROblo6YeDwa9iTLeyY",  
                        "orderId": 12569099453,  
                        "orderListId": 19431,  
                        "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",  
                        "transactTime": 1684804350068,  
                        "price": "23450.50000000",  
                        "origQty": "0.00850000",  
                        "executedQty": "0.00000000",  
                        "origQuoteOrderQty": "0.000000",  
                        "cummulativeQuoteQty": "0.00000000",  
                        "status": "CANCELED",  
                        "timeInForce": "GTC",  
                        "type": "STOP_LOSS_LIMIT",  
                        "side": "BUY",  
                        "stopPrice": "23430.00000000",  
                        "selfTradePreventionMode": "NONE"  
                    },  
                    {  
                        "symbol": "BTCUSDT",  
                        "origClientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW",  
                        "orderId": 12569099454,  
                        "orderListId": 19431,  
                        "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",  
                        "transactTime": 1684804350068,  
                        "price": "23400.00000000",  
                        "origQty": "0.00850000",  
                        "executedQty": "0.00000000",  
                        "origQuoteOrderQty": "0.000000",  
                        "cummulativeQuoteQty": "0.00000000",  
                        "status": "CANCELED",  
                        "timeInForce": "GTC",  
                        "type": "LIMIT_MAKER",  
                        "side": "BUY",  
                        "selfTradePreventionMode": "NONE"  
                    }  
                ]  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses).

### Order lists[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#order-lists "Direct link to Order lists")

#### Place new OCO - Deprecated (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-oco---deprecated-trade "Direct link to Place new OCO - Deprecated \(TRADE\)")
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "method": "orderList.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "price": "23420.00000000",  
            "quantity": "0.00650000",  
            "stopPrice": "23410.00000000",  
            "stopLimitPrice": "23405.00000000",  
            "stopLimitTimeInForce": "GTC",  
            "newOrderRespType": "RESULT",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "6689c2a36a639ff3915c2904871709990ab65f3c7a9ff13857558fd350315c35",  
            "timestamp": 1660801713767  
        }  
    }  
    

Send in a new one-cancels-the-other (OCO) pair: `LIMIT_MAKER` \+ `STOP_LOSS`/`STOP_LOSS_LIMIT` orders (called _legs_), where activation of one order immediately cancels the other.

This adds 1 order to `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter

**Weight:** 1

**Unfilled Order Count:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`side`| ENUM| YES| `BUY` or `SELL`  
`price`| DECIMAL| YES| Price for the limit order  
`quantity`| DECIMAL| YES|   
`listClientOrderId`| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent  
`limitClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the limit order. Automatically generated if not sent  
`limitIcebergQty`| DECIMAL| NO|   
`limitStrategyId`| LONG| NO| Arbitrary numeric value identifying the limit order within an order strategy.  
`limitStrategyType`| INT| NO| Arbitrary numeric value identifying the limit order strategy.Values smaller than `1000000` are reserved and cannot be used.  
`stopPrice`| DECIMAL| YES *| Either `stopPrice` or `trailingDelta`, or both must be specified  
`trailingDelta`| INT| YES *| See [Trailing Stop order FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq)  
`stopClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the stop order. Automatically generated if not sent  
`stopLimitPrice`| DECIMAL| NO *|   
`stopLimitTimeInForce`| ENUM| NO *| See [`order.place`](/docs/binance-spot-api-docs/websocket-api/trading-requests#timeInForce) for available options  
`stopIcebergQty`| DECIMAL| NO *|   
`stopStrategyId`| LONG| NO| Arbitrary numeric value identifying the stop order within an order strategy.  
`stopStrategyType`| INT| NO| Arbitrary numeric value identifying the stop order strategy.Values smaller than `1000000` are reserved and cannot be used.  
`newOrderRespType`| ENUM| NO| Select response format: `ACK`, `RESULT`, `FULL` (default)  
`selfTradePreventionMode`| ENUM| NO| The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`signature`| STRING| YES|   
`timestamp`| LONG| YES|   
  
Notes:

  * `listClientOrderId` parameter specifies `listClientOrderId` for the OCO pair.

A new OCO with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.

`listClientOrderId` is distinct from `clientOrderId` of individual orders.

  * `limitClientOrderId` and `stopClientOrderId` specify `clientOrderId` values for both legs of the OCO.

A new order with the same `clientOrderId` is accepted only when the previous one is filled or expired.

  * Price restrictions on the legs:

`side`| Price relation  
---|---  
`BUY`| `price` < market price < `stopPrice`  
`SELL`| `price` > market price > `stopPrice`  
  * Both legs have the same `quantity`.

However, you can set different iceberg quantity for individual legs.

If `stopIcebergQty` is used, `stopLimitTimeInForce` must be `GTC`.

  * `trailingDelta` applies only to the `STOP_LOSS`/`STOP_LOSS_LIMIT` leg of the OCO.




**Data Source:** Matching Engine

**Response:**

Response format for `orderReports` is selected using the `newOrderRespType` parameter. The following example is for `RESULT` response type. See [`order.place`](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-trade) for more examples.
    
    
    {  
        "id": "57833dc0-e3f2-43fb-ba20-46480973b0aa",  
        "status": 200,  
        "result": {  
            "orderListId": 1274512,  
            "contingencyType": "OCO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "08985fedd9ea2cf6b28996",  
            "transactionTime": 1660801713793,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138901,  
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138902,  
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138901,  
                    "orderListId": 1274512,  
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU",  
                    "transactTime": 1660801713793,  
                    "price": "23410.00000000",  
                    "origQty": "0.00650000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "SELL",  
                    "stopPrice": "23405.00000000",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138902,  
                    "orderListId": 1274512,  
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us",  
                    "transactTime": 1660801713793,  
                    "price": "23420.00000000",  
                    "origQty": "0.00650000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "SELL",  
                    "workingTime": 1660801713793,  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 2  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 2  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

#### Place new Order list - OCO (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-list---oco-trade "Direct link to Place new Order list - OCO \(TRADE\)")
    
    
    {  
        "id": "56374a46-3261-486b-a211-99ed972eb648",  
        "method": "orderList.place.oco",  
        "params": {  
            "symbol": "LTCBNB",  
            "side": "BUY",  
            "quantity": 1,  
            "timestamp": 1711062760647,  
            "aboveType": "STOP_LOSS_LIMIT",  
            "abovePrice": "1.5",  
            "aboveStopPrice": "1.50000001",  
            "aboveTimeInForce": "GTC",  
            "belowType": "LIMIT_MAKER",  
            "belowPrice": "1.49999999",  
            "apiKey": "duwNf97YPLqhFIk7kZF0dDdGYVAXStA7BeEz0fIT9RAhUbixJtyS6kJ3hhzJsRXC",  
            "signature": "64614cfd8dd38260d4fd86d3c455dbf4b9d1c8a8170ea54f700592a986c30ddb"  
        }  
    }  
    

Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

  * An OCO has 2 orders called the **above order** and **below order**.
  * One of the orders must be a `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` order and the other must be `STOP_LOSS` or `STOP_LOSS_LIMIT` order.
  * Price restrictions: 
    * If the OCO is on the `SELL` side: 
      * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
      * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
    * If the OCO is on the `BUY` side: 
      * `LIMIT_MAKER` `price` < Last Traded Price < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
      * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
  * OCOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and `MAX_NUM_ORDERS` filter.



**Weight:** 1

**Unfilled Order Count:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`listClientOrderId`| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent.   
A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.   
`listClientOrderId` is distinct from the `aboveClientOrderId` and the `belowCLientOrderId`.  
`side`| ENUM| YES| `BUY` or `SELL`  
`quantity`| DECIMAL| YES| Quantity for both orders of the order list.  
`aboveType`| ENUM| YES| Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
`aboveClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the above order. Automatically generated if not sent  
`aboveIcebergQty`| LONG| NO| Note that this can only be used if `aboveTimeInForce` is `GTC`.  
`abovePrice`| DECIMAL| NO| Can be used if `aboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.  
`aboveStopPrice`| DECIMAL| NO| Can be used if `aboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`.   
Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified.  
`aboveTrailingDelta`| LONG| NO| See [Trailing Stop order FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq).  
`aboveTimeInForce`| ENUM| NO| Required if `aboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.  
`aboveStrategyId`| LONG| NO| Arbitrary numeric value identifying the above order within an order strategy.  
`aboveStrategyType`| INT| NO| Arbitrary numeric value identifying the above order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
`abovePegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`abovePegOffsetType`| ENUM| NO|   
`abovePegOffsetValue`| INT| NO|   
`belowType`| ENUM| YES| Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`  
`belowClientOrderId`| STRING| NO|   
`belowIcebergQty`| LONG| NO| Note that this can only be used if `belowTimeInForce` is `GTC`.  
`belowPrice`| DECIMAL| NO| Can be used if `belowType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.  
`belowStopPrice`| DECIMAL| NO| Can be used if `belowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` or `TAKE_PROFIT_LIMIT`.   
Either `belowStopPrice` or `belowTrailingDelta` or both, must be specified.  
`belowTrailingDelta`| LONG| NO| See [Trailing Stop order FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq).  
`belowTimeInForce`| ENUM| NO| Required if `belowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`  
`belowStrategyId`| LONG| NO| Arbitrary numeric value identifying the below order within an order strategy.  
`belowStrategyType`| INT| NO| Arbitrary numeric value identifying the below order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
`belowPegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`belowPegOffsetType`| ENUM| NO|   
`belowPegOffsetValue`| INT| NO|   
`newOrderRespType`| ENUM| NO| Select response format: `ACK`, `RESULT`, `FULL`  
`selfTradePreventionMode`| ENUM| NO| The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes).  
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`timestamp`| LONG| YES|   
`signature`| STRING| YES|   
  
**Data Source:** Matching Engine

**Response:**

Response format for `orderReports` is selected using the `newOrderRespType` parameter. The following example is for `RESULT` response type. See [`order.place`](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-trade) for more examples.
    
    
    {  
        "id": "56374a46-3261-486b-a211-99ed972eb648",  
        "status": 200,  
        "result": {  
            "orderListId": 2,  
            "contingencyType": "OCO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "cKPMnDCbcLQILtDYM4f4fX",  
            "transactionTime": 1711062760648,  
            "symbol": "LTCBNB",  
            "orders": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 2,  
                    "clientOrderId": "0m6I4wfxvTUrOBSMUl0OPU"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 3,  
                    "clientOrderId": "Z2IMlR79XNY5LU0tOxrWyW"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 2,  
                    "orderListId": 2,  
                    "clientOrderId": "0m6I4wfxvTUrOBSMUl0OPU",  
                    "transactTime": 1711062760648,  
                    "price": "1.50000000",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "BUY",  
                    "stopPrice": "1.50000001",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 3,  
                    "orderListId": 2,  
                    "clientOrderId": "Z2IMlR79XNY5LU0tOxrWyW",  
                    "transactTime": 1711062760648,  
                    "price": "1.49999999",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "BUY",  
                    "workingTime": 1711062760648,  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 2  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 2  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

#### Place new Order list - OTO (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-list---oto-trade "Direct link to Place new Order list - OTO \(TRADE\)")
    
    
    {  
        "id": "1712544395950",  
        "method": "orderList.place.oto",  
        "params": {  
            "signature": "3e1e5ac8690b0caf9a2afd5c5de881ceba69939cc9d817daead5386bf65d0cbb",  
            "apiKey": "Rf07JlnL9PHVxjs27O5CvKNyOsV4qJ5gXdrRfpvlOdvMZbGZbPO5Ce2nIwfRP0iA",  
            "pendingQuantity": 1,  
            "pendingSide": "BUY",  
            "pendingType": "MARKET",  
            "symbol": "LTCBNB",  
            "recvWindow": "5000",  
            "timestamp": "1712544395951",  
            "workingPrice": 1,  
            "workingQuantity": 1,  
            "workingSide": "SELL",  
            "workingTimeInForce": "GTC",  
            "workingType": "LIMIT"  
        }  
    }  
    

Places an OTO.

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
`symbol`| STRING| YES|   
`listClientOrderId`| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent.   
A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired.   
`listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.  
`newOrderRespType`| ENUM| NO| Format of the JSON response. Supported values: [Order Response Type](/docs/binance-spot-api-docs/enums#orderresponsetype)  
`selfTradePreventionMode`| ENUM| NO| The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
`workingType`| ENUM| YES| Supported values: `LIMIT`,`LIMIT_MAKER`  
`workingSide`| ENUM| YES| Supported values: [Order side](/docs/binance-spot-api-docs/enums#side)  
`workingClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the working order.  
Automatically generated if not sent.  
`workingPrice`| DECIMAL| YES|   
`workingQuantity`| DECIMAL| YES| Sets the quantity for the working order.  
`workingIcebergQty`| DECIMAL| NO| This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.  
`workingTimeInForce`| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
`workingStrategyId`| LONG| NO| Arbitrary numeric value identifying the working order within an order strategy.  
`workingStrategyType`| INT| NO| Arbitrary numeric value identifying the working order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
`workingPegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`workingPegOffsetType`| ENUM| NO|   
`workingPegOffsetValue`| INT| NO|   
`pendingType`| ENUM| YES| Supported values: [Order types](/docs/binance-spot-api-docs/websocket-api/trading-requests#order-type).   
Note that `MARKET` orders using `quoteOrderQty` are not supported.  
`pendingSide`| ENUM| YES| Supported values: [Order side](/docs/binance-spot-api-docs/enums#side)  
`pendingClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the pending order.  
Automatically generated if not sent.  
`pendingPrice`| DECIMAL| NO|   
`pendingStopPrice`| DECIMAL| NO|   
`pendingTrailingDelta`| DECIMAL| NO|   
`pendingQuantity`| DECIMAL| YES| Sets the quantity for the pending order.  
`pendingIcebergQty`| DECIMAL| NO| This can only be used if `pendingTimeInForce` is `GTC`, or if `pendingType` is `LIMIT_MAKER`.  
`pendingTimeInForce`| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
`pendingStrategyId`| LONG| NO| Arbitrary numeric value identifying the pending order within an order strategy.  
`pendingStrategyType`| INT| NO| Arbitrary numeric value identifying the pending order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
`pendingPegOffsetType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingPegPriceType`| ENUM| NO|   
`pendingPegOffsetValue`| INT| NO|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`timestamp`| LONG| YES|   
`signature`| STRING| YES|   
  
**Mandatory parameters based on`pendingType` or `workingType`**

Depending on the `pendingType` or `workingType`, some optional parameters will become mandatory.

Type| Additional mandatory parameters| Additional information  
---|---|---  
`workingType` = `LIMIT`| `workingTimeInForce`|   
`pendingType` = `LIMIT`| `pendingPrice`, `pendingTimeInForce`|   
`pendingType` = `STOP_LOSS` or `TAKE_PROFIT`| `pendingStopPrice` and/or `pendingTrailingDelta`|   
`pendingType` =`STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`| `pendingPrice`, `pendingStopPrice` and/or `pendingTrailingDelta`, `pendingTimeInForce`|   
  
**Data Source:** Matching Engine

**Response:**
    
    
    {  
        "id": "1712544395950",  
        "status": 200,  
        "result": {  
            "orderListId": 626,  
            "contingencyType": "OTO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "KA4EBjGnzvSwSCQsDdTrlf",  
            "transactionTime": 1712544395981,  
            "symbol": "1712544378871",  
            "orders": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 13,  
                    "clientOrderId": "YiAUtM9yJjl1a2jXHSp9Ny"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 14,  
                    "clientOrderId": "9MxJSE1TYkmyx5lbGLve7R"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 13,  
                    "orderListId": 626,  
                    "clientOrderId": "YiAUtM9yJjl1a2jXHSp9Ny",  
                    "transactTime": 1712544395981,  
                    "price": "1.000000",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "SELL",  
                    "workingTime": 1712544395981,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 14,  
                    "orderListId": 626,  
                    "clientOrderId": "9MxJSE1TYkmyx5lbGLve7R",  
                    "transactTime": 1712544395981,  
                    "price": "0.000000",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "PENDING_NEW",  
                    "timeInForce": "GTC",  
                    "type": "MARKET",  
                    "side": "BUY",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 10000000,  
                "count": 10  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 1000,  
                "count": 38  
            }  
        ]  
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses).

#### Place new Order list - OTOCO (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-list---otoco-trade "Direct link to Place new Order list - OTOCO \(TRADE\)")
    
    
    {  
        "id": "1712544408508",  
        "method": "orderList.place.otoco",  
        "params": {  
            "signature": "c094473304374e1b9c5f7e2558358066cfa99df69f50f63d09cfee755136cb07",  
            "apiKey": "Rf07JlnL9PHVxjs27O5CvKNyOsV4qJ5gXdrRfpvlOdvMZbGZbPO5Ce2nIwfRP0iA",  
            "pendingQuantity": 5,  
            "pendingSide": "SELL",  
            "pendingBelowPrice": 5,  
            "pendingBelowType": "LIMIT_MAKER",  
            "pendingAboveStopPrice": 0.5,  
            "pendingAboveType": "STOP_LOSS",  
            "symbol": "LTCBNB",  
            "recvWindow": "5000",  
            "timestamp": "1712544408509",  
            "workingPrice": 1.5,  
            "workingQuantity": 1,  
            "workingSide": "BUY",  
            "workingTimeInForce": "GTC",  
            "workingType": "LIMIT"  
        }  
    }  
    

Place an OTOCO.

  * An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
  * The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book. 
    * The behavior of the working order is the same as the [OTO](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-list---oto-trade).
  * OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only placed on the order book when the working order gets **fully filled**. 
    * The rules of the pending above and pending below follow the same rules as the [Order list OCO](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-list---oco-trade).
  * OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.



**Weight:** 1

**Unfilled Order Count:** 3

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`listClientOrderId`| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent.   
A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired.   
`listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.  
`newOrderRespType`| ENUM| NO| Format of the JSON response. Supported values: [Order Response Type](/docs/binance-spot-api-docs/enums#orderresponsetype)  
`selfTradePreventionMode`| ENUM| NO| The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
`workingType`| ENUM| YES| Supported values: `LIMIT`, `LIMIT_MAKER`  
`workingSide`| ENUM| YES| Supported values: [Order Side](/docs/binance-spot-api-docs/enums#side)  
`workingClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the working order.  
Automatically generated if not sent.  
`workingPrice`| DECIMAL| YES|   
`workingQuantity`| DECIMAL| YES|   
`workingIcebergQty`| DECIMAL| NO| This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.  
`workingTimeInForce`| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
`workingStrategyId`| LONG| NO| Arbitrary numeric value identifying the working order within an order strategy.  
`workingStrategyType`| INT| NO| Arbitrary numeric value identifying the working order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
`workingPegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`workingPegOffsetType`| ENUM| NO|   
`workingPegOffsetValue`| INT| NO|   
`pendingSide`| ENUM| YES| Supported values: [Order Side](/docs/binance-spot-api-docs/enums#side)  
`pendingQuantity`| DECIMAL| YES|   
`pendingAboveType`| ENUM| YES| Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
`pendingAboveClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the pending above order.  
Automatically generated if not sent.  
`pendingAbovePrice`| DECIMAL| NO| Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.  
`pendingAboveStopPrice`| DECIMAL| NO| Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
`pendingAboveTrailingDelta`| DECIMAL| NO| See [Trailing Stop FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq)  
`pendingAboveIcebergQty`| DECIMAL| NO| This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`.  
`pendingAboveTimeInForce`| ENUM| NO|   
`pendingAboveStrategyId`| LONG| NO| Arbitrary numeric value identifying the pending above order within an order strategy.  
`pendingAboveStrategyType`| INT| NO| Arbitrary numeric value identifying the pending above order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
`pendingAbovePegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingAbovePegOffsetType`| ENUM| NO|   
`pendingAbovePegOffsetValue`| INT| NO|   
`pendingBelowType`| ENUM| NO| Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`  
`pendingBelowClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the pending below order.  
Automatically generated if not sent.  
`pendingBelowPrice`| DECIMAL| NO| Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the limit price.  
`pendingBelowStopPrice`| DECIMAL| NO| Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT or TAKE_PROFIT_LIMIT`.   
Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.  
`pendingBelowTrailingDelta`| DECIMAL| NO|   
`pendingBelowIcebergQty`| DECIMAL| NO| This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`.  
`pendingBelowTimeInForce`| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
`pendingBelowStrategyId`| LONG| NO| Arbitrary numeric value identifying the pending below order within an order strategy.  
`pendingBelowStrategyType`| INT| NO| Arbitrary numeric value identifying the pending below order strategy.   
Values smaller than 1000000 are reserved and cannot be used.  
`pendingBelowPegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingBelowPegOffsetType`| ENUM| NO|   
`pendingBelowPegOffsetValue`| INT| NO|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`timestamp`| LONG| YES|   
`signature`| STRING| YES|   
  
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
  
**Data Source:** Matching Engine

**Response:**
    
    
    {  
        "id": "1712544408508",  
        "status": 200,  
        "result": {  
            "orderListId": 629,  
            "contingencyType": "OTO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "GaeJHjZPasPItFj4x7Mqm6",  
            "transactionTime": 1712544408537,  
            "symbol": "1712544378871",  
            "orders": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 23,  
                    "clientOrderId": "OVQOpKwfmPCfaBTD0n7e7H"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 24,  
                    "clientOrderId": "YcCPKCDMQIjNvLtNswt82X"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 25,  
                    "clientOrderId": "ilpIoShcFZ1ZGgSASKxMPt"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 23,  
                    "orderListId": 629,  
                    "clientOrderId": "OVQOpKwfmPCfaBTD0n7e7H",  
                    "transactTime": 1712544408537,  
                    "price": "1.500000",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "BUY",  
                    "workingTime": 1712544408537,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 24,  
                    "orderListId": 629,  
                    "clientOrderId": "YcCPKCDMQIjNvLtNswt82X",  
                    "transactTime": 1712544408537,  
                    "price": "0.000000",  
                    "origQty": "5.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "PENDING_NEW",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS",  
                    "side": "SELL",  
                    "stopPrice": "0.500000",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 25,  
                    "orderListId": 629,  
                    "clientOrderId": "ilpIoShcFZ1ZGgSASKxMPt",  
                    "transactTime": 1712544408537,  
                    "price": "5.000000",  
                    "origQty": "5.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "PENDING_NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "SELL",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 10000000,  
                "count": 18  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 1000,  
                "count": 65  
            }  
        ]  
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses).

#### OPO (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#opo-trade "Direct link to OPO \(TRADE\)")
    
    
    {  
        "id": "1762941318128",  
        "method": "orderList.place.opo",  
        "params": {  
            "workingPrice": "101496",  
            "workingQuantity": "0.0007",  
            "workingType": "LIMIT",  
            "workingTimeInForce": "GTC",  
            "pendingType": "MARKET",  
            "pendingSide": "SELL",  
            "recvWindow": 5000,  
            "workingSide": "BUY",  
            "symbol": "BTCUSDT",  
            "timestamp": 1762941318129,  
            "apiKey": "aHb4Ur1cK1biW3sgibqUFs39SE58f9d5Xwf4uEW0tFh7ibun5g035QKSktxoOBfE",  
            "signature": "b50ce8977333a78a3bbad21df178d7e104a8c985d19007b55df688cdf868639a"  
        }  
    }  
    

Place an [OPO](/docs/binance-spot-api-docs/faqs/opo).

  * OPOs add 2 orders to the EXCHANGE_MAX_NUM_ORDERS filter and MAX_NUM_ORDERS filter.



**Weight:** 1

**Unfilled Order Count:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`listClientOrderId`| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.  
`newOrderRespType`| ENUM| NO| Format of the JSON response. Supported values: [Order Response Type](/docs/binance-spot-api-docs/enums#orderresponsetype)  
`selfTradePreventionMode`| ENUM| NO| The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
`workingType`| ENUM| YES| Supported values: `LIMIT`,`LIMIT_MAKER`  
`workingSide`| ENUM| YES| Supported values: [Order Side](/docs/binance-spot-api-docs/enums#side)  
`workingClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.  
`workingPrice`| DECIMAL| YES|   
`workingQuantity`| DECIMAL| YES| Sets the quantity for the working order.  
`workingIcebergQty`| DECIMAL| NO| This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.  
`workingTimeInForce`| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
`workingStrategyId`| LONG| NO| Arbitrary numeric value identifying the working order within an order strategy.  
`workingStrategyType`| INT| NO| Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used.  
`workingPegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`workingPegOffsetType`| ENUM| NO|   
`workingPegOffsetValue`| INT| NO|   
`pendingType`| ENUM| YES| Supported values: [Order Types](/docs/binance-spot-api-docs/websocket-api/trading-requests#order-type) Note that `MARKET` orders using `quoteOrderQty` are not supported.  
`pendingSide`| ENUM| YES| Supported values: [Order Side](/docs/binance-spot-api-docs/enums#side)  
`pendingClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.  
`pendingPrice`| DECIMAL| NO|   
`pendingStopPrice`| DECIMAL| NO|   
`pendingTrailingDelta`| DECIMAL| NO|   
`pendingIcebergQty`| DECIMAL| NO| This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.  
`pendingTimeInForce`| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
`pendingStrategyId`| LONG| NO| Arbitrary numeric value identifying the pending order within an order strategy.  
`pendingStrategyType`| INT| NO| Arbitrary numeric value identifying the pending order strategy. Values smaller than 1000000 are reserved and cannot be used.  
`pendingPegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingPegOffsetType`| ENUM| NO|   
`pendingPegOffsetValue`| INT| NO|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`timestamp`| LONG| YES|   
  
**Data Source** : Matching Engine

**Response:**
    
    
    {  
        "id": "1762941318128",  
        "status": 200,  
        "result": {  
            "orderListId": 2,  
            "contingencyType": "OTO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "OiOgqvRagBefpzdM5gjYX3",  
            "transactionTime": 1762941318142,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 2,  
                    "clientOrderId": "pUzhKBbc0ZVdMScIRAqitH"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 3,  
                    "clientOrderId": "x7ISSjywZxFXOdzwsThNnd"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 2,  
                    "orderListId": 2,  
                    "clientOrderId": "pUzhKBbc0ZVdMScIRAqitH",  
                    "transactTime": 1762941318142,  
                    "price": "101496.00000000",  
                    "origQty": "0.00070000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.00000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "BUY",  
                    "workingTime": 1762941318142,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 3,  
                    "orderListId": 2,  
                    "clientOrderId": "x7ISSjywZxFXOdzwsThNnd",  
                    "transactTime": 1762941318142,  
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
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses).

#### OPOCO (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#opoco-trade "Direct link to OPOCO \(TRADE\)")
    
    
    {  
        "id": "1763000139090",  
        "method": "orderList.place.opoco",  
        "params": {  
            "workingPrice": "102496",  
            "workingQuantity": "0.0017",  
            "workingType": "LIMIT",  
            "workingTimeInForce": "GTC",  
            "pendingAboveType": "LIMIT_MAKER",  
            "pendingAbovePrice": "104261",  
            "pendingBelowStopPrice": "10100",  
            "pendingBelowPrice": "101613",  
            "pendingBelowType": "STOP_LOSS_LIMIT",  
            "pendingBelowTimeInForce": "IOC",  
            "pendingSide": "SELL",  
            "recvWindow": 5000,  
            "workingSide": "BUY",  
            "symbol": "BTCUSDT",  
            "timestamp": 1763000139091,  
            "apiKey": "2wiKgTLyllTCu0QWXaEtKWX9tUQ5iQMiDQqTQPdUe2bZ1IVT9aXoS6o19wkYIKl2",  
            "signature": "adfa185c50f793392a54ad5a6e2c39fd34ef6d35944adf2ddd6f30e1866e58d3"  
        }  
    }  
    

Place an [OPOCO](/docs/binance-spot-api-docs/faqs/opo).

**Weight** : 1

**Unfilled Order Count:** 3

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`listClientOrderId`| STRING| NO| Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.  
`newOrderRespType`| ENUM| NO| Format of the JSON response. Supported values: [Order Response Type](/docs/binance-spot-api-docs/enums#orderresponsetype)  
`selfTradePreventionMode`| ENUM| NO| The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes)  
`workingType`| ENUM| YES| Supported values: `LIMIT`, `LIMIT_MAKER`  
`workingSide`| ENUM| YES| Supported values: [Order side](/docs/binance-spot-api-docs/enums#side)  
`workingClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.  
`workingPrice`| DECIMAL| YES|   
`workingQuantity`| DECIMAL| YES|   
`workingIcebergQty`| DECIMAL| NO| This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.  
`workingTimeInForce`| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
`workingStrategyId`| LONG| NO| Arbitrary numeric value identifying the working order within an order strategy.  
`workingStrategyType`| INT| NO| Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used.  
`workingPegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`workingPegOffsetType`| ENUM| NO|   
`workingPegOffsetValue`| INT| NO|   
`pendingSide`| ENUM| YES| Supported values: [Order side](/docs/binance-spot-api-docs/enums#side)  
`pendingAboveType`| ENUM| YES| Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
`pendingAboveClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.  
`pendingAbovePrice`| DECIMAL| NO| Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.  
`pendingAboveStopPrice`| DECIMAL| NO| Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
`pendingAboveTrailingDelta`| DECIMAL| NO| See [Trailing Stop FAQ](/docs/binance-spot-api-docs/faqs/trailing-stop-faq)  
`pendingAboveIcebergQty`| DECIMAL| NO| This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`.  
`pendingAboveTimeInForce`| ENUM| NO|   
`pendingAboveStrategyId`| LONG| NO| Arbitrary numeric value identifying the pending above order within an order strategy.  
`pendingAboveStrategyType`| INT| NO| Arbitrary numeric value identifying the pending above order strategy. Values smaller than 1000000 are reserved and cannot be used.  
`pendingAbovePegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingAbovePegOffsetType`| ENUM| NO|   
`pendingAbovePegOffsetValue`| INT| NO|   
`pendingBelowType`| ENUM| NO| Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`  
`pendingBelowClientOrderId`| STRING| NO| Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.  
`pendingBelowPrice`| DECIMAL| NO| Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify limit price  
`pendingBelowStopPrice`| DECIMAL| NO| Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT or TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.  
`pendingBelowTrailingDelta`| DECIMAL| NO|   
`pendingBelowIcebergQty`| DECIMAL| NO| This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`.  
`pendingBelowTimeInForce`| ENUM| NO| Supported values: [Time In Force](/docs/binance-spot-api-docs/enums#timeinforce)  
`pendingBelowStrategyId`| LONG| NO| Arbitrary numeric value identifying the pending below order within an order strategy.  
`pendingBelowStrategyType`| INT| NO| Arbitrary numeric value identifying the pending below order strategy. Values smaller than 1000000 are reserved and cannot be used.  
`pendingBelowPegPriceType`| ENUM| NO| See [Pegged Orders](/docs/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingBelowPegOffsetType`| ENUM| NO|   
`pendingBelowPegOffsetValue`| INT| NO|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`timestamp`| LONG| YES|   
  
**Data Source** : Matching Engine

**Response:**
    
    
    {  
        "id": "1763000139090",  
        "status": 200,  
        "result": {  
            "orderListId": 1,  
            "contingencyType": "OTO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "TVbG6ymkYMXTj7tczbOsBf",  
            "transactionTime": 1763000139104,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 6,  
                    "clientOrderId": "3czuJSeyjPwV9Xo28j1Dv3"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 7,  
                    "clientOrderId": "kyIKnMLKQclE5FmyYgaMSo"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 8,  
                    "clientOrderId": "i76cGJWN9J1FpADS56TtQZ"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 6,  
                    "orderListId": 1,  
                    "clientOrderId": "3czuJSeyjPwV9Xo28j1Dv3",  
                    "transactTime": 1763000139104,  
                    "price": "102496.00000000",  
                    "origQty": "0.00170000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.00000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "BUY",  
                    "workingTime": 1763000139104,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 7,  
                    "orderListId": 1,  
                    "clientOrderId": "kyIKnMLKQclE5FmyYgaMSo",  
                    "transactTime": 1763000139104,  
                    "price": "101613.00000000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.00000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "PENDING_NEW",  
                    "timeInForce": "IOC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "SELL",  
                    "stopPrice": "10100.00000000",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 8,  
                    "orderListId": 1,  
                    "clientOrderId": "i76cGJWN9J1FpADS56TtQZ",  
                    "transactTime": 1763000139104,  
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
    }  
    

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](/docs/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses).

#### Cancel Order list (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-order-list-trade "Direct link to Cancel Order list \(TRADE\)")
    
    
    {  
        "id": "c5899911-d3f4-47ae-8835-97da553d27d0",  
        "method": "orderList.cancel",  
        "params": {  
            "symbol": "BTCUSDT",  
            "orderListId": 1274512,  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "4973f4b2fee30bf6d45e4a973e941cc60fdd53c8dd5a25edeac96f5733c0ccee",  
            "timestamp": 1660801720210  
        }  
    }  
    

Cancel an active order list.

**Weight** : 1

**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
`symbol` | STRING | YES |   
`orderListId` | INT | YES | Cancel order list by `orderListId`  
`listClientOrderId` | STRING | Cancel order list by `listClientId`  
`newClientOrderId` | STRING | NO | New ID for the canceled order list. Automatically generated if not sent  
`apiKey` | STRING | YES |   
`recvWindow` | DECIMAL | NO | The value cannot be greater than `60000`.  
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`signature` | STRING | YES |   
`timestamp` | LONG | YES |   
  
Notes:

  * If both `orderListId` and `listClientOrderId` parameters are provided, the `orderListId` is searched first, then the `listClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.

  * Canceling an individual order with [`order.cancel`](/docs/binance-spot-api-docs/websocket-api/trading-requests#cancel-order-trade) will cancel the entire order list as well.




**Data Source:** Matching Engine

**Response:**
    
    
    {  
        "id": "c5899911-d3f4-47ae-8835-97da553d27d0",  
        "status": 200,  
        "result": {  
            "orderListId": 1274512,  
            "contingencyType": "OCO",  
            "listStatusType": "ALL_DONE",  
            "listOrderStatus": "ALL_DONE",  
            "listClientOrderId": "6023531d7edaad348f5aff",  
            "transactionTime": 1660801720215,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138901,  
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138902,  
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138901,  
                    "orderListId": 1274512,  
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU",  
                    "transactTime": 1660801720215,  
                    "price": "23410.00000000",  
                    "origQty": "0.00650000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "SELL",  
                    "stopPrice": "23405.00000000",  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138902,  
                    "orderListId": 1274512,  
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us",  
                    "transactTime": 1660801720215,  
                    "price": "23420.00000000",  
                    "origQty": "0.00650000",  
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
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

### SOR[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#sor "Direct link to SOR")

#### Place new order using SOR (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-using-sor-trade "Direct link to Place new order using SOR \(TRADE\)")
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "method": "sor.order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "BUY",  
            "type": "LIMIT",  
            "quantity": 0.5,  
            "timeInForce": "GTC",  
            "price": 31000,  
            "timestamp": 1687485436575,  
            "apiKey": "u5lgqJb97QWXWfgeV4cROuHbReSJM9rgQL0IvYcYc7BVeA5lpAqqc3a5p2OARIFk",  
            "signature": "fd301899567bc9472ce023392160cdc265ad8fcbbb67e0ea1b2af70a4b0cd9c7"  
        }  
    }  
    

Places an order using smart order routing (SOR).

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [SOR FAQ](/docs/binance-spot-api-docs/faqs/sor_faq) to learn more.

**Weight:** 1

**Unfilled Order Count:** 1

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
`symbol`| STRING| YES|   
`side`| ENUM| YES| `BUY` or `SELL`  
`type`| ENUM| YES|   
`timeInForce`| ENUM| NO| Applicable only to `LIMIT` order type  
`price`| DECIMAL| NO| Applicable only to `LIMIT` order type  
`quantity`| DECIMAL| YES|   
`newClientOrderId`| STRING| NO| Arbitrary unique ID among open orders. Automatically generated if not sent  
`newOrderRespType`| ENUM| NO| Select response format: `ACK`, `RESULT`, `FULL`.`MARKET` and `LIMIT` orders use `FULL` by default.  
`icebergQty`| DECIMAL| NO|   
`strategyId`| LONG| NO| Arbitrary numeric value identifying the order within an order strategy.  
`strategyType`| INT| NO| Arbitrary numeric value identifying the order strategy.Values smaller than `1000000` are reserved and cannot be used.  
`selfTradePreventionMode`| ENUM| NO| The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](/docs/binance-spot-api-docs/enums#stpmodes).  
`apiKey`| STRING| YES|   
`timestamp`| LONG| YES|   
`recvWindow`| DECIMAL| NO| The value cannot be greater than `60000`.   
Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.  
`signature`| STRING| YES|   
  
**Note:** `sor.order.place` only supports `LIMIT` and `MARKET` orders. `quoteOrderQty` is not supported.

**Data Source:** Matching Engine

**Response:**
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "status": 200,  
        "result": [  
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
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

#### Test new order using SOR (TRADE)[​](/docs/binance-spot-api-docs/websocket-api/trading-requests#test-new-order-using-sor-trade "Direct link to Test new order using SOR \(TRADE\)")
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "method": "sor.order.test",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "BUY",  
            "type": "LIMIT",  
            "quantity": 0.1,  
            "timeInForce": "GTC",  
            "price": 0.1,  
            "timestamp": 1687485436575,  
            "apiKey": "u5lgqJb97QWXWfgeV4cROuHbReSJM9rgQL0IvYcYc7BVeA5lpAqqc3a5p2OARIFk",  
            "signature": "fd301899567bc9472ce023392160cdc265ad8fcbbb67e0ea1b2af70a4b0cd9c7"  
        }  
    }  
    

Test new order creation and signature/recvWindow using smart order routing (SOR). Creates and validates a new order but does not send it into the matching engine.

**Weight:**

Condition| Request Weight  
---|---  
Without `computeCommissionRates`| 1  
With `computeCommissionRates`| 20  
  
**Parameters:**

In addition to all parameters accepted by [`sor.order.place`](/docs/binance-spot-api-docs/websocket-api/trading-requests#place-new-order-using-sor-trade), the following optional parameters are also accepted:

Name| Type| Mandatory| Description  
---|---|---|---  
`computeCommissionRates`| BOOLEAN| NO| Default: `false`  
  
**Data Source:** Memory

**Response:**

Without `computeCommissionRates`:
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "status": 200,  
        "result": {},  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

With `computeCommissionRates`:
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "status": 200,  
        "result": {  
            "standardCommissionForOrder": {  // Commission rates for the order depending on its role (e.g. maker or taker)  
                "maker": "0.00000112",  
                "taker": "0.00000114"  
            },  
            "taxCommissionForOrder": {       // Tax deduction rates for the order depending on its role (e.g. maker or taker)  
                "maker": "0.00000112",  
                "taker": "0.00000114"  
            },  
            "discount": {                    // Discount on standard commissions when paying in BNB.  
                "enabledForAccount": true,  
                "enabledForSymbol": true,  
                "discountAsset": "BNB",  
                "discount": "0.25"           // Standard commission is reduced by this rate when paying in BNB.  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 20  
            }  
        ]  
    }

---

# 交易请求

### 下新的订单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#下新的订单-trade "下新的订单 \(TRADE\)的直接链接")
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "price": "23416.10000000",  
            "quantity": "0.00847000",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",  
            "timestamp": 1660801715431  
        }  
    }  
    

下新的订单。

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

**权重:** 1

**未成交的订单计数:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`side`| ENUM| YES| `BUY` 或者 `SELL`  
`type`| ENUM| YES|   
`timeInForce`| ENUM| NO *|   
`price`| DECIMAL| NO *|   
`quantity`| DECIMAL| NO *|   
`quoteOrderQty`| DECIMAL| NO *|   
`newClientOrderId`| STRING| NO| 客户自定义的唯一订单ID。如果未发送，则自动生成。  
`newOrderRespType`| ENUM| NO| 可选的响应格式: `ACK`，`RESULT`，`FULL`.`MARKET`和`LIMIT`订单默认使用`FULL`，其他订单类型默认使用`ACK`。  
`stopPrice`| DECIMAL| NO *|   
`trailingDelta`| INT| NO *| 请看 [Trailing Stop order FAQ](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)  
`icebergQty`| DECIMAL| NO|   
`strategyId`| LONG| NO| 标识订单策略中订单的任意ID。  
`strategyType`| INT| NO| 标识订单策略的任意数值。小于`1000000`的值是保留的，不能使用。  
`selfTradePreventionMode`| ENUM| NO| 允许的 ENUM 取决于交易对的配置。支持值：[STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
`pegPriceType`| ENUM| NO| `PRIMARY_PEG` 或 `MARKET_PEG`   
参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pegOffsetValue`| INT| NO| 用于挂钩的价格水平（最大值：100）   
参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pegOffsetType`| ENUM| NO| 仅支持 `PRICE_LEVEL`   
参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`signature`| STRING| YES|   
`timestamp`| LONG| YES|   
  
根据订单 `type`，某些参数(*) 可能成为必需参数:

订单 `type` | 强制要求的参数  
---|---  
`LIMIT` | 

  * `timeInForce`
  * `price`
  * `quantity`

  
`LIMIT_MAKER` | 

  * `price`
  * `quantity`

  
`MARKET` | 

  * `quantity` 或者 `quoteOrderQty`

  
`STOP_LOSS` | 

  * `quantity`
  * `stopPrice` 或者 `trailingDelta`

  
`STOP_LOSS_LIMIT` | 

  * `timeInForce`
  * `price`
  * `quantity`
  * `stopPrice` 或者 `trailingDelta`

  
`TAKE_PROFIT` | 

  * `quantity`
  * `stopPrice` 或者 `trailingDelta`

  
`TAKE_PROFIT_LIMIT` | 

  * `timeInForce`
  * `price`
  * `quantity`
  * `stopPrice` 或者 `trailingDelta`

  
  
支持的订单类型：

订单 `type` | 描述  
---|---  
`LIMIT` |  以指定的 `price` 或更好的 `price`, 买入或卖出 `quantity`。   
`LIMIT_MAKER` |  `LIMIT` 订单，如果它立即匹配并成为吃单方将被拒绝。  此订单类型也称为 POST-ONLY 订单。   
`MARKET` |  以最佳市场价格买入或卖出。 

  * 带有 `quantity` 参数的 `MARKET` 订单指定您要BUY或SELL的 _base asset_ 的数量。 报价资产的实际执行quantity将取决于可用的市场流动性。  例如，在 BTCUSDT 下` "quantity": "0.1000" ` 的市场买单，指定您想以最优惠的价格 BUY 0.1 BTC。 如果以最优价格没有足够的 BTC，会继续以次优价格买入，直到您的订单被执行，或者您的 USDT 用完，或者市场上的 BTC 用完。 
  * 使用 `quoteOrderQty` 的 `MARKET` 订单 明确的是通过买入(或卖出)想要花费(或获取)的 _quote asset_ 数量。 基础资产的实际执行数量将取决于可用的市场流动性。  例如，在 BTCUSDT 下 ` "quoteOrderQty": "100.00" ` 的市场买单，指定您想以最优惠的价格以 100 USDT 购买尽可能多的 BTC。 同样，卖出订单将卖出尽可能多的可用 BTC，以便您获得 100 USDT（佣金前）。 

  
`STOP_LOSS` |  当满足指定条件时，执行给定 `quantity` 的 `MARKET` 订单。  I.e., 当达到 `stopPrice` 或激活 `trailingDelta` 时。   
`STOP_LOSS_LIMIT` |  当满足指定条件时，执行给定参数的 `LIMIT` 订单。   
`TAKE_PROFIT` |  与 `STOP_LOSS` 类似，但在市场价格向有利方向移动时激活。   
`TAKE_PROFIT_LIMIT` |  与 `STOP_LOSS_LIMIT` 类似，但在市场价格向有利方向移动时激活。   
  
关于挂钩订单参数的注意事项：

  * 这些参数仅适用于 `LIMIT`， `LIMIT_MAKER`， `STOP_LOSS_LIMIT` 和 `TAKE_PROFIT_LIMIT` 订单。
  * 如果使用了 `pegPriceType`， 那么 `price` 字段将是可选的。 否则，`price` 字段依旧是必须的。
  * `pegPriceType=PRIMARY_PEG` 就是主要挂钩（`primary`），这是订单簿上与您的订单同一方向的最佳价格。
  * `pegPriceType=MARKET_PEG` 就是市场挂钩（`market`），这是订单簿上与您的订单相反方向的最佳价格。
  * 可以通过使用 `pegOffsetType` 和 `pegOffsetValue` 来获取最佳价格以外的价格水平。 这两个参数必须一起使用。



可用的 `timeInForce` 选项，设置订单在到期前应该活跃多长时间：

TIF| 描述  
---|---  
`GTC`| **Good 'til Canceled** – 成交为止。订单会一直有效，直到被成交或者取消。  
`IOC`| **Immediate 或者 Cancel** – 无法立即成交的部分就撤销。订单在失效前会尽量多的成交。  
`FOK`| **Fill 或者 Kill** – 无法全部立即成交就撤销。如果无法全部成交，订单会失效。  
  
备注：

  * `newClientOrderId` 指定订单的 `clientOrderId` 值。

仅当前一个订单已成交或过期时，才会接受具有相同 `clientOrderId` 的新订单。

  * 任何 `LIMIT` 或 `LIMIT_MAKER` 订单都可以通过指定 `icebergQty` 变成冰山订单。

带有 `icebergQty` 的订单必须将 `timeInForce` 设置为 `GTC`。

  * `STOP_LOSS`/`TAKE_PROFIT` 订单的触发订单价格规则：

    * `stopPrice` 必须高于市场价格：`STOP_LOSS BUY`，`TAKE_PROFIT SELL`
    * `stopPrice` 必须低于市场价格：`STOP_LOSS SELL`，`TAKE_PROFIT BUY`
  * 使用 `quoteOrderQty` 的 `MARKET` 订单遵循 [`LOT_SIZE`](/docs/zh-CN/binance-spot-api-docs/filters#lot_size) 过滤规则。

该订单将执行一个名义价值尽可能接近请求的 `quoteOrderQty` 的数量。




**数据源:** 撮合引擎

**响应:** 使用 `newOrderRespType` 参数可以选择响应格式。

`ACK` 响应类型：
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12569099453,  
            "orderListId": -1, // 单个订单会一直是 -1  
            "clientOrderId": "4d96324ff9d44481926157ec08158a40",  
            "transactTime": 1660801715639  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

`RESULT` 响应类型：
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12569099453,  
            "orderListId": -1, // 单个订单会一直是 -1  
            "clientOrderId": "4d96324ff9d44481926157ec08158a40",  
            "transactTime": 1660801715639,  
            "price": "23416.10000000",  
            "origQty": "0.00847000",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL",  
            "workingTime": 1660801715639,  
            "selfTradePreventionMode": "NONE"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

`FULL` 响应类型：
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12569099453,  
            "orderListId": -1,  
            "clientOrderId": "4d96324ff9d44481926157ec08158a40",  
            "transactTime": 1660801715793,  
            "price": "23416.10000000",  
            "origQty": "0.00847000",  
            "executedQty": "0.00847000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "198.33521500",  
            "status": "FILLED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL",  
            "workingTime": 1660801715639,  
            // FULL 响应与 RESULT 响应相同，具有相同的可选字段基于订单类型和参数。FULL响应还包括立即完成订单的交易列表。  
            "fills": [  
                {  
                    "price": "23416.10000000",  
                    "qty": "0.00635000",  
                    "commission": "0.000000",  
                    "commissionAsset": "BNB",  
                    "tradeId": 1650422481  
                },  
                {  
                    "price": "23416.50000000",  
                    "qty": "0.00212000",  
                    "commission": "0.000000",  
                    "commissionAsset": "BNB",  
                    "tradeId": 1650422482  
                }  
            ],  
            "selfTradePreventionMode": "NONE"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
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
`usedSor`| 用于确定订单是否使用`SOR`的字段| 在使用`SOR`下单时出现| `"usedSor": true`  
`workingFloor`| 用以定义订单是通过 SOR 还是由订单提交到的订单簿（order book）成交的。| 出现在使用了 SOR 的订单中。| `"workingFloor": "SOR"`  
`pegPriceType`| 挂钩价格类型| 仅用于挂钩订单| `"pegPriceType": "PRIMARY_PEG"`  
`pegOffsetType`| 挂钩价格偏移类型| 如若需要，仅用于挂钩订单| `"pegOffsetType": "PRICE_LEVEL"`  
`pegOffsetValue`| 挂钩价格偏移值| 如若需要，仅用于挂钩订单| `"pegOffsetValue": 5`  
`peggedPrice`| 订单对应的当前挂钩价格| 一旦确定，仅用于挂钩订单| `"peggedPrice": "87523.83710000"`  
`expiryReason`| 订单失效原因| 当订单失效时| `"expiryReason": "INSUFFICIENT_LIQUIDITY"`  
  
### 测试下单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#测试下单-trade "测试下单 \(TRADE\)的直接链接")
    
    
    {  
        "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",  
        "method": "order.test",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "price": "23416.10000000",  
            "quantity": "0.00847000",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",  
            "timestamp": 1660801715431  
        }  
    }  
    

测试下单。

验证新订单参数并验证您的签名但不会将订单发送到撮合引擎。

**权重:**

条件| 请求权重  
---|---  
没有 `computeCommissionRates`| 1  
有 `computeCommissionRates`| 20  
  
**参数:**

除了 [`order.place`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-place) 的所有参数, 下面参数也有效:

参数名| 类型| 是否必需| 描述  
---|---|---|---  
`computeCommissionRates`| BOOLEAN| NO| 默认值： `false`   
请参阅[佣金常见问题解答](/docs/zh-CN/binance-spot-api-docs/faqs/commission_faq#test-order-diferences) 了解更多信息。  
  
**数据源:** 缓存

**响应:**

没有 `computeCommissionRates`:
    
    
    {  
        "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",  
        "status": 200,  
        "result": {},  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

有 `computeCommissionRates`:
    
    
    {  
        "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",  
        "status": 200,  
        "result": {  
            "standardCommissionForOrder": {  // 根据订单的角色（例如，Maker或Taker）确定的佣金费率。  
                "maker": "0.00000112",  
                "taker": "0.00000114"  
            },  
            "specialCommissionForOrder": {   // 根据订单的角色（例如，Maker或Taker）确定的特殊佣金率。  
                "maker": "0.05000000",  
                "taker": "0.06000000"  
            },  
            "taxCommissionForOrder": {       // 根据订单的角色（例如，Maker或Taker）确定的税收扣除率。  
                "maker": "0.00000112",  
                "taker": "0.00000114"  
            },  
            "discount": {                    // 以BNB支付时的标准佣金折扣。  
                "enabledForAccount": true,  
                "enabledForSymbol": true,  
                "discountAsset": "BNB",  
                "discount": "0.25000000"     // 当用BNB支付佣金时，在标准佣金上按此比率打折。  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 20  
            }  
        ]  
    }  
    

### 撤销订单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#撤销订单-trade "撤销订单 \(TRADE\)的直接链接")
    
    
    {  
        "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
        "method": "order.cancel",  
        "params": {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "4d96324ff9d44481926157",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "33d5b721f278ae17a52f004a82a6f68a70c68e7dd6776ed0be77a455ab855282",  
            "timestamp": 1660801715830  
        }  
    }  
    

取消有效订单。

**权重:** 1

**参数:**

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`symbol` | STRING | YES |   
`orderId` | LONG | YES | 按 `orderId` 取消订单  
`origClientOrderId` | STRING | 按 `clientOrderId` 取消订单  
`newClientOrderId` | STRING | NO | 已取消订单的新 ID。如果未发送，则自动生成  
`cancelRestrictions` | ENUM | NO | 支持的值:   
`ONLY_NEW` \- 如果订单状态为 `NEW`，撤销将成功。  
`ONLY_PARTIALLY_FILLED` \- 如果订单状态为 `PARTIALLY_FILLED`，撤销将成功。  
`apiKey` | STRING | YES |   
`recvWindow` | DECIMAL | NO | 值不能大于 `60000`。  
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`signature` | STRING | YES |   
`timestamp` | LONG | YES |   
  
备注：

  * 当同时提供 `orderId` 和 `origClientOrderId` 两个参数时，系统首先将会使用 `orderId` 来搜索订单。然后， 查找结果中的 `origClientOrderId` 的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。

  * `newClientOrderId` 将替换已取消订单的 `clientOrderId`，为新订单腾出空间。

  * 如果您取消属于订单列表的订单，则整个订单列表将被取消。

  * 当仅发送 `orderId` 时,取消订单的执行(单个 Cancel 或作为 Cancel-Replace 的一部分)总是更快。发送 `origClientOrderId` 或同时发送 `orderId` \+ `origClientOrderId` 会稍慢。




**数据源:** 撮合引擎

**响应:**

取消单个订单时：
    
    
    {  
        "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "origClientOrderId": "4d96324ff9d44481926157",     // 被取消的 clientOrderId  
            "orderId": 12569099453,  
            "orderListId": -1,                                 // 订单列表的ID，不然就是 -1  
            "clientOrderId": "91fe37ce9e69c90d6358c0",         // 请求的 newClientOrderId  
            "transactTime": 1684804350068,  
            "price": "23416.10000000",  
            "origQty": "0.00847000",  
            "executedQty": "0.00001000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.23416100",  
            "status": "CANCELED",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "SELL",  
            "stopPrice": "0.00000000",                         // 如果订单设置了 stopPrice 会出现  
            "trailingDelta": 0,                                // 如果订单设置了 trailingDelta 会出现  
            "icebergQty": "0.00000000",                        // 如果订单设置了 icebergQty 会出现  
            "strategyId": 37463720,                            // 如果订单设置了 strategyId 会出现  
            "strategyType": 1000000,                           // 如果订单设置了 strategyType 会出现  
            "selfTradePreventionMode": "NONE"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 2  
            }  
        ]  
    }  
    

取消订单列表时：
    
    
    {  
        "id": "16eaf097-bbec-44b9-96ff-e97e6e875870",  
        "status": 200,  
        "result": {  
            "orderListId": 19431,  
            "contingencyType": "OCO",  
            "listStatusType": "ALL_DONE",  
            "listOrderStatus": "ALL_DONE",  
            "listClientOrderId": "iuVNVJYYrByz6C4yGOPPK0",  
            "transactionTime": 1660803702431,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569099453,  
                    "clientOrderId": "bX5wROblo6YeDwa9iTLeyY"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569099454,  
                    "clientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW"  
                }  
            ],  
            // 订单列表的状态格式与单个订单相同。  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "bX5wROblo6YeDwa9iTLeyY",  
                    "orderId": 12569099453,  
                    "orderListId": 19431,  
                    "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",  
                    "transactTime": 1684804350068,  
                    "price": "23450.50000000",  
                    "origQty": "0.00850000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "BUY",  
                    "stopPrice": "23430.00000000",  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW",  
                    "orderId": 12569099454,  
                    "orderListId": 19431,  
                    "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",  
                    "transactTime": 1684804350068,  
                    "price": "23400.00000000",  
                    "origQty": "0.00850000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "BUY",  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses) 部分。

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
    

### 撤消挂单再下单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#撤消挂单再下单-trade "撤消挂单再下单 \(TRADE\)的直接链接")
    
    
    {  
        "id": "99de1036-b5e2-4e0f-9b5c-13d751c93a1a",  
        "method": "order.cancelReplace",  
        "params": {  
            "symbol": "BTCUSDT",  
            "cancelReplaceMode": "ALLOW_FAILURE",  
            "cancelOrigClientOrderId": "4d96324ff9d44481926157",  
            "side": "SELL",  
            "type": "LIMIT",  
            "timeInForce": "GTC",  
            "price": "23416.10000000",  
            "quantity": "0.00847000",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "7028fdc187868754d25e42c37ccfa5ba2bab1d180ad55d4c3a7e2de643943dc5",  
            "timestamp": 1660813156900  
        }  
    }  
    

  * 撤消一个现有订单，并立即重新下单。
  * 即使新订单未被尝试（即 `newOrderResult: NOT_ATTEMPTED`），未成交订单数量仍会增加1。
  * 通过此接口只能撤消订单列表中的单个订单，但结果与撤消整个订单列表相同。



**权重:** 1

**未成交的订单计数:** 1

**参数:**

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`symbol` | STRING | YES |   
`cancelReplaceMode` | ENUM | YES |   
`cancelOrderId` | LONG | YES | 按 `orderId` 取消订单  
`cancelOrigClientOrderId` | STRING | 按 `clientOrderId` 取消订单  
`cancelNewClientOrderId` | STRING | NO | 已取消订单的新 ID。如果未发送，则自动生成  
`side` | ENUM | YES | `BUY` 或者 `SELL`  
`type` | ENUM | YES |   
`timeInForce` | ENUM | NO * |   
`price` | DECIMAL | NO * |   
`quantity` | DECIMAL | NO * |   
`quoteOrderQty` | DECIMAL | NO * |   
`newClientOrderId` | STRING | NO | 客户自定义的唯一订单ID。如果未发送，则自动生成  
`newOrderRespType` | ENUM | NO |  选择响应格式： `ACK`, `RESULT`, `FULL`。 `MARKET` 和 `LIMIT` 订单默认推送 `FULL` 响应， 其他订单类型默认为 `ACK`。   
`stopPrice` | DECIMAL | NO * |   
`trailingDelta` | DECIMAL | NO * | 请看 [Trailing Stop order FAQ](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)  
`icebergQty` | DECIMAL | NO |   
`strategyId` | LONG | NO | 标识订单策略中订单的任意ID。  
`strategyType` | INT | NO |  标识订单策略的任意数值。 小于 `1000000` 的值被保留，不能使用。  
`selfTradePreventionMode` | ENUM | NO |  允许的 ENUM 取决于交易对的配置。 支持的值有： [STP 模式](/docs/zh-CN/binance-spot-api-docs/enums.md#stpmodes)。  
`cancelRestrictions` | ENUM | NO | 支持的值:   
`ONLY_NEW` \- 如果订单状态为 `NEW`，撤销将成功。  
`ONLY_PARTIALLY_FILLED` \- 如果订单状态为 `PARTIALLY_FILLED`，撤销将成功。  
`apiKey` | STRING | YES |   
`orderRateLimitExceededMode` | ENUM | NO | 支持的值：   
`DO_NOTHING` （默认值） - 仅在账户未超过未成交订单频率限制时，会尝试取消订单。  
`CANCEL_ONLY` \- 将始终取消订单。  
`pegPriceType` | ENUM | NO | `PRIMARY_PEG` 或 `MARKET_PEG`。   
参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)"  
`pegOffsetValue` | INT | NO | 用于价格挂钩的价格水平（最大值：100）   
参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pegOffsetType` | ENUM | NO | 仅支持 `PRICE_LEVEL`   
参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`recvWindow` | DECIMAL | NO | 值不能大于 `60000`。  
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`signature` | STRING | YES |   
`timestamp` | LONG | YES |   
  
类似于 [`order.place`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-place) 请求，额外的强制参数 (*) 由新订单的 [`type`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-type) 确定。

可用的 `cancelReplaceMode` 选项：

  * `STOP_ON_FAILURE` – 如果撤销订单请求失败，将不会尝试下新订单。
  * `ALLOW_FAILURE` – 即使撤销订单请求失败，也会尝试下新订单。

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
超出限制范围 | ✅ `SUCCESS` | ✅ `SUCCESS` | `200`  
❌ `FAILURE` | ❌ `FAILURE` | `400`  
❌ `FAILURE` | ✅ `SUCCESS` | N/A  
✅ `SUCCESS` | ❌ `FAILURE` | `409`  
  
备注：

  * 当同时提供 `cancelOrderId` 和 `cancelOrigClientOrderId` 两个参数时，系统首先将会使用 `cancelOrderId` 来搜索订单。然后， 查找结果中的 `cancelOrigClientOrderId` 的值将会被用来验证订单。如果两个条件都不满足，则请求将被拒绝。

  * `cancelNewClientOrderId` 将替换已撤销订单的 `clientOrderId`，为新订单腾出空间。

  * `newClientOrderId` 指定下单的 `clientOrderId` 值。

仅当前一个订单已成交或过期时，才会接受具有相同 `clientOrderId` 的新订单。

新订单可以重用已取消订单的旧 `clientOrderId`。

  * 此 cancel-replace 操作**不是事务性的** 。

如果一个操作成功但另一个操作失败，则仍然执行成功的操作。

例如，在 `STOP_ON_FAILURE` 模式下，如果下新订单达失败，旧订单仍然被撤销。

  * 过滤器和订单次数限制会在撤销和下订单之前评估。

  * 如果未尝试下新订单，订单次数仍会增加。

  * 与 [`order.cancel`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-cancel) 一样，如果您撤销订单列表内的某个订单，则整个订单列表将被撤销。

  * 当仅发送 `orderId` 时,取消订单的执行(单个 Cancel 或作为 Cancel-Replace 的一部分)总是更快。发送 `origClientOrderId` 或同时发送 `orderId` \+ `origClientOrderId` 会稍慢。




**数据源:** 撮合引擎

**响应:**

如果撤销订单和下新订单都成功，响应会是 `"status": 200`：
    
    
    {  
        "id": "99de1036-b5e2-4e0f-9b5c-13d751c93a1a",  
        "status": 200,  
        "result": {  
            "cancelResult": "SUCCESS",  
            "newOrderResult": "SUCCESS",  
            // 格式与 "order.cancel" 格式相同。  
            // 某些字段是可选的，仅在订单中有设置它们时才包括。  
            "cancelResponse": {  
                "symbol": "BTCUSDT",  
                "origClientOrderId": "4d96324ff9d44481926157",     // 请求的 cancelOrigClientOrderId  
                "orderId": 125690984230,  
                "orderListId": -1,  
                "clientOrderId": "91fe37ce9e69c90d6358c0",         // 请求的 cancelNewClientOrderId  
                "transactTime": 1684804350068,  
                "price": "23450.00000000",  
                "origQty": "0.00847000",  
                "executedQty": "0.00001000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.23450000",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "selfTradePreventionMode": "NONE"  
            },  
            // 格式与 "order.place" 格式相同, 受 "newOrderRespType" 影响。  
            // 某些字段是可选的，仅在订单中有设置它们时才包括。  
            "newOrderResponse": {  
                "symbol": "BTCUSDT",  
                "orderId": 12569099453,  
                "orderListId": -1,  
                "clientOrderId": "bX5wROblo6YeDwa9iTLeyY",         // 请求的 newClientOrderId  
                "transactTime": 1660813156959,  
                "price": "23416.10000000",  
                "origQty": "0.00847000",  
                "executedQty": "0.00000000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "selfTradePreventionMode": "NONE"  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

在 `STOP_ON_FAILURE` 模式，失败的撤销订单会阻止下新订单，响应会是`"status": 400`：
    
    
    {  
        "id": "27e1bf9f-0539-4fb0-85c6-06183d36f66c",  
        "status": 400,  
        "error": {  
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
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

如果 cancel-replace 模式允许失败并且其中一个操作失败，响应会是 `"status": 409` 和 `"data"` 字段会制定哪个操作成功，哪个失败，以及原因：
    
    
    {  
        "id": "b220edfe-f3c4-4a3a-9d13-b35473783a25",  
        "status": 409,  
        "error": {  
            "code": -2021,  
            "msg": "Order cancel-replace partially failed.",  
            "data": {  
                "cancelResult": "SUCCESS",  
                "newOrderResult": "FAILURE",  
                "cancelResponse": {  
                    "symbol": "BTCUSDT",  
                    "origClientOrderId": "4d96324ff9d44481926157",  
                    "orderId": 125690984230,  
                    "orderListId": -1,  
                    "clientOrderId": "91fe37ce9e69c90d6358c0",  
                    "transactTime": 1684804350068,  
                    "price": "23450.00000000",  
                    "origQty": "0.00847000",  
                    "executedQty": "0.00001000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.23450000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "SELL",  
                    "selfTradePreventionMode": "NONE"  
                },  
                "newOrderResponse": {  
                    "code": -2010,  
                    "msg": "Order would immediately match and take."  
                }  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    
    
    
    {  
        "id": "ce641763-ff74-41ac-b9f7-db7cbe5e93b1",  
        "status": 409,  
        "error": {  
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
                    "orderId": 12569099453,  
                    "orderListId": -1,  
                    "clientOrderId": "bX5wROblo6YeDwa9iTLeyY",  
                    "transactTime": 1660813156959,  
                    "price": "23416.10000000",  
                    "origQty": "0.00847000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "SELL",  
                    "selfTradePreventionMode": "NONE"  
                }  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

如果两个操作都失败，响应将有 `"status": 400`：
    
    
    {  
        "id": "3b3ac45c-1002-4c7d-88e8-630c408ecd87",  
        "status": 400,  
        "error": {  
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
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 1  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 1  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

如果 `orderRateLimitExceededMode` 是 `DO_NOTHING`，那么无论 `cancelReplaceMode` 的取值，当账户超出未成交订单计数时，响应将有 `"status": 429`:
    
    
    {  
        "id": "3b3ac45c-1002-4c7d-88e8-630c408ecd87",  
        "status": 429,  
        "error": {  
            "code": -1015,  
            "msg": "Too many new orders; current limit is 50 orders per 10 SECOND."  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 50  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 50  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

如果 `orderRateLimitExceededMode` 是 `CANCEL_ONLY`，那么无论 `cancelReplaceMode` 的取值，当账户超出未成交订单计数时，响应将有 `"status": 409`:
    
    
    {  
        "id": "3b3ac45c-1002-4c7d-88e8-630c408ecd87",  
        "status": 409,  
        "error": {  
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
                    "msg": "Too many new orders; current limit is 50 orders per 10 SECOND."  
                }  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 50  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 50  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses) 部分。

### 修改订单并保留优先级 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#修改订单并保留优先级-trade "修改订单并保留优先级 \(TRADE\)的直接链接")
    
    
    {  
        "id": "56374a46-3061-486b-a311-89ee972eb648",  
        "method": "order.amend.keepPriority",  
        "params": {  
            "newQty": "5",  
            "origClientOrderId": "my_test_order1",  
            "recvWindow": 5000,  
            "symbol": "BTCUSDT",  
            "timestamp": 1741922620419,  
            "apiKey": "Rl1KOMDCpSg6xviMYOkNk9ENUB5QOTnufXukVe0Ijd40yduAlpHn78at3rJyJN4F",  
            "signature": "fa49c0c4ebc331c6ebd3fcb20deb387f60081ea858eebe6e35aa6fcdf2a82e08"  
        }  
    }  
    

由客户发送以减少其现有当前挂单的原始数量。

这个请求会把0个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

请阅读 [保留优先权的修改订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/order_amend_keep_priority) 了解更多信息。

**权重:** 4

**未成交的订单计数:** 0

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`orderId`| LONG| NO*| 需提供 `orderId` 或 `origClientOrderId`。  
`origClientOrderId`| STRING| NO*| 需提供 `orderId` 或 `origClientOrderId`。  
`newClientOrderId`| STRING| NO*| 订单在被修改后被赋予的新 client order ID。   
如果未发送则自动生成。   
可以将当前 clientOrderId 作为 `newClientOrderId` 发送来重用当前 clientOrderId 的值。  
`newQty`| DECIMAL| YES| 交易的新数量。 `newQty` 必须大于0, 但是必须比订单的原始数量小。  
`recvWindow`| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`timestamp`| LONG| NO|   
  
**数据源:** 撮合引擎

**响应:**

来自单个订单的响应：
    
    
    {  
        "id": "56374a46-3061-486b-a311-89ee972eb648",  
        "status": 200,  
        "result": {  
            "transactTime": 1741923284382,  
            "executionId": 16,  
            "amendedOrder": {  
                "symbol": "BTCUSDT",  
                "orderId": 12,  
                "orderListId": -1,  
                "origClientOrderId": "my_test_order1",  
                "clientOrderId": "4zR9HFcEq8gM1tWUqPEUHc",  
                "price": "5.00000000",  
                "qty": "5.00000000",  
                "executedQty": "0.00000000",  
                "preventedQty": "0.00000000",  
                "quoteOrderQty": "0.00000000",  
                "cumulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "BUY",  
                "workingTime": 1741923284364,  
                "selfTradePreventionMode": "NONE"  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

来自订单列表中单个订单的响应：
    
    
    {  
        "id": "56374b46-3061-486b-a311-89ee972eb648",  
        "status": 200,  
        "result": {  
            "transactTime": 1741924229819,  
            "executionId": 60,  
            "amendedOrder": {  
                "symbol": "BTUCSDT",  
                "orderId": 23,  
                "orderListId": 4,  
                "origClientOrderId": "my_pending_order",  
                "clientOrderId": "xbxXh5SSwaHS7oUEOCI88B",  
                "price": "1.00000000",  
                "qty": "5.00000000",  
                "executedQty": "0.00000000",  
                "preventedQty": "0.00000000",  
                "quoteOrderQty": "0.00000000",  
                "cumulativeQuoteQty": "0.00000000",  
                "status": "NEW",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "BUY",  
                "workingTime": 1741924204920,  
                "selfTradePreventionMode": "NONE"  
            },  
            "listStatus": {  
                "orderListId": 4,  
                "contingencyType": "OTO",  
                "listOrderStatus": "EXECUTING",  
                "listClientOrderId": "8nOGLLawudj1QoOiwbroRH",  
                "symbol": "BTCUSDT",  
                "orders": [  
                    {  
                        "symbol": "BTCUSDT",  
                        "orderId": 22,  
                        "clientOrderId": "g04EWsjaackzedjC9wRkWD"  
                    },  
                    {  
                        "symbol": "BTCUSDT",  
                        "orderId": 23,  
                        "clientOrderId": "xbxXh5SSwaHS7oUEOCI88B"  
                    }  
                ]  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses) 部分。

### 撤销单一交易对的所有挂单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#撤销单一交易对的所有挂单-trade "撤销单一交易对的所有挂单 \(TRADE\)的直接链接")
    
    
    {  
        "id": "778f938f-9041-4b88-9914-efbf64eeacc8",  
        "method": "openOrders.cancelAll",  
        "params": {  
            "symbol": "BTCUSDT",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "773f01b6e3c2c9e0c1d217bc043ce383c1ddd6f0e25f8d6070f2b66a6ceaf3a5",  
            "timestamp": 1660805557200  
        }  
    }  
    

撤销单一交易对的所有挂单,包括交易组。

**权重:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`signature`| STRING| YES|   
`timestamp`| LONG| YES|   
  
**数据源:** 撮合引擎

**响应:**

订单和订单列表的撤销报告的格式与 [`order.cancel`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-cancel) 中的格式相同。
    
    
    {  
        "id": "778f938f-9041-4b88-9914-efbf64eeacc8",  
        "status": 200,  
        "result": [  
            {  
                "symbol": "BTCUSDT",  
                "origClientOrderId": "4d96324ff9d44481926157",  
                "orderId": 12569099453,  
                "orderListId": -1,  
                "clientOrderId": "91fe37ce9e69c90d6358c0",  
                "transactTime": 1684804350068,  
                "price": "23416.10000000",  
                "origQty": "0.00847000",  
                "executedQty": "0.00001000",  
                "origQuoteOrderQty": "0.000000",  
                "cummulativeQuoteQty": "0.23416100",  
                "status": "CANCELED",  
                "timeInForce": "GTC",  
                "type": "LIMIT",  
                "side": "SELL",  
                "stopPrice": "0.00000000",  
                "trailingDelta": 0,  
                "trailingTime": -1,  
                "icebergQty": "0.00000000",  
                "strategyId": 37463720,  
                "strategyType": 1000000,  
                "selfTradePreventionMode": "NONE"  
            },  
            {  
                "orderListId": 19431,  
                "contingencyType": "OCO",  
                "listStatusType": "ALL_DONE",  
                "listOrderStatus": "ALL_DONE",  
                "listClientOrderId": "iuVNVJYYrByz6C4yGOPPK0",  
                "transactionTime": 1660803702431,  
                "symbol": "BTCUSDT",  
                "orders": [  
                    {  
                        "symbol": "BTCUSDT",  
                        "orderId": 12569099453,  
                        "clientOrderId": "bX5wROblo6YeDwa9iTLeyY"  
                    },  
                    {  
                        "symbol": "BTCUSDT",  
                        "orderId": 12569099454,  
                        "clientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW"  
                    }  
                ],  
                "orderReports": [  
                    {  
                        "symbol": "BTCUSDT",  
                        "origClientOrderId": "bX5wROblo6YeDwa9iTLeyY",  
                        "orderId": 12569099453,  
                        "orderListId": 19431,  
                        "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",  
                        "transactTime": 1684804350068,  
                        "price": "23450.50000000",  
                        "origQty": "0.00850000",  
                        "executedQty": "0.00000000",  
                        "origQuoteOrderQty": "0.000000",  
                        "cummulativeQuoteQty": "0.00000000",  
                        "status": "CANCELED",  
                        "timeInForce": "GTC",  
                        "type": "STOP_LOSS_LIMIT",  
                        "side": "BUY",  
                        "stopPrice": "23430.00000000",  
                        "selfTradePreventionMode": "NONE"  
                    },  
                    {  
                        "symbol": "BTCUSDT",  
                        "origClientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW",  
                        "orderId": 12569099454,  
                        "orderListId": 19431,  
                        "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",  
                        "transactTime": 1684804350068,  
                        "price": "23400.00000000",  
                        "origQty": "0.00850000",  
                        "executedQty": "0.00000000",  
                        "origQuoteOrderQty": "0.000000",  
                        "cummulativeQuoteQty": "0.00000000",  
                        "status": "CANCELED",  
                        "timeInForce": "GTC",  
                        "type": "LIMIT_MAKER",  
                        "side": "BUY",  
                        "selfTradePreventionMode": "NONE"  
                    }  
                ]  
            }  
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses) 部分。

### 订单列表（Order lists）[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#订单列表order-lists "订单列表（Order lists）的直接链接")

#### OCO下单 - 已弃用 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#oco下单---已弃用-trade "OCO下单 - 已弃用 \(TRADE\)的直接链接")
    
    
    {  
        "id": "56374a46-3061-486b-a311-99ee972eb648",  
        "method": "orderList.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "SELL",  
            "price": "23420.00000000",  
            "quantity": "0.00650000",  
            "stopPrice": "23410.00000000",  
            "stopLimitPrice": "23405.00000000",  
            "stopLimitTimeInForce": "GTC",  
            "newOrderRespType": "RESULT",  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "6689c2a36a639ff3915c2904871709990ab65f3c7a9ff13857558fd350315c35",  
            "timestamp": 1660801713767  
        }  
    }  
    

发送新的OCO(one-cancels-the-other) 订单: `LIMIT_MAKER` 订单 + `STOP_LOSS`/`STOP_LOSS_LIMIT` 订单(称呼为 _legs_), 其中一个订单的激活会立即取消另一个订单。

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

**权重:** 1

**未成交的订单计数:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`side`| ENUM| YES| `BUY` 或者 `SELL`  
`price`| DECIMAL| YES| Limit 订单的价格  
`quantity`| DECIMAL| YES|   
`listClientOrderId`| STRING| NO| 订单列表的客户自定义的唯一订单ID。如果未发送，则自动生成  
`limitClientOrderId`| STRING| NO| Limit 挂单的客户自定义的唯一订单ID。如果未发送，则自动生成  
`limitIcebergQty`| DECIMAL| NO|   
`limitStrategyId`| LONG| NO| 标识订单策略中的 limit 订单的任意ID。  
`limitStrategyType`| INT| NO| 标识 limit 订单策略的任意数值小于`1000000`的值是保留的，不能使用。  
`stopPrice`| DECIMAL| YES *| 必须指定 `stopPrice` 或 `trailingDelta`，或两者都指定  
`trailingDelta`| INT| YES *| 请看 [追踪止盈止损(Trailing Stop)订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)  
`stopClientOrderId`| STRING| NO| Stop 订单的客户自定义的唯一订单ID。如果未发送，则自动生成  
`stopLimitPrice`| DECIMAL| NO *|   
`stopLimitTimeInForce`| ENUM| NO *| 有关可用选项，请看 [`order.place`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#timeInForce)  
`stopIcebergQty`| DECIMAL| NO *|   
`stopStrategyId`| LONG| NO| 标识订单策略中的 stop 订单的任意ID。  
`stopStrategyType`| INT| NO| 标识 stop 订单策略的任意数值。小于`1000000`的值是保留的，不能使用。  
`newOrderRespType`| ENUM| NO| 可选的响应格式: `ACK`，`RESULT`，`FULL` (默认)  
`selfTradePreventionMode`| ENUM| NO| 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`signature`| STRING| YES|   
`timestamp`| LONG| YES|   
  
备注：

  * `listClientOrderId` 参数指定 OCO 对的 `listClientOrderId`。

只有当前一个 OCO 已满或完全过期时，才会接受具有相同 `listClientOrderId` 的新 OCO。

`listClientOrderId` 与单个订单的 `clientOrderId` 不同。

  * legs 的价格限制：

`side`| 价格关系  
---|---  
`BUY`| `price` < 市场价格 < `stopPrice`  
`SELL`| `price` > 市场价格 > `stopPrice`  
  * 两个 legs 的 `quantity` 需要相同。

不过单个 leg 可以设置不同的冰山数量。

如果使用 `stopIcebergQty`，`stopLimitTimeInForce` 必须是 `GTC`。

  * `trailingDelta` 仅适用于 OCO 的 `STOP_LOSS`/`STOP_LOSS_LIMIT` leg。




**数据源:** 撮合引擎

**响应:**

使用 `newOrderRespType` 参数选择 `orderReports` 的响应格式。 以下示例适用于 `RESULT` 响应类型。 有关更多示例，请参阅 [`order.place`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-place)。
    
    
    {  
        "id": "57833dc0-e3f2-43fb-ba20-46480973b0aa",  
        "status": 200,  
        "result": {  
            "orderListId": 1274512,  
            "contingencyType": "OCO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "08985fedd9ea2cf6b28996",  
            "transactionTime": 1660801713793,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138901,  
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138902,  
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138901,  
                    "orderListId": 1274512,  
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU",  
                    "transactTime": 1660801713793,  
                    "price": "23410.00000000",  
                    "origQty": "0.00650000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "SELL",  
                    "stopPrice": "23405.00000000",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138902,  
                    "orderListId": 1274512,  
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us",  
                    "transactTime": 1660801713793,  
                    "price": "23420.00000000",  
                    "origQty": "0.00650000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "SELL",  
                    "workingTime": 1660801713793,  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 2  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 2  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

#### 发送新 OCO 订单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#发送新-oco-订单-trade "发送新 OCO 订单 \(TRADE\)的直接链接")
    
    
    {  
        "id": "56374a46-3261-486b-a211-99ed972eb648",  
        "method": "orderList.place.oco",  
        "params": {  
            "symbol": "LTCBNB",  
            "side": "BUY",  
            "quantity": 1,  
            "timestamp": 1711062760647,  
            "aboveType": "STOP_LOSS_LIMIT",  
            "abovePrice": "1.5",  
            "aboveStopPrice": "1.50000001",  
            "aboveTimeInForce": "GTC",  
            "belowType": "LIMIT_MAKER",  
            "belowPrice": "1.49999999",  
            "apiKey": "duwNf97YPLqhFIk7kZF0dDdGYVAXStA7BeEz0fIT9RAhUbixJtyS6kJ3hhzJsRXC",  
            "signature": "64614cfd8dd38260d4fd86d3c455dbf4b9d1c8a8170ea54f700592a986c30ddb"  
        }  
    }  
    

发送新 one-cancels-the-other (OCO) 订单，激活其中一个订单会立即取消另一个订单。

  * OCO 包含了两个订单，分别被称为 **上方订单** 和 **下方订单** 。
  * 其中一个订单必须是 `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` 订单，另一个订单必须是 `STOP_LOSS` 或 `STOP_LOSS_LIMIT` 订单。
  * 针对价格限制： 
    * 如果 OCO 订单方向是 `SELL`： 
      * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
      * `TAKE_PROFIT` `stopPrice` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    * 如果 OCO 订单方向是 `BUY`： 
      * `LIMIT_MAKER` `price` < 最后交易价格 < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
      * `TAKE_PROFIT` `stopPrice` > 最后交易价格 > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
  * OCO 将**2 个订单** 添加到 `EXCHANGE_MAX_ORDERS`过滤器和 `MAX_NUM_ORDERS` 过滤器中。



**权重:** 1

**未成交的订单计数:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`listClientOrderId`| STRING| NO| 整个订单列表的唯一ID。 如果未发送则自动生成。   
仅当前一个订单已填满或完全过期时，才会接受具有相同的`listClientOrderId`。  
`listClientOrderId` 与 `aboveClientOrderId` 和 `belowCLientOrderId` 不同。  
`side`| ENUM| YES| 订单方向：`BUY` or `SELL`  
`quantity`| DECIMAL| YES| 两个订单的数量。  
`aboveType`| ENUM| YES| 支持值：`STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`。  
`aboveClientOrderId`| STRING| NO| 上方订单的唯一ID。 如果未发送则自动生成。  
`aboveIcebergQty`| LONG| NO| 请注意，只有当 `aboveTimeInForce` 为 `GTC` 时才能使用。  
`abovePrice`| DECIMAL| NO| 当 `aboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。  
`aboveStopPrice`| DECIMAL| NO| 如果 `aboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。  
必须指定 `aboveStopPrice` 或 `aboveTrailingDelta` 或两者。  
`aboveTrailingDelta`| LONG| NO| 请看 [追踪止盈止损(Trailing Stop)订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq).  
`aboveTimeInForce`| ENUM| NO| 如果 `aboveType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必填项。  
`aboveStrategyId`| LONG| NO| 订单策略中上方订单的 ID。  
`aboveStrategyType`| INT| NO| 上方订单策略的任意数值。  
小于 `1000000` 的值被保留，无法使用。  
`abovePegPriceType`| ENUM| NO| 参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`abovePegOffsetType`| ENUM| NO|   
`abovePegOffsetValue`| INT| NO|   
`belowType`| ENUM| YES| 支持值：`STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`。  
`belowClientOrderId`| STRING| NO|   
`belowIcebergQty`| LONG| NO| 请注意，只有当 `belowTimeInForce` 为 `GTC` 时才能使用。  
`belowPrice`| DECIMAL| NO| 当 `belowType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。  
`belowStopPrice`| DECIMAL| NO| 如果 `belowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 才能使用。  
必须指定 `belowStopPrice` 或 `belowTrailingDelta` 或两者。  
`belowTrailingDelta`| LONG| NO| 请看 [追踪止盈止损(Trailing Stop)订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)。  
`belowTimeInForce`| ENUM| NO| 如果`belowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT`，则为必须配合提交的值。  
`belowStrategyId`| LONG| NO| 订单策略中下方订单的 ID。  
`belowStrategyType`| INT| NO| 下方订单策略的任意数值。  
小于 `1000000` 的值被保留，无法使用。  
`belowPegPriceType`| ENUM| NO| 参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`belowPegOffsetType`| ENUM| NO|   
`belowPegOffsetValue`| INT| NO|   
`newOrderRespType`| ENUM| NO| 响应格式可选值: `ACK`, `RESULT`, `FULL`。  
`selfTradePreventionMode`| ENUM| NO| 允许的 ENUM 取决于交易对上的配置。 可能支持的值为：[STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
`apiKey`| STRING| YES|   
`recvWindow`| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`signature`| STRING| YES|   
`timestamp`| LONG| YES|   
  
**数据源:** 撮合引擎

**响应:**

使用 `newOrderRespType` 参数来选择 `orderReports` 的响应格式。以下示例适用于 `RESULT` 响应类型。 请参阅 [`order.place`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-place)了解更多 `orderReports` 的响应类型。
    
    
    {  
        "id": "56374a46-3261-486b-a211-99ed972eb648",  
        "status": 200,  
        "result": {  
            "orderListId": 2,  
            "contingencyType": "OCO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "cKPMnDCbcLQILtDYM4f4fX",  
            "transactionTime": 1711062760648,  
            "symbol": "LTCBNB",  
            "orders": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 2,  
                    "clientOrderId": "0m6I4wfxvTUrOBSMUl0OPU"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 3,  
                    "clientOrderId": "Z2IMlR79XNY5LU0tOxrWyW"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 2,  
                    "orderListId": 2,  
                    "clientOrderId": "0m6I4wfxvTUrOBSMUl0OPU",  
                    "transactTime": 1711062760648,  
                    "price": "1.50000000",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "BUY",  
                    "stopPrice": "1.50000001",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 3,  
                    "orderListId": 2,  
                    "clientOrderId": "Z2IMlR79XNY5LU0tOxrWyW",  
                    "transactTime": 1711062760648,  
                    "price": "1.49999999",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "BUY",  
                    "workingTime": 1711062760648,  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 2  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 2  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

#### 发送新订单列表 - OTO (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#发送新订单列表---oto-trade "发送新订单列表 - OTO \(TRADE\)的直接链接")
    
    
    {  
        "id": "1712544395950",  
        "method": "orderList.place.oto",  
        "params": {  
            "signature": "3e1e5ac8690b0caf9a2afd5c5de881ceba69939cc9d817daead5386bf65d0cbb",  
            "apiKey": "Rf07JlnL9PHVxjs27O5CvKNyOsV4qJ5gXdrRfpvlOdvMZbGZbPO5Ce2nIwfRP0iA",  
            "pendingQuantity": 1,  
            "pendingSide": "BUY",  
            "pendingType": "MARKET",  
            "symbol": "LTCBNB",  
            "recvWindow": "5000",  
            "timestamp": "1712544395951",  
            "workingPrice": 1,  
            "workingQuantity": 1,  
            "workingSide": "SELL",  
            "workingTimeInForce": "GTC",  
            "workingType": "LIMIT"  
        }  
    }  
    

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
`symbol`| STRING| YES|   
`listClientOrderId`| STRING| NO| 整个订单列表的唯一ID。 如果未发送则自动生成。   
仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。   
`listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。  
`newOrderRespType`| ENUM| NO| 用于设置JSON响应的格式。 支持的数值： [订单返回类型](/docs/zh-CN/binance-spot-api-docs/enums#orderresponsetype)  
`selfTradePreventionMode`| ENUM| NO| 允许的数值取决于交易对上的配置。参考 [STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
`workingType`| ENUM| YES| 支持的数值： `LIMIT`， `LIMIT_MAKER`  
`workingSide`| ENUM| YES| 支持的数值： [订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
`workingClientOrderId`| STRING| NO| 用于标识生效订单的唯一ID。   
如果未发送则自动生成。  
`workingPrice`| DECIMAL| YES|   
`workingQuantity`| DECIMAL| YES| 用于设置生效订单的数量。  
`workingIcebergQty`| DECIMAL| NO| 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。  
`workingTimeInForce`| ENUM| NO| 支持的数值： [生效时间](/docs/zh-CN/binance-spot-api-docs/enums#timeinforce)  
`workingStrategyId`| LONG| NO| 订单策略中用于标识生效订单的 ID。  
`workingStrategyType`| INT| NO| 用于标识生效订单策略的任意数值。  
小于 `1000000` 的值被保留，无法使用。  
`workingPegPriceType`| ENUM| NO| 参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`workingPegOffsetType`| ENUM| NO|   
`workingPegOffsetValue`| INT| NO|   
`pendingType`| ENUM| YES| 支持的数值： [订单类型](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-type)  
请注意，系统不支持使用 `quoteOrderQty` 的 `MARKET` 订单。  
`pendingSide`| ENUM| YES| 支持的数值： [订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
`pendingClientOrderId`| STRING| NO| 用于标识待处理订单的唯一ID。   
如果未发送则自动生成。  
`pendingPrice`| DECIMAL| NO|   
`pendingStopPrice`| DECIMAL| NO|   
`pendingTrailingDelta`| DECIMAL| NO|   
`pendingQuantity`| DECIMAL| YES| 用于设置待处理订单的数量。  
`pendingIcebergQty`| DECIMAL| NO| 只有当 `pendingTimeInForce` 为 `GTC` 时才能使用。  
`pendingTimeInForce`| ENUM| NO| 支持的数值： [生效时间](/docs/zh-CN/binance-spot-api-docs/enums#timeinforce)  
`pendingStrategyId`| LONG| NO| 订单策略中用于标识待处理订单的 ID。  
`pendingStrategyType`| INT| NO| 用于标识待处理订单策略的任意数值。   
小于 `1000000` 的值被保留，无法使用。  
`pendingPegOffsetType`| ENUM| NO| 参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingPegPriceType`| ENUM| NO|   
`pendingPegOffsetValue`| INT| NO|   
`recvWindow`| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`timestamp`| LONG| YES|   
`signature`| STRING| YES|   
  
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
        "id": "1712544395950",  
        "status": 200,  
        "result": {  
            "orderListId": 626,  
            "contingencyType": "OTO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "KA4EBjGnzvSwSCQsDdTrlf",  
            "transactionTime": 1712544395981,  
            "symbol": "1712544378871",  
            "orders": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 13,  
                    "clientOrderId": "YiAUtM9yJjl1a2jXHSp9Ny"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 14,  
                    "clientOrderId": "9MxJSE1TYkmyx5lbGLve7R"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 13,  
                    "orderListId": 626,  
                    "clientOrderId": "YiAUtM9yJjl1a2jXHSp9Ny",  
                    "transactTime": 1712544395981,  
                    "price": "1.000000",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "SELL",  
                    "workingTime": 1712544395981,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 14,  
                    "orderListId": 626,  
                    "clientOrderId": "9MxJSE1TYkmyx5lbGLve7R",  
                    "transactTime": 1712544395981,  
                    "price": "0.000000",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "PENDING_NEW",  
                    "timeInForce": "GTC",  
                    "type": "MARKET",  
                    "side": "BUY",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 10000000,  
                "count": 10  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 1000,  
                "count": 38  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses) 部分。

#### 发送新订单列表 - OTOCO (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#发送新订单列表---otoco-trade "发送新订单列表 - OTOCO \(TRADE\)的直接链接")
    
    
    {  
        "id": "1712544408508",  
        "method": "orderList.place.otoco",  
        "params": {  
            "signature": "c094473304374e1b9c5f7e2558358066cfa99df69f50f63d09cfee755136cb07",  
            "apiKey": "Rf07JlnL9PHVxjs27O5CvKNyOsV4qJ5gXdrRfpvlOdvMZbGZbPO5Ce2nIwfRP0iA",  
            "pendingQuantity": 5,  
            "pendingSide": "SELL",  
            "pendingBelowPrice": 5,  
            "pendingBelowType": "LIMIT_MAKER",  
            "pendingAboveStopPrice": 0.5,  
            "pendingAboveType": "STOP_LOSS",  
            "symbol": "LTCBNB",  
            "recvWindow": "5000",  
            "timestamp": "1712544408509",  
            "workingPrice": 1.5,  
            "workingQuantity": 1,  
            "workingSide": "BUY",  
            "workingTimeInForce": "GTC",  
            "workingType": "LIMIT"  
        }  
    }  
    

发送一个新的 OTOCO 订单。

  * 一个 OTOCO 订单（One-Triggers-One-Cancels-the-Other）是一个包含了三个订单的订单列表。
  * 第一个订单被称为**生效订单** ，必须为 `LIMIT` 或 `LIMIT_MAKER` 类型的订单。最初，订单簿上只有生效订单。 
    * 生效订单的行为与此一致 [OTO](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#orderList-place-oto)
  * 一个OTOCO订单有两个待处理订单（pending above 和 pending below），它们构成了一个 OCO 订单列表。只有当生效订单**完全成交** 时，待处理订单们才会被自动下单。 
    * 待处理上方(pending above)订单和待处理下方(pending below)订单都遵循与 OCO 订单列表相同的规则 [Order List OCO](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#orderlist-place-oco)。
  * `OTOCO` 在 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器的基础上添加**3个订单** 。



**权重:** 1

**未成交的订单计数:** 3

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`listClientOrderId`| STRING| NO| 整个订单列表的唯一ID。 如果未发送则自动生成。   
仅当前一个订单列表已填满或完全过期时，才会接受含有相同 `listClientOrderId` 值的新订单列表。   
`listClientOrderId` 与 `workingClientOrderId`， `pendingAboveClientOrderId` 以及 `pendingBelowClientOrderId` 不同。  
`newOrderRespType`| ENUM| NO| 用于设置JSON响应的格式。 支持的数值： [订单返回类型](/docs/zh-CN/binance-spot-api-docs/enums#orderresponsetype)  
`selfTradePreventionMode`| ENUM| NO| 允许的数值取决于交易对上的配置。支持的数值： [STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
`workingType`| ENUM| YES| 支持的数值： `LIMIT`，`LIMIT_MAKER`  
`workingSide`| ENUM| YES| 支持的数值： [订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
`workingClientOrderId`| STRING| NO| 用于标识生效订单的唯一ID。   
如果未发送则自动生成。  
`workingPrice`| DECIMAL| YES|   
`workingQuantity`| DECIMAL| YES|   
`workingIcebergQty`| DECIMAL| NO| 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时，才能使用此功能。  
`workingTimeInForce`| ENUM| NO| 支持的数值： [生效时间](/docs/zh-CN/binance-spot-api-docs/enums#timeinforce)  
`workingStrategyId`| LONG| NO| 订单策略中用于标识生效订单的 ID。  
`workingStrategyType`| INT| NO| 用于标识生效订单策略的任意数值。  
小于 `1000000` 的值被保留，无法使用。  
`workingPegPriceType`| ENUM| NO| 参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`workingPegOffsetType`| ENUM| NO|   
`workingPegOffsetValue`| INT| NO|   
`pendingSide`| ENUM| YES| 支持的数值： [订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
`pendingQuantity`| DECIMAL| YES|   
`pendingAboveType`| ENUM| YES| 支持的数值： `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
`pendingAboveClientOrderId`| STRING| NO| 用于标识待处理上方订单的唯一ID。   
如果未发送则自动生成。  
`pendingAbovePrice`| DECIMAL| NO| 当 `pendingAboveType` 是 `STOP_LOSS_LIMIT`, `LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。  
`pendingAboveStopPrice`| DECIMAL| NO| 如果 `pendingAboveType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。  
`pendingAboveTrailingDelta`| DECIMAL| NO| 参见 [追踪止盈止损(Trailing Stop)订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)  
`pendingAboveIcebergQty`| DECIMAL| NO| 只有当 `pendingAboveTimeInForce` 为 `GTC` 时才能使用。  
`pendingAboveTimeInForce`| ENUM| NO|   
`pendingAboveStrategyId`| LONG| NO| 订单策略中用于标识待处理上方订单的 ID。  
`pendingAboveStrategyType`| INT| NO| 用于标识待处理上方订单策略的任意数值。   
小于 `1000000` 的值被保留，无法使用。  
`pendingAbovePegPriceType`| ENUM| NO| 参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingAbovePegOffsetType`| ENUM| NO|   
`pendingAbovePegOffsetValue`| INT| NO|   
`pendingBelowType`| ENUM| NO| 支持的数值： `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`  
`pendingBelowClientOrderId`| STRING| NO| 用于标识待处理下方订单的唯一ID。   
如果未发送则自动生成。  
`pendingBelowPrice`| DECIMAL| NO| 当 `pendingBelowType` 是 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用以指定限价。  
`pendingBelowStopPrice`| DECIMAL| NO| 如果 `pendingBelowType` 是 `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` 才能使用。  
必须指定 `pendingBelowStopPrice` 或 `pendingBelowTrailingDelta` 或两者。  
`pendingBelowTrailingDelta`| DECIMAL| NO|   
`pendingBelowIcebergQty`| DECIMAL| NO| 只有当 `pendingBelowTimeInForce` 为 `GTC` 时才能使用。  
`pendingBelowTimeInForce`| ENUM| NO| 支持的数值： [生效时间](/docs/zh-CN/binance-spot-api-docs/enums#timeinforce)  
`pendingBelowStrategyId`| LONG| NO| 订单策略中用于标识待处理下方订单的 ID。  
`pendingBelowStrategyType`| INT| NO| 用于标识待处理下方订单策略的任意数值。   
小于 `1000000` 的值被保留，无法使用。  
`pendingBelowPegPriceType`| ENUM| NO| 参阅 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingBelowPegOffsetType`| ENUM| NO|   
`pendingBelowPegOffsetValue`| INT| NO|   
`recvWindow`| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`timestamp`| LONG| YES|   
`signature`| STRING| YES|   
  
**根据`pendingAboveType`， `pendingBelowType` 或者`workingType`的不同值，对于某些参数的强制要求**

根据 `pendingAboveType`， `pendingBelowType` 或者`workingType`的不同值，对于某些可选参数有强制要求，具体如下：

类型| 强制要求的参数| 其他信息  
---|---|---  
`workingType` = `LIMIT`| `workingTimeInForce`|   
`pendingAboveType` = `STOP_LOSS/TAKE_PROFIT`| `pendingAboveStopPrice` 与/或 `pendingAboveTrailingDelta`|   
`pendingAboveType` = `STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`| `pendingAbovePrice`， `pendingAboveStopPrice` 与/或 `pendingAboveTrailingDelta`， `pendingAboveTimeInForce`|   
`pendingAboveType` = `LIMIT_MAKER`| `pendingAbovePrice`|   
`pendingBelowType` = `STOP_LOSS/TAKE_PROFIT`| `pendingBelowStopPrice` 与/或 `pendingBelowTrailingDelta`|   
`pendingBelowType` = `STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`| `pendingBelowPrice`， `pendingBelowStopPrice` 与/或 `pendingBelowTrailingDelta`， `pendingBelowTimeInForce`|   
`pendingBelowType` = `LIMIT_MAKER`| `pendingBelowPrice`|   
  
**数据源:** 撮合引擎

**响应:**
    
    
    {  
        "id": "1712544408508",  
        "status": 200,  
        "result": {  
            "orderListId": 629,  
            "contingencyType": "OTO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "GaeJHjZPasPItFj4x7Mqm6",  
            "transactionTime": 1712544408537,  
            "symbol": "1712544378871",  
            "orders": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 23,  
                    "clientOrderId": "OVQOpKwfmPCfaBTD0n7e7H"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 24,  
                    "clientOrderId": "YcCPKCDMQIjNvLtNswt82X"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 25,  
                    "clientOrderId": "ilpIoShcFZ1ZGgSASKxMPt"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 23,  
                    "orderListId": 629,  
                    "clientOrderId": "OVQOpKwfmPCfaBTD0n7e7H",  
                    "transactTime": 1712544408537,  
                    "price": "1.500000",  
                    "origQty": "1.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "BUY",  
                    "workingTime": 1712544408537,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 24,  
                    "orderListId": 629,  
                    "clientOrderId": "YcCPKCDMQIjNvLtNswt82X",  
                    "transactTime": 1712544408537,  
                    "price": "0.000000",  
                    "origQty": "5.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "PENDING_NEW",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS",  
                    "side": "SELL",  
                    "stopPrice": "0.500000",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "LTCBNB",  
                    "orderId": 25,  
                    "orderListId": 629,  
                    "clientOrderId": "ilpIoShcFZ1ZGgSASKxMPt",  
                    "transactTime": 1712544408537,  
                    "price": "5.000000",  
                    "origQty": "5.000000",  
                    "executedQty": "0.000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.000000",  
                    "status": "PENDING_NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT_MAKER",  
                    "side": "SELL",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 10000000,  
                "count": 18  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 1000,  
                "count": 65  
            }  
        ]  
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses) 部分。

#### 新订单列表 - OPO（TRADE）[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#新订单列表---opotrade "新订单列表 - OPO（TRADE）的直接链接")
    
    
    {  
        "id": "1762941318128",  
        "method": "orderList.place.opo",  
        "params": {  
            "workingPrice": "101496",  
            "workingQuantity": "0.0007",  
            "workingType": "LIMIT",  
            "workingTimeInForce": "GTC",  
            "pendingType": "MARKET",  
            "pendingSide": "SELL",  
            "recvWindow": 5000,  
            "workingSide": "BUY",  
            "symbol": "BTCUSDT",  
            "timestamp": 1762941318129,  
            "apiKey": "aHb4Ur1cK1biW3sgibqUFs39SE58f9d5Xwf4uEW0tFh7ibun5g035QKSktxoOBfE",  
            "signature": "b50ce8977333a78a3bbad21df178d7e104a8c985d19007b55df688cdf868639a"  
        }  
    }  
    

发送一个 [OPO](/docs/zh-CN/binance-spot-api-docs/faqs/opo) 订单。

  * OPO 会向 `EXCHANGE_MAX_NUM_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中添加 2 个订单。



**权重:** 1

**未成交订单数量:** 2

**参数:**

名称| 类型| 必填| 描述  
---|---|---|---  
`symbol`| STRING| YES| 交易对符号  
`listClientOrderId`| STRING| NO| 订单列表中的任意唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期时，才接受新的同一 `listClientOrderId` 的订单列表。`listClientOrderId` 与 `workingClientOrderId` 和 `pendingClientOrderId` 不同。  
`newOrderRespType`| ENUM| NO| JSON 响应格式。支持的数值：[订单返回类型](/docs/zh-CN/binance-spot-api-docs/enums#orderresponsetype)  
`selfTradePreventionMode`| ENUM| NO| 允许的值取决于交易对的配置。支持的值见：[STP模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
`workingType`| ENUM| YES| 支持的数值：`LIMIT`，`LIMIT_MAKER`  
`workingSide`| ENUM| YES| 支持的数值：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
`workingClientOrderId`| STRING| NO| 生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。  
`workingPrice`| DECIMAL| YES| 生效订单价格  
`workingQuantity`| DECIMAL| YES| 设置生效订单的数量  
`workingIcebergQty`| DECIMAL| NO| 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用  
`workingTimeInForce`| ENUM| NO| 支持的数值：[生效时间](/docs/zh-CN/binance-spot-api-docs/enums#timeinforce)  
`workingStrategyId`| LONG| NO| 用于标识订单策略中生效订单的任意数字值  
`workingStrategyType`| INT| NO| 用于标识生效订单策略的任意数字值。小于 1000000 为保留值，不能使用。  
`workingPegPriceType`| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`workingPegOffsetType`| ENUM| NO|   
`workingPegOffsetValue`| INT| NO|   
`pendingType`| ENUM| YES| 支持的数值：[订单类型](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-type)。注意，不支持使用 `quoteOrderQty` 的 `MARKET` 订单。  
`pendingSide`| ENUM| YES| 支持的数值：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
`pendingClientOrderId`| STRING| NO| 待处理订单中挂单的任意唯一 ID。如果未发送，则自动生成。  
`pendingPrice`| DECIMAL| NO| 待处理订单价格  
`pendingStopPrice`| DECIMAL| NO| 待处理订单止损价格  
`pendingTrailingDelta`| DECIMAL| NO| 待处理订单跟踪止损差值  
`pendingIcebergQty`| DECIMAL| NO| 仅当 `pendingTimeInForce` 为 `GTC` 或 `pendingType` 为 `LIMIT_MAKER` 时可用  
`pendingTimeInForce`| ENUM| NO| 支持的数值：[生效时间](/docs/zh-CN/binance-spot-api-docs/enums#timeinforce)  
`pendingStrategyId`| LONG| NO| 用于标识订单策略中待处理订单的任意数字值  
`pendingStrategyType`| INT| NO| 用于标识待处理订单策略的任意数字值。小于 1000000 为保留值，不能使用。  
`pendingPegPriceType`| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingPegOffsetType`| ENUM| NO|   
`pendingPegOffsetValue`| INT| NO|   
`recvWindow`| DECIMAL| NO| 该值不能大于 `60000`。支持最多三位小数精度（例如 6000.346），以便指定微秒。  
`timestamp`| LONG| YES| 时间戳  
  
**数据来源** ：撮合引擎

**响应示例:**
    
    
    {  
        "id": "1762941318128",  
        "status": 200,  
        "result": {  
            "orderListId": 2,  
            "contingencyType": "OTO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "OiOgqvRagBefpzdM5gjYX3",  
            "transactionTime": 1762941318142,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 2,  
                    "clientOrderId": "pUzhKBbc0ZVdMScIRAqitH"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 3,  
                    "clientOrderId": "x7ISSjywZxFXOdzwsThNnd"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 2,  
                    "orderListId": 2,  
                    "clientOrderId": "pUzhKBbc0ZVdMScIRAqitH",  
                    "transactTime": 1762941318142,  
                    "price": "101496.00000000",  
                    "origQty": "0.00070000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.00000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "BUY",  
                    "workingTime": 1762941318142,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 3,  
                    "orderListId": 2,  
                    "clientOrderId": "x7ISSjywZxFXOdzwsThNnd",  
                    "transactTime": 1762941318142,  
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
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses) 部分。

#### 新订单列表 - OPOCO（TRADE）[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#新订单列表---opocotrade "新订单列表 - OPOCO（TRADE）的直接链接")
    
    
    {  
        "id": "1763000139090",  
        "method": "orderList.place.opoco",  
        "params": {  
            "workingPrice": "102496",  
            "workingQuantity": "0.0017",  
            "workingType": "LIMIT",  
            "workingTimeInForce": "GTC",  
            "pendingAboveType": "LIMIT_MAKER",  
            "pendingAbovePrice": "104261",  
            "pendingBelowStopPrice": "10100",  
            "pendingBelowPrice": "101613",  
            "pendingBelowType": "STOP_LOSS_LIMIT",  
            "pendingBelowTimeInForce": "IOC",  
            "pendingSide": "SELL",  
            "recvWindow": 5000,  
            "workingSide": "BUY",  
            "symbol": "BTCUSDT",  
            "timestamp": 1763000139091,  
            "apiKey": "2wiKgTLyllTCu0QWXaEtKWX9tUQ5iQMiDQqTQPdUe2bZ1IVT9aXoS6o19wkYIKl2",  
            "signature": "adfa185c50f793392a54ad5a6e2c39fd34ef6d35944adf2ddd6f30e1866e58d3"  
        }  
    }  
    

发送一个 [OPOCO](/docs/zh-CN/binance-spot-api-docs/faqs/opo) 订单。

**权重** : 1

**未成交订单数量:** 3

**参数:**

名称| 类型| 必填| 描述  
---|---|---|---  
`symbol`| STRING| YES| 交易对符号  
`listClientOrderId`| STRING| NO| 订单列表中的任意唯一 ID。如果未发送，则自动生成。只有当之前的同一 `listClientOrderId` 的订单列表已成交或完全过期时，才接受新的同一 `listClientOrderId` 的订单列表。`listClientOrderId` 与 `workingClientOrderId`、`pendingAboveClientOrderId` 和 `pendingBelowClientOrderId` 不同。  
`newOrderRespType`| ENUM| NO| JSON 响应格式。支持的数值：[订单返回类型](/docs/zh-CN/binance-spot-api-docs/enums#orderresponsetype)  
`selfTradePreventionMode`| ENUM| NO| 允许的值取决于交易对的配置。支持的数值：[STP模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
`workingType`| ENUM| YES| 支持的值：`LIMIT`，`LIMIT_MAKER`  
`workingSide`| ENUM| YES| 支持的值见：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
`workingClientOrderId`| STRING| NO| 生效订单中挂单的任意唯一 ID。如果未发送，则自动生成。  
`workingPrice`| DECIMAL| YES| 生效订单价格  
`workingQuantity`| DECIMAL| YES| 生效订单数量  
`workingIcebergQty`| DECIMAL| NO| 仅当 `workingTimeInForce` 为 `GTC` 或 `workingType` 为 `LIMIT_MAKER` 时可用  
`workingTimeInForce`| ENUM| NO| 支持的数值：[生效时间](/docs/zh-CN/binance-spot-api-docs/enums#timeinforce)  
`workingStrategyId`| LONG| NO| 用于标识订单策略中生效订单的任意数字值  
`workingStrategyType`| INT| NO| 用于标识生效订单策略的任意数字值。小于 1000000 为保留值，不能使用。  
`workingPegPriceType`| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`workingPegOffsetType`| ENUM| NO|   
`workingPegOffsetValue`| INT| NO|   
`pendingSide`| ENUM| YES| 支持的值见：[订单方向](/docs/zh-CN/binance-spot-api-docs/enums#side)  
`pendingAboveType`| ENUM| YES| 支持的值：`STOP_LOSS_LIMIT`，`STOP_LOSS`，`LIMIT_MAKER`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`  
`pendingAboveClientOrderId`| STRING| NO| 待处理上方订单中开放订单的任意唯一 ID。如果未发送，则自动生成。  
`pendingAbovePrice`| DECIMAL| NO| 当 `pendingAboveType` 为 `STOP_LOSS_LIMIT`、`LIMIT_MAKER` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。  
`pendingAboveStopPrice`| DECIMAL| NO| 当 `pendingAboveType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT`、`TAKE_PROFIT_LIMIT` 时可用。  
`pendingAboveTrailingDelta`| DECIMAL| NO| 详见 [追踪止盈止损订单常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/trailing-stop-faq)  
`pendingAboveIcebergQty`| DECIMAL| NO| 仅当 `pendingAboveTimeInForce` 为 `GTC` 或 `pendingAboveType` 为 `LIMIT_MAKER` 时可用。  
`pendingAboveTimeInForce`| ENUM| NO|   
`pendingAboveStrategyId`| LONG| NO| 用于标识订单策略中待处理上方订单的任意数值。  
`pendingAboveStrategyType`| INT| NO| 用于标识待处理上方订单策略的任意数字值。小于 1000000 的值为保留，不能使用。  
`pendingAbovePegPriceType`| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingAbovePegOffsetType`| ENUM| NO|   
`pendingAbovePegOffsetValue`| INT| NO|   
`pendingBelowType`| ENUM| NO| 支持的值：`STOP_LOSS`，`STOP_LOSS_LIMIT`，`TAKE_PROFIT`，`TAKE_PROFIT_LIMIT`  
`pendingBelowClientOrderId`| STRING| NO| 待处理下方订单中开放订单的任意唯一 ID。如果未发送，则自动生成。  
`pendingBelowPrice`| DECIMAL| NO| 当 `pendingBelowType` 为 `STOP_LOSS_LIMIT` 或 `TAKE_PROFIT_LIMIT` 时，可用于指定限价。  
`pendingBelowStopPrice`| DECIMAL| NO| 当 `pendingBelowType` 为 `STOP_LOSS`、`STOP_LOSS_LIMIT`、`TAKE_PROFIT` 或 `TAKE_PROFIT_LIMIT` 时可用。`pendingBelowStopPrice`、`pendingBelowTrailingDelta` 或两者之一必须被指定。  
`pendingBelowTrailingDelta`| DECIMAL| NO|   
`pendingBelowIcebergQty`| DECIMAL| NO| 仅当 `pendingBelowTimeInForce` 为 `GTC` 或 `pendingBelowType` 为 `LIMIT_MAKER` 时可用。  
`pendingBelowTimeInForce`| ENUM| NO| 支持的值见：[生效时间](/docs/zh-CN/binance-spot-api-docs/enums#timeinforce)  
`pendingBelowStrategyId`| LONG| NO| 用于标识订单策略中待处理下方订单的任意数值。  
`pendingBelowStrategyType`| INT| NO| 用于标识待处理下方订单策略的任意数值。小于 1000000 为保留值，不能使用。  
`pendingBelowPegPriceType`| ENUM| NO| 详见 [挂钩订单](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#pegged-orders-info)  
`pendingBelowPegOffsetType`| ENUM| NO|   
`pendingBelowPegOffsetValue`| INT| NO|   
`recvWindow`| DECIMAL| NO| 该值不能大于 `60000`。支持最多三位小数精度（例如 6000.346），以便指定微秒。  
`timestamp`| LONG| YES| 时间戳  
  
**数据来源** ：撮合引擎

**响应示例:**
    
    
    {  
        "id": "1763000139090",  
        "status": 200,  
        "result": {  
            "orderListId": 1,  
            "contingencyType": "OTO",  
            "listStatusType": "EXEC_STARTED",  
            "listOrderStatus": "EXECUTING",  
            "listClientOrderId": "TVbG6ymkYMXTj7tczbOsBf",  
            "transactionTime": 1763000139104,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 6,  
                    "clientOrderId": "3czuJSeyjPwV9Xo28j1Dv3"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 7,  
                    "clientOrderId": "kyIKnMLKQclE5FmyYgaMSo"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 8,  
                    "clientOrderId": "i76cGJWN9J1FpADS56TtQZ"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 6,  
                    "orderListId": 1,  
                    "clientOrderId": "3czuJSeyjPwV9Xo28j1Dv3",  
                    "transactTime": 1763000139104,  
                    "price": "102496.00000000",  
                    "origQty": "0.00170000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.00000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "NEW",  
                    "timeInForce": "GTC",  
                    "type": "LIMIT",  
                    "side": "BUY",  
                    "workingTime": 1763000139104,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 7,  
                    "orderListId": 1,  
                    "clientOrderId": "kyIKnMLKQclE5FmyYgaMSo",  
                    "transactTime": 1763000139104,  
                    "price": "101613.00000000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.00000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "PENDING_NEW",  
                    "timeInForce": "IOC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "SELL",  
                    "stopPrice": "10100.00000000",  
                    "workingTime": -1,  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 8,  
                    "orderListId": 1,  
                    "clientOrderId": "i76cGJWN9J1FpADS56TtQZ",  
                    "transactTime": 1763000139104,  
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
    }  
    

**注意:** 上面的 payload 没有显示所有可以出现的字段，更多请看 [订单响应中的特定条件时才会出现的字段](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#conditional-fields-in-order-responses) 部分。

#### 撤销订单列表订单(TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#撤销订单列表订单trade "撤销订单列表订单\(TRADE\)的直接链接")
    
    
    {  
        "id": "c5899911-d3f4-47ae-8835-97da553d27d0",  
        "method": "orderList.cancel",  
        "params": {  
            "symbol": "BTCUSDT",  
            "orderListId": 1274512,  
            "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",  
            "signature": "4973f4b2fee30bf6d45e4a973e941cc60fdd53c8dd5a25edeac96f5733c0ccee",  
            "timestamp": 1660801720210  
        }  
    }  
    

取消整个订单列表。

**权重:** 1

**参数:**

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`symbol` | STRING | YES |   
`orderListId` | INT | YES | 通过 `orderListId` 撤销订单列表  
`listClientOrderId` | STRING | 通过 `listClientId` 撤销订单列表  
`newClientOrderId` | STRING | NO | 已取消订单列表的新 ID。如果未发送，则自动生成  
`apiKey` | STRING | YES |   
`recvWindow` | DECIMAL | NO | 值不能大于 `60000`。  
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`signature` | STRING | YES |   
`timestamp` | LONG | YES |   
  
备注：

  * 如果同时指定了 `orderListId` 和 `listClientOrderId` 参数，首先将会用`orderListId` 进行搜索，然后将检索结果中的 `listClientOrderId` 与订单进行比对。如果两个条件都不满足，则请求将被拒绝。

  * 使用 [`order.cancel`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#order-cancel) 撤销订单列表内的某个订单，则整个订单列表将被撤销。




**数据源:** 撮合引擎

**响应:**
    
    
    {  
        "id": "c5899911-d3f4-47ae-8835-97da553d27d0",  
        "status": 200,  
        "result": {  
            "orderListId": 1274512,  
            "contingencyType": "OCO",  
            "listStatusType": "ALL_DONE",  
            "listOrderStatus": "ALL_DONE",  
            "listClientOrderId": "6023531d7edaad348f5aff",  
            "transactionTime": 1660801720215,  
            "symbol": "BTCUSDT",  
            "orders": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138901,  
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138902,  
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"  
                }  
            ],  
            "orderReports": [  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138901,  
                    "orderListId": 1274512,  
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU",  
                    "transactTime": 1660801720215,  
                    "price": "23410.00000000",  
                    "origQty": "0.00650000",  
                    "executedQty": "0.00000000",  
                    "origQuoteOrderQty": "0.000000",  
                    "cummulativeQuoteQty": "0.00000000",  
                    "status": "CANCELED",  
                    "timeInForce": "GTC",  
                    "type": "STOP_LOSS_LIMIT",  
                    "side": "SELL",  
                    "stopPrice": "23405.00000000",  
                    "selfTradePreventionMode": "NONE"  
                },  
                {  
                    "symbol": "BTCUSDT",  
                    "orderId": 12569138902,  
                    "orderListId": 1274512,  
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us",  
                    "transactTime": 1660801720215,  
                    "price": "23420.00000000",  
                    "origQty": "0.00650000",  
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
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

### SOR[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#sor "SOR的直接链接")

#### 下 SOR 订单 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#下-sor-订单-trade "下 SOR 订单 \(TRADE\)的直接链接")
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "method": "sor.order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "BUY",  
            "type": "LIMIT",  
            "quantity": 0.5,  
            "timeInForce": "GTC",  
            "price": 31000,  
            "timestamp": 1687485436575,  
            "apiKey": "u5lgqJb97QWXWfgeV4cROuHbReSJM9rgQL0IvYcYc7BVeA5lpAqqc3a5p2OARIFk",  
            "signature": "fd301899567bc9472ce023392160cdc265ad8fcbbb67e0ea1b2af70a4b0cd9c7"  
        }  
    }  
    

下使用智能订单路由 (SOR) 的新订单。

这个请求会把1个订单添加到 `EXCHANGE_MAX_ORDERS` 过滤器和 `MAX_NUM_ORDERS` 过滤器中。

请参阅 [智能订单路由 (SOR)](/docs/zh-CN/binance-spot-api-docs/faqs/sor_faq) 来了解更多详情。

**权重:** 1

**未成交的订单计数:** 1

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
`symbol`| STRING| YES|   
`side`| ENUM| YES| `BUY` 或 `SELL`  
`type`| ENUM| YES|   
`timeInForce`| ENUM| NO| 只适用于`限价`订单类型  
`price`| DECIMAL| NO| 只适用于`限价`订单类型  
`quantity`| DECIMAL| YES|   
`newClientOrderId`| STRING| NO| 用户自定义的任意唯一值orderid，如空缺系统会自动赋值  
`newOrderRespType`| ENUM| NO| 可选的响应格式: `ACK`，`RESULT`，`FULL` Select response format: `ACK`, `RESULT`, `FULL`.`市场`和`限价`单默认使用`FULL`  
`icebergQty`| DECIMAL| NO|   
`strategyId`| LONG| NO| 用于标识订单策略中订单的任意数字值。  
`strategyType`| INT| NO| 用于标识订单策略的任意数字值。小于 `1000000` 是保留值，应此不能被使用。  
`selfTradePreventionMode`| ENUM| NO| 允许的 ENUM 取决于交易对的配置。支持的值有：[STP 模式](/docs/zh-CN/binance-spot-api-docs/enums#stpmodes)  
`apiKey`| STRING| YES|   
`timestamp`| LONG| YES|   
`recvWindow`| DECIMAL| NO| 最大值为 `60000` 毫秒。   
支持最多三位小数的精度（例如 6000.346），以便可以指定微秒。  
`signature`| STRING| YES|   
  
**注意:** `sor.order.place` 只支持 `限价` 和 `市场` 单， 并不支持 `quoteOrderQty`。

**数据源:** 撮合引擎

**响应:** *
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "status": 200,  
        "result": [  
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
        ],  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

#### 测试 SOR 下单接口 (TRADE)[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#测试-sor-下单接口-trade "测试 SOR 下单接口 \(TRADE\)的直接链接")
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "method": "sor.order.test",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "BUY",  
            "type": "LIMIT",  
            "quantity": 0.1,  
            "timeInForce": "GTC",  
            "price": 0.1,  
            "timestamp": 1687485436575,  
            "apiKey": "u5lgqJb97QWXWfgeV4cROuHbReSJM9rgQL0IvYcYc7BVeA5lpAqqc3a5p2OARIFk",  
            "signature": "fd301899567bc9472ce023392160cdc265ad8fcbbb67e0ea1b2af70a4b0cd9c7"  
        }  
    }  
    

用于测试使用智能订单路由 (SOR) 的订单请求，但不会提交到撮合引擎。

**权重:**

条件| 请求权重  
---|---  
没有 `computeCommissionRates`| 1  
有 `computeCommissionRates`| 20  
  
**参数:**

除了 [`sor.order.place`](/docs/zh-CN/binance-spot-api-docs/websocket-api/trading-requests#sor-order-place) 所有参数, 下面参数也有效:

参数名| 类型| 是否必需| 描述  
---|---|---|---  
`computeCommissionRates`| BOOLEAN| NO| 默认值： `false`  
  
**数据源:** 缓存

**响应:**

没有 `computeCommissionRates`:
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "status": 200,  
        "result": {},  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

有 `computeCommissionRates`:
    
    
    {  
        "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",  
        "status": 200,  
        "result": {  
            "standardCommissionForOrder": { // 订单交易的标准佣金率。  
                "maker": "0.00000112",  
                "taker": "0.00000114"  
            },  
            "taxCommissionForOrder": {      // 订单交易的税率。  
                "maker": "0.00000112",  
                "taker": "0.00000114"  
            },  
            "discount": {                   // 以BNB支付时的标准佣金折扣。  
                "enabledForAccount": true,  
                "enabledForSymbol": true,  
                "discountAsset": "BNB",  
                "discount": "0.25000000"     // 当用BNB支付佣金时，在标准佣金上按此比率打折。  
            }  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 20  
            }  
        ]  
    }