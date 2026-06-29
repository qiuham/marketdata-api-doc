---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading
anchor_id: spread-trading
api_type: API
updated_at: 2026-06-29 19:56:57.156073
---

# Spread Trading

👉 The Spread Orderbook product enables users to **post or consume liquidity** on spreads for **large sizes** that are guaranteed **atomic execution**. Benefits include simplified futures rolls, funding arbitrage, yield enhancement, and speculation on basis and term structures.   
  
## Introduction

### Basic Concepts

  1. **Spread -** Entering a trade where the trader is long one instrument and short an offsetting quantity of a related instrument, forming a trade with two risk offsetting legs.
  2. **Order-book -** A collection of offers to trade an instrument or basket. Each offer contains a defined instrument or group of instruments, relevant quantity, and the price at which the offerer is willing to transact. Takers can then immediately consume these offers up to the full amount of quantity listed at the offered price. The pending order limit of spread trading is 500 across all spreads.

### High Level Workflow

Nitro Spreads is centered around the familiar concept of a Central Limit Order Book (**CLOB**).

  * Spreads consist of instruments sourced from OKX where they are cleared and settled.
  * Anyone can act as a "Taker," who consumes an existing resting order, or a "Maker," whose order is consumed.
  * Trades take place when orders are crossed. Trades are then sent for clearing and settlement on OKX.

At a high level, the Nitro Spreads workflow is as follows:

  1. _Maker_ rests a Limit Order upon a Spread's Order Book.
  2. _Taker_ consumes a resting Order via a Limit Order.
  3. The crossed orders are sent for clearing and settlement.
  4. The _Taker_ and _Maker_ receive confirmation of the success or rejection of the Trade.
  5. All users are notified of successfully settled & cleared Trades, minus the counterparties or sides (`buy` / `sell`) involved.

Key aspects of Nitro Spreads:

  * All Spreads have **publicly accessible** Central Limit Order Books **(CLOB)**.
  * The availability of trading Spreads is determined by OKX. Typically, these Spreads encompass all possible combinations of delta one derivatives (Expiry Futures and Perpetual Futures) and SPOT within a specific instrument family (e.g. "BTC/USDT" or "ETH/USDC").
  * **Partial fills** and multiple orders can be consumed as part of a single trade.
  * **Counterparties** are **NOT** selected. All Spread Order Books can be engaged by anyone, effectively trading against the broader market.
  * Anonymity is maintained throughout the process, with all orders and trades conducted on an **anonymous basis**.
  * Users have the flexibility to place multiple orders on both the bid and ask sides of the Order Book, allowing for a **ladder-style** configuration.

## Comprehensive API Workflow

Notifications regarding Orders and Trades will be received by both the Taker and the Maker through the WebSocket Notification channels. 

A user assumes the role of a _Maker_ when their Order is executed upon by another Order. A user becomes a _Taker_ when they submit an Order that crosses an existing Order in the Order Book.

### Obtaining Available Spreads

To retrieve all available Spreads for trading on OKX, make a request to the `GET /api/v5/sprd/spreads` endpoint.

### Retrieving Your Orders

To retrieve orders on OKX, make a request to the `GET /api/v5/sprd/order` endpoint.

### Retrieving Your Trades

To retrieve trades on OKX, make a request to the `GET /api/v5/sprd/trades` endpoint.

### Submitting an Order

To submit an order to a Spread's Order Book, make a request to the `POST /api/v5/sprd/order` endpoint.

### Spread States

There are three different states during a Spread's life cycle: `live`, `suspend`, and `expired` as detailed below:

  1. `live`: Spreads that are actively traded on Nitro Spreads
  2. `suspend`: Spreads in which at least one of the legs is suspended and the other one is active or suspended on the OKX orderbook exchange; or spreads in which the underlying instruments are still live on the OKX orderbook exchange, but removed from Nitro Spreads
  3. `expired`: Spreads in which at least one of the underlying instruments is expired on the OKX orderbook exchange

Please refer to the following table for all possible scenarios given the state of the underlying instruments and the resulting state of the spread on Nitro Spreads (except for the case that the spread is delisted on Nitro Spreads):

Instrument A | Instrument B | Spread State  
---|---|---  
Live | Live | Live  
Suspend | Live | Suspend  
Live | Suspend | Suspend  
Suspend | Suspend | Suspend  
Expired | Live | Expired  
Live | Expired | Expired  
Suspend | Expired | Expired  
Expired | Suspend | Expired  
Expired | Expired | Expired  
  
### Trade Lifecycle

In order for a trade to take place, two orders must be crossed within a Spread's Order Book.

Obtain information about the state of an Order and determine if it has reached its final state by monitoring the `sprd-orders`WebSocket channel. The `state` key in the channel indicates the current state of the Order. If the state is `live` or `partially_filled`, it means that the Order still has available size (`sz`) that the creator or another user can take action on. On the other hand, if the state is `canceled` or `filled`, the Order no longer has any available actions that the creator or any other user can take action on.

It is important to closely track the values of the following attributes: `sz`(size),`pendingFillSz` (pending fill size), `canceledSz` (canceled size), and `accFillSz`(accumulated fill size). These attributes provide crucial information regarding the status and progression of the Order.

### Order State

Track the state of an order by subscribing to the `sprd-orders` WebSocket channel.

  1. Upon submitting an order, whether as a Maker or Taker, an order update message is sent via the orders WebSocket channel. The message will indicate the order's `state` == `live`.
  2. Order matching and trade settlement are asynchronous processes. When the order is matched but not settled, system pushes `pendingSettleSz` > 0 and `fillSz` == ""
  3. If the order is partially filled, an order update message is sent with `state` == `partially_filled`.
  4. In the event that the order is completely filled, an order update message is sent with the `state` == `filled`.
  5. If the order is not fully filled but has reached its final state, an order update message is sent with the `state` == `canceled`.
  6. If a certain part of an order is rejected, an order update message is sent with updated `canceledSz` and `pendingFillSz`, and `code` and `msg` corresponding to the error.

### Trade State

Track the state of a trade by subscribing to the `sprd-trades`WebSocket channel.

  1. After an executed trade undergoes clearing and settlement on OKX, it reaches finality.
  2. For successfully cleared trades, a WebSocket message is sent with the `state`denoted as `filled`.
  3. In the case of an unsuccessful trade clearing, a trade update message is sent with the `state` reflected as `rejected`.
  4. If the trade state is `rejected`, the trade update message will also include the error `code` and a corresponding error message (`msg`) that explains the reason for the rejection.

### All Trades

All users have the ability to receive updates on all trades that take place through the OKX Nitro Spreads product.

It's important to note that OKX Nitro Spreads does not disclose information about the counterparties involved in the trades or the individual `side` (`buy` or `sell`) of the composite legs that were traded.

  1. By subscribing to the `sprd-public-trades`WebSocket channel, WebSocket messages are sent exclusively for trades that have been successfully cleared and settled.

## REST API

### Place order

Place a new order

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/sprd/order`

> Request Example
    
    
    # place order for a spread
    POST /api/v5/sprd/order
    body
    {
       "sprdId":"BTC-USDT_BTC-USDT-SWAP",
       "clOrdId":"b15",
       "side":"buy",
       "ordType":"limit",
       "px":"2.15",
       "sz":"2"
    }
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # place order
    result = spreadAPI.place_order(sprdId='BTC-USDT_BTC-USDT-SWAP',
                                   clOrdId='b16',side='buy',ordType='limit',
                                   px='2',sz='2')
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USD-SWAP  
clOrdId | String | No | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
tag | String | No | Order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
side | String | Yes | Order side, `buy` `sell`  
ordType | String | Yes | Order type  
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order  
`ioc`: Immediate-or-cancel order  
sz | String | Yes | Quantity to buy or sell. The unit is USD for inverse spreads, and the corresponding baseCcy for linear and hybrid spreads.  
px | String | Yes | Order price. Only applicable to `limit`, `post_only`, `ioc`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "clOrdId": "b15",
          "ordId": "312269865356374016",
          "tag": "",
          "sCode": "0",
          "sMsg": ""
        }
      ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
sCode | String | The code of the event execution result, 0 means success.  
sMsg | String | Rejection or success message of event execution.  
clOrdId   
clOrdId is a user-defined unique ID used to identify the order. It will be included in the response parameters if you have specified during order submission, and can be used as a request parameter to the endpoints to query, cancel and amend orders. clOrdId must be unique among the clOrdIds of all pending orders.  ordType   
Order type. When creating a new order, you must specify the order type. The order type you specify will affect: 1) what order parameters are required, and 2) how the matching system executes your order. The following are valid order types:  
limit: Limit order, which requires specified sz and px.  
post_only: Post-only order, which the order can only provide liquidity to the market and be a maker. If the order would have executed on placement, it will be canceled instead. ioc: Immediate-or-cancel order  sz   
The sz unit for inverse spreads is USD in Nitro Spread, as opposed to contract in OKX orderbook. 

### Cancel order

Cancel an incomplete order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/sprd/cancel-order`

> Request Example
    
    
    POST /api/v5/sprd/cancel-order
    body
    {
        "ordId":"2510789768709120"
    }
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # cancel order
    result = spreadAPI.cancel_order(ordId='1905309079888199680')
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required. If both are passed, `ordId` will be used.  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "clOrdId":"oktswap6",
                "ordId":"12345689",
                "sCode":"0",
                "sMsg":""
            }
        ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
sCode | String | The code of the event execution result, 0 means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the order channel or the get order state. 

### Cancel All orders

Cancel all pending orders.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/sprd/mass-cancel`

> Request Example
    
    
    POST /api/v5/sprd/mass-cancel
    body
    {
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
    }
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # cancel all
    result = spreadAPI.cancel_all_orders(sprdId="BTC-USDT_BTC-USDT-SWAP")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | No | spread ID  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "result":true
            }
        ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
result | Boolean | Result of the request `true`, `false`  
Getting a response with result=true means your request has been successfully received and will be processed. The result of the cancellation is subject to the state pushed by the order channel or the get order state. 

### Amend order

Amend an incomplete order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/sprd/amend-order`

> Request Example
    
    
    POST /api/v5/sprd/amend-order
    body
    {
        "ordId":"2510789768709120",
        "newSz":"2"
    }
    
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required. If both are passed, ordId will be used.  
clOrdId | String | Conditional | Client Order ID as assigned by the client  
reqId | String | No | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.   
The response will include the corresponding reqId to help you identify the request if you provide it in the request.  
newSz | String | Conditional | New quantity after amendment   
Either `newSz` or `newPx` is required.   
When amending a partially-filled order, the newSz should include the amount that has been filled.  
newPx | String | Conditional | New price after amendment   
Either `newSz` or `newPx` is required.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
             "clOrdId":"",
             "ordId":"12344",
             "reqId":"b12344",
             "sCode":"0",
             "sMsg":""
            }
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client.  
reqId | String | Client Request ID as assigned by the client for order amendment.  
sCode | String | The code of the event execution result, 0 means success.  
sMsg | String | Rejection message if the request is unsuccessful.  
newSz  
If the new quantity of the order is less than or equal to the (accFillSz + canceledSz + pendingSettleSz), after pendingSettleSz is settled, the order status will be transitioned into filled (if canceledSz = 0), or canceled (if canceledSz > 0).  The amend order returns sCode equal to 0  
It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query. 

### Get order details

Retrieve order details.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/order`

> Request Example
    
    
    GET /api/v5/sprd/order?ordId=2510789768709120
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get order details
    result = spreadAPI.get_order_details(ordId='1905309079888199680')
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used  
clOrdId | String | Conditional | Client Order ID as assigned by the client. The latest order will be returned.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "instId": "BTC-USD-200329",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price  
sz | String | Quantity to buy or sell  
ordType | String | Order type  
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
side | String | Order side  
fillSz | String | Last fill quantity  
fillPx | String | Last fill price  
tradeId | String | Last trade ID  
accFillSz | String | Accumulated fill quantity  
pendingFillSz | String | Live quantity  
pendingSettleSz | String | Quantity that's pending settlement  
canceledSz | String | Quantity canceled due order cancellations or trade rejections  
avgPx | String | Average filled price. If none is filled, it will return "0".  
state | String | State   
`canceled`   
`live`   
`partially_filled`   
`filled`  
cancelSource | String | Source of the order cancellation.Valid values and the corresponding meanings are:   
`0`: Order canceled by system   
`1`: Order canceled by user   
`14`: Order canceled: IOC order was partially canceled due to incompletely filled  
`15`: Order canceled: The order price is beyond the limit  
`20`: Cancel all after triggered   
`31`: The post-only order will take liquidity in maker orders  
`32`: Self trade prevention  
`34`: Order failed to settle due to insufficient margin   
`35`: Order cancellation due to insufficient margin from another order  
`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit.  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
Order sizes equation: pendingFillSz + canceledSz + accFillSz = sz 

### Get active orders

Retrieve all incomplete orders under the current account.

#### Rate Limit: 10 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/orders-pending`

> Request Example
    
    
    GET /api/v5/sprd/orders-pending
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get active orders
    result = spreadAPI.get_active_orders()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | No | spread ID, e.g.  
ordType | String | No | Order type  
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
state | String | No | State   
`live`   
`partially_filled`  
beginId | String | No | Start order ID the request to begin with. Pagination of data to return records newer than the requested order Id, not including beginId  
endId | String | No | End order ID the request to end with. Pagination of data to return records earlier than the requested order Id, not including endId  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price  
sz | String | Quantity to buy or sell  
ordType | String | Order type  
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
side | String | Order side  
fillSz | String | Last fill quantity  
fillPx | String | Last fill price  
tradeId | String | Last trade ID  
accFillSz | String | Accumulated fill quantity  
pendingFillSz | String | Quantity still remaining to be filled  
pendingSettleSz | String | Quantity that's pending settlement  
canceledSz | String | Quantity canceled due order cancellations or trade rejections  
avgPx | String | Average filled price. If none is filled, it will return "0".  
state | String | State   
`live`   
`partially_filled`  
cancelSource | String | Source of the order cancellation.Valid values and the corresponding meanings are:   
`0`: Order canceled by system   
`1`: Order canceled by user   
`14`: Order canceled: IOC order was partially canceled due to incompletely filled  
`15`: Order canceled: The order price is beyond the limit  
`20`: Cancel all after triggered   
`31`: The post-only order will take liquidity in maker orders  
`32`: Self trade prevention   
`34`: Order failed to settle due to insufficient margin   
`35`: Order cancellation due to insufficient margin from another order  
`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit.  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get orders (last 21 days)

Retrieve the completed order data for the last 21 days, and the incomplete orders (filledSz =0 & state = canceled) that have been canceled are only reserved for 2 hours. Results are returned in counter chronological order of orders creation.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/orders-history`

> Request Example
    
    
    GET /api/v5/sprd/orders-history
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get orders history
    result = spreadAPI.get_orders()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | No | spread ID, e.g.  
ordType | String | No | Order type  
`market`: Market order   
`limit`: limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
state | String | No | State   
`canceled`   
`filled`  
beginId | String | No | Start order ID the request to begin with. Pagination of data to return records newer than the requested order Id, not including beginId  
endId | String | No | End order ID the request to end with. Pagination of data to return records earlier than the requested order Id, not including endId  
begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`. Date older than 7 days will be truncated.  
end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
         {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price  
sz | String | Quantity to buy or sell  
ordType | String | Order type  
`market`: Market order   
`limit`: limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
side | String | Order side  
fillSz | String | Last fill quantity  
fillPx | String | Last fill price  
tradeId | String | Last trade ID  
accFillSz | String | Accumulated fill quantity  
pendingFillSz | String | Quantity still remaining to be filled, inluding pendingSettleSz  
pendingSettleSz | String | Quantity that's pending settlement  
canceledSz | String | Quantity canceled due order cancellations or trade rejections  
avgPx | String | Average filled price. If none is filled, it will return "0".  
state | String | State   
`canceled`   
`filled`  
cancelSource | String | Source of the order cancellation. Valid values and the corresponding meanings are:   
`0`: Order canceled by system   
`1`: Order canceled by user   
`14`: Order canceled: IOC order was partially canceled due to incompletely filled  
`15`: Order canceled: The order price is beyond the limit  
`20`: Cancel all after triggered   
`31`: The post-only order will take liquidity in maker orders  
`32`: Self trade prevention  
`34`: Order failed to settle due to insufficient margin   
`35`: Order cancellation due to insufficient margin from another order  
`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit.  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get orders history (last 3 months)

Retrieve the completed order data for the last 3 months, including those placed 3 months ago but completed in the last 3 months. Results are returned in counter chronological order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/orders-history-archive`

> Request Example
    
    
    GET /api/v5/sprd/orders-history-archive
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | No | spread ID, e.g.  
ordType | String | No | Order type  
`market`: Market order   
`limit`: limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
state | String | No | State   
`canceled`   
`filled`  
instType | String | No | Instrument type  
`SPOT`  
`FUTURES`  
`SWAP`   
Any orders with spreads containing the specified instrument type in any legs will be returned  
instFamily | String | No | Instrument family, e.g. BTC-USDT. Any orders with spreads containing the specified instrument family in any legs will be returned  
beginId | String | No | Start order ID the request to begin with. Pagination of data to return records newer than the requested order Id, not including beginId  
endId | String | No | End order ID the request to end with. Pagination of data to return records earlier than the requested order Id, not including endId  
begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
         {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "canceled",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    

#### Response Example

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
px | String | Price  
sz | String | Quantity to buy or sell  
ordType | String | Order type  
`market`: Market order   
`limit`: limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
side | String | Order side  
fillSz | String | Last fill quantity  
fillPx | String | Last fill price  
tradeId | String | Last trade ID  
accFillSz | String | Accumulated fill quantity  
pendingFillSz | String | Quantity still remaining to be filled, inluding pendingSettleSz  
pendingSettleSz | String | Quantity that's pending settlement  
canceledSz | String | Quantity canceled due order cancellations or trade rejections  
avgPx | String | Average filled price. If none is filled, it will return "0".  
state | String | State   
`canceled`   
`filled`  
cancelSource | String | Source of the order cancellation. Valid values and the corresponding meanings are:   
`0`: Order canceled by system   
`1`: Order canceled by user   
`14`: Order canceled: IOC order was partially canceled due to incompletely filled  
`15`: Order canceled: The order price is beyond the limit  
`20`: Cancel all after triggered   
`31`: The post-only order will take liquidity in maker orders  
`32`: Self trade prevention  
`34`: Order failed to settle due to insufficient margin   
`35`: Order cancellation due to insufficient margin from another order  
`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit.  
uTime | String | Update time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### Get trades (last 7 days)

Retrieve historical transaction details **for the last 7 days**. Results are returned in counter chronological order.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/trades`

> Request Example
    
    
    GET /api/v5/sprd/trades
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get private trades
    result = spreadAPI.get_trades()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | No | spread ID, e.g.  
tradeId | String | No | Trade ID  
ordId | String | No | Order ID  
beginId | String | No | Start trade ID the request to begin with. Pagination of data to return records newer than the requested tradeId, not including beginId  
endId | String | No | End trade ID the request to end with. Pagination of data to return records earlier than the requested tradeId, not including endId  
begin | String | No | Filter with a begin timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
end | String | No | Filter with an end timestamp. Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is 100. The default is 100  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT-SWAP_BTC-USDT-200329",
                "tradeId": "123",
                "ordId": "123445",
                "clOrdId": "b16",
                "tag": "",
                "fillPx": "999",
                "fillSz": "3",
                "state": "filled",
                "side": "buy",
                "execType": "M",
                "ts": "1597026383085",
                "legs": [
                    {
                        "instId": "BTC-USDT-SWAP",
                        "px": "20000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "buy",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "1232342342"
                    },
                    {
                        "instId": "BTC-USDT-200329",
                        "px": "21000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "sell",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "5345646634"
                    }
                ],
                "code": "",
                "msg": ""
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
tradeId | String | Trade ID  
ordId | String | Order ID  
clOrdId | String | Client Order ID as assigned by the client  
tag | String | Order tag  
fillPx | String | Filled price  
fillSz | String | Filled quantity  
side | String | Order side, `buy` `sell`  
state | String | Trade state.   
Valid values are `filled` and `rejected`  
execType | String | Liquidity taker or maker, `T`: taker `M`: maker  
ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
legs | Array of objects | Legs of trade  
> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
> px | String | The price the leg executed  
> sz | String | The size of each leg  
> szCont | String | Filled amount of the contract   
Only applicable to contracts, return "" for spot  
> side | String | The direction of the leg. Valid value can be `buy` or `sell`.  
> fillPnl | String | Last filled profit and loss, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
> fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive number represents rebate.  
> feeCcy | String | Fee currency  
> tradeId | String | Traded ID in the OKX orderbook.  
code | String | Error Code, the default is 0  
msg | String | Error Message, the default is ""  
  
### Get Spreads (Public)

Retrieve all available spreads based on the request parameters.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/spreads`

> Request Example
    
    
    GET /api/v5/sprd/spreads?instId=BTC-USDT
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get spreads
    result = spreadAPI.get_spreads()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
baseCcy | string | No | Currency instrument is based in, e.g. BTC, ETH  
instId | String | No | The instrument ID to be included in the spread.  
sprdId | String | No | The spread ID  
state | string | No | Spreads which are available to trade, suspened or expired. Valid values include `live`, `suspend` and `expired`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "sprdId": "ETH-USD-SWAP_ETH-USD-231229",
                "sprdType": "inverse",
                "state": "live",
                "baseCcy": "ETH",
                "szCcy": "USD",
                "quoteCcy": "USD",
                "tickSz": "0.01",
                "minSz": "10",
                "lotSz": "10",
                "listTime": "1686903000159",
                "legs": [{
                        "instId": "ETH-USD-SWAP",
                        "side": "sell"
                    },
                    {
                        "instId": "ETH-USD-231229",
                        "side": "buy"
                    }
                ],
                "expTime": "1703836800000",
                "uTime": "1691376905595"
            },
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "sprdType": "linear",
                "state": "live",
                "baseCcy": "BTC",
                "szCcy": "BTC",
                "quoteCcy": "USDT",
                "tickSz": "0.0001",
                "minSz": "0.001",
                "lotSz": "1",
                "listTime": "1597026383085",
                "expTime": "1597029999085",
                "uTime": "1597028888085",
                "legs": [{
                        "instId": "BTC-USDT",
                        "side": "sell"
                    },
                    {
                        "instId": "BTC-USDT-SWAP",
                        "side": "buy"
                    }
                ]
            },
            {
                "sprdId": "BTC-USDT_BTC-USDT-230317",
                "sprdType": "linear",
                "state": "live",
                "baseCcy": "BTC",
                "szCcy": "BTC",
                "quoteCcy": "USDT",
                "tickSz": "0.0001",
                "minSz": "0.001",
                "lotSz": "1",
                "listTime": "1597026383085",
                "expTime": "1597029999085",
                "uTime": "1597028888085",
                "legs": [{
                        "instId": "BTC-USDT",
                        "side": "sell"
                    },
                    {
                        "instId": "BTC-USDT-230317",
                        "side": "buy"
                    }
                ]
            }
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
sprdType | String | spread Type. Valid values are `linear`, `inverse`, `hybrid`  
state | String | Current state of the spread. Valid values include `live`, `expired`, `suspend`.  
baseCcy | String | Currency instrument is based in. Valid values include BTC, ETH  
szCcy | String | The currency the spread order size is submitted to the underlying venue in, e.g. USD, BTC, ETH.  
quoteCcy | String | The currency the spread is priced in, e.g. USDT, USD  
tickSz | String | Tick size, e.g. 0.0001 in the quoteCcy of the spread.  
minSz | String | Minimum order size in the szCcy of the spread.  
lotSz | String | The minimum order size increment the spread can be traded in the szCcy of the spread.  
listTime | String | The timestamp the spread was created. Unix timestamp format in milliseconds, , e.g. `1597026383085`  
expTime | String | Expiry time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
uTime | String | The timestamp the spread was last updated. Unix timestamp format in milliseconds, e.g. `1597026383085`  
legs | array of objects |   
> instId | String | Instrument ID, e.g. BTC-USD-SWAP  
> side | String | The direction of the leg of the spread. Valid Values include `buy` and `sell`.  
  
### Get order book (Public)

Retrieve the order book of the spread.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/books`

> Request Example
    
    
    GET /api/v5/sprd/books?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get order book
    result = spreadAPI.get_order_book(sprdId="BTC-USDT_BTC-USDT-SWAP", sz=20)
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USDT-SWAP  
sz | String | No | Order book depth per side. Maximum value is 400. Default value is 5.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8", // price
                        "0.60038921", // quantity
                        "1" // number of orders at the price
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "2"
                    ]
                ],
                "ts": "1629966436396"
            }
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
asks | Array of arrays | Order book on sell side  
bids | Array of arrays | Order book on buy side  
ts | String | Order book generation time  
An example of the array of asks and bids values: ["411.8", "10", "4"]  
\- "411.8" is the depth price  
\- "10" is the quantity at the price (Unit: szCcy)  
\- "4" is the number of orders at the price.  

### Get ticker (Public)

Retrieve the latest price snapshot, best bid/ask price and quantity.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/sprd-ticker`

> Request Example
    
    
    GET /api/v5/market/sprd-ticker?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USDT-SWAP  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "last": "14.5",
                "lastSz": "0.5",
                "askPx": "8.5",
                "askSz": "12.0",
                "bidPx": "0.5",
                "bidSz": "12.0",
                "open24h": "4",
                "high24h": "14.5",
                "low24h": "-2.2",
                "vol24h": "6.67",
                "ts": "1715331406485"
            }
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
last | String | Last traded price  
lastSz | String | Last traded size  
askPx | String | Best ask price  
askSz | String | Best ask size  
bidPx | String | Best bid price  
bidSz | String | Best bid size  
open24h | String | Open price in the past 24 hours  
high24h | String | Highest price in the past 24 hours  
low24h | String | Lowest price in the past 24 hours  
vol24h | String | 24h trading volume  
The unit is USD for inverse spreads, and the corresponding baseCcy for linear and hybrid spreads.  
ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. 1597026383085.  
  
### Get public trades (Public)

Retrieve the recent transactions of an instrument (at most 500 records per request). Results are returned in counter chronological order. 

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### Permission: Read

#### HTTP Request

`GET /api/v5/sprd/public-trades`

> Request Example
    
    
    GET /api/v5/sprd/public-trades?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # Production trading:0 , demo trading:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # get public trades
    result = spreadAPI.get_public_trades(sprdId='ETH-USDT-SWAP_ETH-USDT-230929')
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | No | Spread ID, e.g. BTC-USDT_BTC-USDT-SWAP  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDC-SWAP",
                "side": "sell",
                "sz": "0.1",
                "px": "964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
sprdId | String | spread ID  
tradeId | String | Trade ID  
px | String | Trade price  
sz | String | Trade quantity  
side | String | Trade side of the taker.   
`buy`   
`sell`  
ts | String | Trade time, Unix timestamp format in milliseconds, e.g. `1597026383085`.  
  
### Get candlesticks

Retrieve the candlestick charts. This endpoint can retrieve the latest 1,440 data entries. Charts are returned in groups based on the requested bar.

#### Rate Limit: 40 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/sprd-candles`

> Request Example
    
    
    GET /api/v5/market/sprd-candles?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | Yes | Spread ID  
bar | String | No | Bar size, the default is 1m, e.g. [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8 opening price k-line:[6H/12H/1D/2D/3D/1W/1M/3M]   
UTC+0 opening price k-line:[/6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
after | String | No | Pagination of data to return records earlier than the requested ts  
before | String | No | Pagination of data to return records newer than the requested ts. The latest data will be returned when using before individually  
limit | String | No | Number of results per request. The maximum is 300. The default is 100.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "0"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "1"
        ]
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. 1597026383085  
o | String | Open price  
h | String | highest price  
l | String | Lowest price  
c | String | Close price  
vol | String | Trading volume  
confirm | String | The state of candlesticks.   
`0` represents that it is uncompleted   
`1` represents that it is completed.  
The first candlestick data may be incomplete, and should not be polled repeatedly.   
The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,confirm]. 

### Get candlesticks history

Retrieve history candlestick charts from recent years.

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/market/sprd-history-candles`

> Request Example
    
    
    GET /api/v5/market/sprd-history-candles?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
sprdId | String | Yes | Spread ID  
after | String | No | Pagination of data to return records earlier than the requested ts  
before | String | No | Pagination of data to return records newer than the requested ts. The latest data will be returned when using before individually  
bar | String | No | Bar size, the default is 1m, e.g. [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8 opening price k-line:[6H/12H/1D/2D/3D/1W/1M/3M]   
UTC+0 opening price k-line:[6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
limit | String | No | Number of results per request. The maximum is 100. The default is 100.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "1"
        ]
        ]
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. 1597026383085  
o | String | Open price  
h | String | Highest price  
l | String | Lowest price  
c | String | Close price  
vol | String | Trading volume  
confirm | String | The state of candlesticks.   
`0` represents that it is uncompleted   
`1` represents that it is completed.  
The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,confirm] 

### Cancel All After

Cancel all pending orders after the countdown timeout. Only applicable to spread trading.

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/sprd/cancel-all-after`

> Request Example
    
    
    POST /api/v5/sprd/cancel-all-after
    {
       "timeOut":"30"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
timeOut | String | Yes | The countdown for order cancellation, with second as the unit.  
Range of value can be 0, [10, 120].   
Setting timeOut to 0 disables Cancel All After.  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "ts":"1587971400"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
triggerTime | String | The time the cancellation is triggered.  
triggerTime=0 means Cancel All After is disabled.  
ts | String | The time the request is received.  
Users are recommended to send a request to the exchange every second. When the cancel all after is triggered, the trading engine will cancel orders on behalf of the client one by one and this operation may take up to a few seconds. This feature is intended as a protection mechanism for clients only and clients should not use this feature as part of their trading strategies. 

## Websocket Trade API

### WS / Place order

You can place an order only if you have sufficient funds.  

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the Nitro Spread `Place order` REST API endpoints 

> Request Example
    
    
    {
      "id": "1512",
      "op": "sprd-order",
      "args": [
        {
           "sprdId":"BTC-USDT_BTC-USDT-SWAP",
           "clOrdId":"b15",
           "side":"buy",
           "ordType":"limit",
           "px":"2.15",
           "sz":"2"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`sprd-order`  
args | Array of objects | Yes | Request parameters  
> sprdId | String | Yes | spread ID, e.g. BTC-USDT_BTC-USD-SWAP  
> clOrdId | String | No | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
> tag | String | No | Order tag   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
> side | String | Yes | Order side   
`buy`   
`sell`  
> ordType | String | Yes | Order type:  
`market`: Market order   
`limit`: Limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
> sz | String | Yes | Quantity to buy or sell  
> px | String | Yes | Order price. Only applicable to `limit, post_only, ioc` order.  
  
> ##### Successful Response Example
    
    
    {
      "id": "1512",
      "op": "sprd-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "12345689",
          "tag": "",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": ""
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "op": "sprd-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "",
          "tag": "",
          "sCode": "5XXXX",
          "sMsg": "not exist"
        }
      ],
      "code": "1",
      "msg": ""
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "sprd-order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tag | String | Order tag  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Rejection or success message of event execution.  
clOrdId  
clOrdId is a user-defined unique ID used to identify the order. It will be included in the response parameters if you have specified during order submission, and can be used as a request parameter to the endpoints to query, cancel and amend orders.   
clOrdId must be unique among the clOrdIds of all pending orders. 

### WS / Amend order

Amend an incomplete order.

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the `Amend order` REST API endpoints 

> Request Example
    
    
    {
       "id":"1512",
       "op":"sprd-amend-order",
       "args":[
          {
             "ordId":"2510789768709120",
             "newSz":"2"
          }
       ]
    }
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the messageProvided by client.   
It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`sprd-amend-order`  
args | Array of objects | Yes | Request Parameters  
> ordId | String | Conditional | Order ID   
Either `ordId` or `clOrdId` is required, if both are passed, `ordId` will be used.  
> clOrdId | String | Conditional | Client Order ID as assigned by the client  
> reqId | String | No | Client Request ID as assigned by the client for order amendment   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
> newSz | String | Conditional | New quantity after amendment.   
Either `newSz` or `newPx` is required. When amending a partially-filled order, the newSz should include the amount that has been filled and failed.  
> newPx | String | Conditional | New price after amendment.  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "reqId": "b12344",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": ""
    }
    
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "reqId": "b12344",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        }
      ],
      "code": "1",
      "msg": ""
    }
    
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args"
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> reqId | String | Client Request ID as assigned by the client for order amendment  
> sCode | String | Order status code, 0 means success  
> sMsg | String | Order status message  
newSz  
If the new quantity of the order is less than or equal to the (accFillSz + canceledSz + pendingSettleSz), after pendingSettleSz is settled, the order status will be transitioned into filled (if canceledSz = 0), or canceled (if canceledSz > 0).  The amend order returns sCode equal to 0  
It is not strictly considered that the order has been amended. It only means that your amend order request has been accepted by the system server. The result of the amend is subject to the status pushed by the order channel or the order status query. 

### WS / Cancel order

Cancel an incomplete order

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 20 requests per 2 seconds

#### Rate limit rule: User ID

Rate limit is shared with the Nitro Spread `Cancel order` REST API endpoints 

> Request Example
    
    
    {
      "id": "1514",
      "op": "sprd-cancel-order",
      "args": [
        {
          "ordId": "2510789768709120"
        }
      ]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`sprd-cancel-order`  
args | Array of objects | Yes | Request Parameters  
> ordId | String | Conditional | Order ID   
Either ordId or clOrdId is required, if both are passed, ordId will be used  
> clOrdId | String | Conditional | Client Order ID as assigned by the client   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
  
> Successful Response Example
    
    
    {
      "id": "1514",
      "op": "sprd-cancel-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": ""
    }
    

> Failure Response Example
    
    
    {
      "id": "1514",
      "op": "sprd-cancel-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "sCode": "5XXXX",
          "sMsg": "Order not exist"
        }
      ],
      "code": "1",
      "msg": ""
    }
    

> Response Example When Format Error
    
    
    {
      "id": "1514",
      "op": "sprd-cancel-order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> sCode | String | Order status code, `0` means success  
> sMsg | String | Order status message  
Cancel order returns with sCode equal to 0. It is not strictly considered that the order has been canceled. It only means that your cancellation request has been accepted by the system server. The result of the cancellation is subject to the state pushed by the sprd-orders channel or the get order state.  

### WS / Cancel all orders

#### URL Path

/ws/v5/business (required login)

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

> Request Example
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "args": [{
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }]
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | Yes | Unique identifier of the message provided by client. It will be returned in response message to identify the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`sprd-mass-cancel`  
args | Array of objects | Yes | Request parameters  
> sprdId | String | No | spread ID  
  
> ##### Successful Response Example
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "data": [
            {
                "result": true
            }
        ],
        "code": "0",
        "msg": ""
    } 
    

> Response Example When Format Error
    
    
    {
      "id": "1512",
      "op": "sprd-mass-cancel",
      "data": [],
      "code": "60013",
      "msg": "Invalid args"
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
id | String | Unique identifier of the message  
op | String | Operation  
code | String | Error Code  
msg | String | Error message  
data | Array of objects | Data  
> result | Boolean | Result of the request `true`, `false`  
  
## WebSocket Private Channel

  * Production Trading URL: `wss://ws.okx.com:8443/ws/v5/business`
  * Demo Trading URL: `wss://wspap.okx.com:8443/ws/v5/business`

### Order channel

Retrieve order information from the `sprd-order` Websocket channel. Data will not be pushed when first subscribed. Data will only be pushed when triggered by events such as placing/canceling order.

#### URL Path

/ws/v5/business (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-orders",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-orders",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> Request Example:
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-orders",
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-orders",
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`sprd-orders`  
> sprdId | String | No | Spread ID  
  
> Successful Response Example : single
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-orders",
        "sprdId": "BTC-USDT_BTC-UST-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-orders"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example 
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-orders\", \"instType\" : \"FUTURES\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### Response parameters

Parameter | Required | Type | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | Yes | String | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | No | Object | Subscribed channel  
> channel | Yes | String | Channel name  
> sprdId | No | String | Spread ID  
code | No | String | Error code  
msg | No | String | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: single
    
    
    {
      "arg": {
            "channel": "sprd-orders",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP",
            "uid": "614488474791936"
        },
      "data": [
         {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085",
          "code": "0",
          "msg": "",
          "reqId": "",
          "amendResult": ""
        }
      ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> sprdId | String | spread ID  
data | Array of objects | Subscribed data  
> sprdId | String | spread ID, e.g.  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tag | String | Order tag  
> px | String | Order price  
> sz | String | The original order quantity, in the unit of szCcy  
> ordType | String | Order type  
`market`: Market order   
`limit`: limit order   
`post_only`: Post-only order   
`ioc`: Immediate-or-cancel order  
> side | String | Order side, buy sell  
> fillSz | String | Last trade quantity, only applicable to order updates representing successful settlement  
> fillPx | String | Last trade price, only applicable to order updates representing successful settlement  
> tradeId | String | Last trade ID  
> accFillSz | String | Accumulated fill quantity  
> pendingFillSz | String | Quantity still remaining to be filled  
> pendingSettleSz | String | Quantity that's pending settlement  
> canceledSz | String | Quantity canceled due order cancellations or trade rejections  
> avgPx | String | Average filled price. If none is filled, it will return "0".  
> state | String | Order state:   
`canceled`   
`live`   
`partially_filled`   
`filled`  
> cancelSource | String | Source of the order cancellation.Valid values and the corresponding meanings are:   
`0`: Order canceled by system   
`1`: Order canceled by user   
`14`: Order canceled: IOC order was partially canceled due to incompletely filled  
`15`: Order canceled: The order price is beyond the limit  
`20`: Cancel all after triggered   
`31`: The post-only order will take liquidity in maker orders  
`32`: Self trade prevention   
`34`: Order failed to settle due to insufficient margin   
`35`: Order cancellation due to insufficient margin from another order  
`44`: Your order was canceled because your available balance of this crypto was insufficient for auto conversion. Auto conversion was triggered when the total collateralized liabilities for this crypto reached the platform’s risk control limit.  
> uTime | String | Update time, Unix timestamp format in milliseconds, e.g. 1597026383085  
> cTime | String | Creation time, Unix timestamp format in milliseconds, e.g. 1597026383085  
> code | String | Error Code, the default is 0  
> msg | String | Error Message, the default is ""  
> reqId | String | Client Request ID as assigned by the client for order amendment. "" will be returned if there is no order amendment.  
> amendResult | String | The result of amending the order   
`-1`: failure   
`0`: success  
"" will be returned if there is no order amendment.  
  
### Trades channel

All updates relating to User's Trades are sent through the `sprd-trades` WebSocket Notifications channel.

This is a private channel and consumable solely by the authenticated user.

Updates received through the `sprd-trades` WebSocket Notification channel can include Trades being `filled` or `rejected`.

You may receive multiple notifications if an Order of yours interacts with more than one other Order.

#### URL Path

/ws/v5/business (required login)

> Request Example : single
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-trades",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> Request Example:
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-trades",
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-trades",
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`sprd-trades`  
> sprdId | String | No | Spread ID  
  
#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> sprdId | String | No | Spread ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "sprd-trades",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP",
            "uid": "614488474791936"
        },
        "data":[
             {
                "sprdId":"BTC-USDT-SWAP_BTC-USDT-200329",
                "tradeId":"123",
                "ordId":"123445",
                "clOrdId": "b16",
                "tag":"",
                "fillPx":"999",
                "fillSz":"3",
                "state": "filled",
                "side":"buy",
                "execType":"M",
                "ts":"1597026383085",
                "legs": [
                    {
                        "instId": "BTC-USDT-SWAP",
                        "px": "20000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "buy",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "1232342342"
                    },
                    {
                        "instId": "BTC-USDT-200329",
                        "px": "21000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "sell",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "5345646634"
                    },
                ]
                "code": "",
                "msg": ""
            }
        ]
    }
    

#### Push Data Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> uid | String | User Identifier  
> sprdId | String | spread ID  
data | Array of objects | Subscribed data  
> sprdId | String | spread ID  
> tradeId | String | Trade ID  
> ordId | String | Order ID  
> clOrdId | String | Client Order ID as assigned by the client  
> tag | String | Order tag  
> fillPx | String | Last filled price  
> fillSz | String | Last filled quantity  
> side | String | Order side, buy sell  
> state | String | Trade state. Valid values are filled and rejected  
> execType | String | Liquidity taker or maker   
`T`: taker   
`M`: maker  
>ts | String | Data generation time, Unix timestamp format in milliseconds, e.g. 1597026383085.  
> legs | Array of objects | Legs of trade  
>> instId | String | Instrument ID, e.g. BTC-USDT-SWAP  
>> px | String | The price the leg executed  
>> sz | String | Size of the leg in contracts or spot.  
>> szCont | String | Filled amount of the contract   
Only applicable to contracts, return "" for spot  
>> side | String | The direction of the leg. Valid value can be `buy` or `sell`.  
>> fillPnl | String | Last filled profit and loss, applicable to orders which have a trade and aim to close position. It always is 0 in other conditions  
>> fee | String | Fee. Negative number represents the user transaction fee charged by the platform. Positive number represents rebate.  
>> feeCcy | String | Fee currency  
>> tradeId | String | Traded ID in the OKX orderbook.  
> code | String | Error Code, the default is 0  
> msg | String | Error Message, the default is ""  
  
## WebSocket Public Channel

  * Production Trading URL: `wss://ws.okx.com:8443/ws/v5/business`
  * Demo Trading URL: `wss://wspap.okx.com:8443/ws/v5/business`

### Order book channel

Retrieve order book data. Available channels:

  * `sprd-bbo-tbt`: 1 depth level snapshot will be pushed in the initial push. Snapshot data will be pushed every 10 ms when there are changes in the 1 depth level snapshot.
  * `sprd-books5`: 5 depth levels snapshot will be pushed in the initial push. Snapshot data will be pushed every 100 ms when there are changes in the 5 depth levels snapshot.
  * `sprd-books-l2-tbt`: 400 depth levels will be pushed in the initial full snapshot. Incremental data will be pushed every 10 ms for the changes in the order book during that period of time. 
  * The push sequence for order book channels within the same connection and trading symbols is fixed as: sprd-bbo-tbt -> sprd-books-l2-tbt -> sprd-books5.

#### URL Path

/ws/v5/business

> Request Example: sprd-books5
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-books5",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-books5",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

> Request Example: sprd-books-l2-tbt
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-books-l2-tbt",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-books-l2-tbt",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
`sprd-bbo-tbt`  
`sprd-books5`  
`sprd-books-l2-tbt`  
> channel | String | Yes | Channel name  
> sprdId | String | Yes | spread ID  
  
> Successful Response Example: sprd-books5
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-books5",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> Successful Response Example: sprd-books-l2-tbt
    
    
    {
      "id": "1512",
       "event":"subscribe",
       "arg":{
          "channel":"sprd-books-l2-tbt",
          "sprdId":"BTC-USDT_BTC-USDT-SWAP"
       },
       "connId":"214fdd24"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"sprd-books5\", \"sprdId\" : \"BTC-USD_BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channels  
`sprd-bbo-tbt`  
`sprd-books5`  
`sprd-books-l2-tbt`  
> channel | String | Yes | Channel name  
> sprdId | String | Yes | spread ID  
msg | String | No | Error message  
code | String | No | Error code  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example: sprd-books5
    
    
    {
      "arg": {
        "channel": "sprd-books5",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            ["111.06","55154","2"],
            ["111.07","53276","2"],
            ["111.08","72435","2"],
            ["111.09","70312","2"],
            ["111.1","67272","2"]],
          "bids": [
            ["111.05","57745","2"],
            ["111.04","57109","2"],
            ["111.03","69563","2"],
            ["111.02","71248","2"],
            ["111.01","65090","2"]],
          "ts": "1670324386802",
          "seqId":1724294007352168320
        }
      ]
    }
    

> Push Data Example: sprd-books-l2-tbt
    
    
    {
       "arg":{
          "channel":"sprd-books-l2-tbt",
          "sprdId":"BTC-USDT_BTC-USDT-SWAP"
       },
       "action":"snapshot",
       "data":[
          {
             "asks":[
                ["1.9","1.1","3"],
                ["2.5","0.9","1"],
                ["3.2","4.921","1"],
                ["4.8","0.165","1"],
                ["5.2","4.921","1"]
              ......
             ],
             "bids":[
                ["1.8","0.165","1"],
                ["0.6","0.2","2"],
                ["0","23.49","1"],
                ["-0.1","1","1"],
                ["-0.6","1","1"],
                ["-3.9","4.921","1"]
                ......
             ],
             "ts":"1724391380926",
             "checksum":-1285595583,
             "prevSeqId":-1,
             "seqId":1724294007352168320
          }
       ]
    }
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> sprdId | String | spread ID  
action | String | Push data action, incremental data or full snapshot.  
`snapshot`: full  
`update`: incremental  
data | Array of objects | Subscribed data  
> asks | Array of strings | Order book on sell side  
> bids | Array of strings | Order book on buy side  
> ts | String | Order book generation time, Unix timestamp format in milliseconds, e.g. 1597026383085  
> checksum | Integer | Checksum, implementation details below. Only applicable to `sprd-books-l2-tbt`.  
> prevSeqId | Integer | Sequence ID of the last sent message. Only applicable to `sprd-books-l2-tbt`.  
> seqId | Integer | Sequence ID of the current message, implementation details below.  
An example of the array of asks and bids values: ["411.8", "10", "4"]  
\- "411.8" is the depth price  
\- "10" is the quantity at the price (Unit: szCcy)  
\- "4" is the number of orders at the price.  

#### Sequence ID

`seqId` is the sequence ID of the market data published. The set of sequence ID received by users is the same if users are connecting to the same channel through multiple websocket connections. Each `sprdId` has an unique set of sequence ID. Users can use `prevSeqId` and `seqId` to build the message sequencing for incremental order book updates. Generally the value of seqId is larger than prevSeqId. The `prevSeqId` in the new message matches with `seqId` of the previous message. The smallest possible sequence ID value is 0, except in snapshot messages where the prevSeqId is always -1.  

Exceptions:  
1\. If there are no updates to the depth for an extended period, OKX will send a message with `'asks': [], 'bids': []` to inform users that the connection is still active. `seqId` is the same as the last sent message and `prevSeqId` equals to `seqId`. 2\. The sequence number may be reset due to maintenance, and in this case, users will receive an incremental message with `seqId` smaller than `prevSeqId`. However, subsequent messages will follow the regular sequencing rule.

##### Example

  1. Snapshot message: prevSeqId = -1, seqId = 10
  2. Incremental message 1 (normal update): prevSeqId = 10, seqId = 15
  3. Incremental message 2 (no update): prevSeqId = 15, seqId = 15
  4. Incremental message 3 (sequence reset): prevSeqId = 15, seqId = 3
  5. Incremental message 4 (normal update): prevSeqId = 3, seqId = 5

#### Checksum

This mechanism can assist users in checking the accuracy of depth data.

##### Merging incremental data into full data

After subscribing to the incremental load push (such as `books` 400 levels) of Order Book Channel, users first receive the initial full load of market depth. After the incremental load is subsequently received, update the local full load.

  1. If there is the same price, compare the size. If the size is 0, delete this depth data. If the size changes, replace the original data.
  2. If there is no same price, sort by price (bid in descending order, ask in ascending order), and insert the depth information into the full load.

##### Calculate Checksum

Use the first 25 bids and asks in the full load to form a string (where a colon connects the price and size in an ask or a bid), and then calculate the CRC32 value (32-bit signed integer).

### Public Trades channel

Retrieve the recent trades data from `sprd-public-trades`. Data will be pushed whenever there is a trade. Every update contains only one trade.

#### URL Path

/ws/v5/business

> Request Example 
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-public-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-public-trades",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`sprd-public-trades`  
> sprdId | String | Yes | spread ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "sprd-public-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-public-trades\", \"instId\" : \"BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> sprdId | String | Yes | spread ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "sprd-public-trades",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "tradeId": "2499206329160695808",
                "px": "-10",
                "sz": "0.001",
                "side": "sell",
                "ts": "1726801105519"
            }
        ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> sprdId | String | spread ID  
data | Array of objects | Subscribed data  
> sprdId | String | spread ID, e.g.  
> tradeId | String | Trade ID  
> px | String | Trade price  
sz | String | Trade quantity   
For spot trading, the unit is base currency  
For `FUTURES`/`SWAP`/`OPTION`, the unit is contract.  
> side | String | Trade direction, buy, sell  
> ts | String | Filled time, Unix timestamp format in milliseconds, e.g. 1597026383085  
  
### Tickers channel

Retrieve the last traded price, bid price, ask price. The fastest rate is 1 update/100ms. There will be no update if the event is not triggered. The events which can trigger update: trade, the change on best ask/bid price

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-tickers",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-tickers",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation  
`subscribe`  
`unsubscribe`  
  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name  
`sprd-tickers`  
> sprdId | String | Yes | spread ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-tickers",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
      "connId": "a4d3ae55"
    }
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | No | Subscribed channel  
> channel | String | Yes | Channel name  
> sprdId | String | Yes | spread ID  
code | String | No | Error code  
msg | String | No | Error message  
connId | String | Yes | WebSocket connection ID  
  
> Push Data Example
    
    
    {
        "arg": {
            "channel": "sprd-tickers",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "last": "4",
                "lastSz": "0.01",
                "askPx": "19.7",
                "askSz": "5.79",
                "bidPx": "5.9",
                "bidSz": "5.79",
                "open24h": "-7",
                "high24h": "19.6",
                "low24h": "-7",
                "vol24h": "9.87",
                "ts": "1715247061026"
            }
        ]
    }
    

#### Push data parameters

**Parameter** | **Type** | **Description**  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> sprdId | String | spread ID  
data | Array of objects | Subscribed data  
> sprdId | String | spread ID  
> last | String | Last traded price  
> lastSz | String | Last traded size  
> askPx | String | Best ask price  
> askSz | String | Best ask size  
> bidPx | String | Best bid price  
> bidSz | String | Best bid size  
> open24h | String | Open price in the past 24 hours  
> high24h | String | Highest price in the past 24 hours  
> low24h | String | Lowest price in the past 24 hours  
> vol24h | String | 24h trading volume, with a unit of base currency or USD  
> ts | String | Ticker data generation time, Unix timestamp format in milliseconds, e.g. 1597026383085  
vol24h  
For Spot vs USDT-margined contracts spread and USDT-margined contracts spread, the volume is with the unit of base currency; for Crypto-margined contracts spread, the volume is with the unit of USD. 

### Candlesticks channel

Retrieve the candlesticks data of an instrument. The push frequency is the fastest interval 1 second push the data.

#### URL Path

/ws/v5/business

> Request Example
    
    
    {
      "id": "1512",
       "op":"subscribe",
       "args":[
          {
             "channel":"sprd-candle1D",
             "sprdId":"BTC-USDT_BTC-USDT-SWAP"
          }
       ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
          {
             "channel":"sprd-candle1D",
             "sprdId":"BTC-USDT_BTC-USDT-SWAP"
          }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### Request parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message   
Provided by client. It will be returned in response message for identifying the corresponding request.   
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters.  
op | String | Yes | Operation, subscribe unsubscribe  
args | Array of objects | Yes | List of subscribed channels  
> channel | String | Yes | Channel name   
`sprd-candle3M` `sprd-candle1M`   
`sprd-candle1W`   
`sprd-candle1D` `sprd-candle2D` `sprd-candle3D` `sprd-candle5D`   
`sprd-candle12H` `sprd-candle6H` `sprd-candle4H` `sprd-candle2H` `sprd-candle1H`   
`sprd-candle30m` `sprd-candle15m` `sprd-candle5m` `sprd-candle3m` `sprd-candle1m`   
`sprd-candle3Mutc` `sprd-candle1Mutc` `sprd-candle1Wutc` `sprd-candle1Dutc` `sprd-candle2Dutc` `sprd-candle3Dutc` `sprd-candle5Dutc` `sprd-candle12Hutc` `sprd-candle6Hutc`  
> sprdId | String | Yes | Spread ID  
  
> Successful Response Example
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-candle1D",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> Failure Response Example
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### Response parameters

Parameter | Type | Required | Description  
---|---|---|---  
id | String | No | Unique identifier of the message  
event | String | Yes | Event, subscribe unsubscribe error  
arg | Object | No | Subscribed channel  
channel | String | yes | channel name  
sprdId | String | Yes | Spread ID  
code | String | No | Error code  
msg | String | No | Error message  
  
> Push Data Example
    
    
    {
      "arg": {
        "channel": "sprd-candle1D",
        "sprdId": "BTC-USDT_BTC-USD-SWAP"
      },
      "data": [
        [
          "1597026383085",
          "8533.02",
          "8553.74",
          "8527.17",
          "8548.26",
          "45247",
          "0"
        ]
      ]
    }
    
    

#### Push data parameters

Parameter | Type | Description  
---|---|---  
arg | Object | Successfully subscribed channel  
> channel | String | Channel name  
> sprdId | String | Spread ID  
data | Array of Arrays | Subscribed data  
> ts | String | Opening time of the candlestick, Unix timestamp format in milliseconds, e.g. 1597026383085  
> o | String | Open price  
> h | String | highest price  
> l | String | Lowest price  
> c | String | Close price  
> vol | String | Trading volume, in szCcy  
> confirm | String | The state of candlesticks.0 represents that it is uncompleted, 1 represents that it is completed.  
The data returned will be arranged in an array like this: [ts,o,h,l,c,vol,confirm]

---

# 价差交易

👉 Spread Orderbook 产品使用户能够灵活交易大尺寸价差（Spread），可以用于简化交割合約展期、资金费套利和提高收益率，以及基于基差和期限结构的投机。   
  
## 介绍 

### 基本概念 

  1. 价差（**Spread） -** 做多一种产品并同时做空数量等价的另一种相关产品，形成具有两条风险互相抵消的腿的交易
  2. 订单簿（**Order-book） -** 一种或一组交易产品的报价集合。每个报价都包含一个或一组定义的产品、相关数量以及 _Maker_(报价者)愿意交易的价格。然后， _Taker_(接受者)可以立即消耗这些报价，直至订单簿上列出的全部数量。价差交易挂单限额为所有价差挂单合计不超过500个。

### 基本工作流程 

Nitro Spreads 以熟悉的**中央限价订单簿 (CLOB)** 概念为中心：

  * Spreads里包含的产品来自OKX交易所，交易之后也在OKX交易所进行清算和结算。
  * 任何人都可以充当“Taker”，消耗现有的剩余订单，或“Maker”，其订单被消耗。
  * 交易在订单被匹配时发生，之后它们被发送到 OKX 进行清算和结算。

简单来说，Nitro Spreads 工作流程是

  1. _Maker 在 Spread 的订单簿上设置限价订单。_
  2. _Taker通过限价单消耗一个resting Order。_
  3. 被匹配的订单被发送去清算和结算。
  4. Taker和Maker收到交易成功或拒绝的确认
  5. 所有用户都会收到成功结算和清算交易的通知，除去涉及的交易双方以交易方向 (买入或卖出) 等信息。

Nitro Spreads 的主要方面：

  * 所有价差都有**可公开访问** 的中央限价订单簿 (**CLOB**)。
  * Spreads的可用性由OKX决定。通常，这些Spreads包括同一标的下（如“BTC/USDT”或“ETH/USDC”）中 delta one 衍生品（交割和永续）和现货的所有可能组合。
  * **部分成交** 和多个订单可以作为单笔交易的一部分。
  * 交易对手方**不是** 任由用户选择的。任何人都可以参与所有Spread的订单簿，有效地与更广泛的市场进行交易。
  * 整个过程保持匿名，所有订单和交易均在**匿名** 的基础上进行。
  * 用户可以灵活地在订单簿的买卖双方下多个订单，从而实现阶梯式配置。

## 全面的 API 工作流程 

有关订单和交易的通知将由 *Taker* 和 *Maker* 通过 WebSocket 通知渠道接收。 

当用户的订单被另一个订单执行时，用户将承担 _Maker_ 的角色。当用户提交的订单与订单簿中的现有订单相匹配时，他们就会成为 _Taker_

### 获取可用Spreads 

要检索在 OKX 上交易的所有可用Spreads，您应该向 `GET /api/v5/sprd/spreads` 发出请求

### 检索您的订单

要在 OKX 上检索您的订单，您应该向 `GET /api/v5/sprd/order` 发出请求。

### 检索您的交易

要检索您在 OKX 上的交易，您应该向 `GET /api/v5/sprd/trades` 发出请求。

### 提交订单 

要向 某个Spread 的订单簿提交订单，您应该请求 `POST /api/v5/sprd/order` 。

### Spread状态 

Spread 的生命周期中存在三种不同的状态：`live`，`suspend`，和 `expired`:

  1. `live`: 在 Nitro Spread 上活跃交易的Spreads
  2. `suspend`：其中至少一条腿被暂停，另一条在 OKX 订单簿交易所处于活跃或暂停状态的价差；或标的工具仍在 OKX 订单簿交易所中存在但已从 Nitro Spread 中移除的Spread
  3. `expired`：至少一条腿在 OKX 订单簿交易所到期的Spread

给定每条腿的状态以及 Nitro Spreads 上的Spread状态（除了在 Nitro Spread上退市的情况），所有可能Spread状态的情况请参考下表：

交易产品A | 交易产品B | Spread状态  
---|---|---  
Live | Live | Live  
Suspend | Live | Suspend  
Live | Suspend | Suspend  
Suspend | Suspend | Suspend  
Expired | Live | Expired  
Live | Expired | Expired  
Suspend | Expired | Expired  
Expired | Suspend | Expired  
Expired | Expired | Expired  
  
### 交易生命周期 

为了进行交易，需要在价差撮合交易中匹配两个订单。 通过订阅 `sprd-orders`WebSocket 通道，您可以获得有关订单状态的信息并确定它是否已达到最终状态。通道中的`state`值表示订单的当前状态。

  1. 如果状态为`live` 或 `partially_filled`，则意味着订单仍有未达最终状态（`filled`或`canceled`）数量，创建者或其他用户仍可能可以对其执行操作。
  2. 另一方面，如果状态为`canceled`或`filled`，创建者或任何其他用户将无法对此订单执行任何操作。

请密切跟踪以下属性：`sz`（数量）、`pendingFillSz`（待完成数量）、`canceledSz`（被取消数量）和 `accFillSz`（累积完成数量）。这些属性提供了有关订单状态和进展的重要信息。

### 用户的订单状态 

通过订阅 `sprd-orders`WebSocket 频道，用户可以跟踪他们的订单状态。

  1. 提交订单后，无论是 _Maker_ 还是 _Taker_ ，用户都会通过订单 WebSocket 频道道收到订单更新消息。该消息将指示订单的`state` == `live`。
  2. 订单成交和结算是异步的。当订单已成交但还没结算，用户将收到`pendingSettleSz`>0，`fillSz` == ""的订单更新消息
  3. 如果订单已部分成交且仍有待处理数量，用户将收到`state` == `partially_filled` 的订单更新消息
  4. 如果订单完全成交，用户将收到`state` == `filled`的订单更新消息
  5. 如果订单未完全消耗，但已达到最终状态，用户将收到`state` == `canceled`的订单更新消息。
  6. 如果订单的某个部分被拒绝，用户会收到更新的订单更新，其中包含更新的 `canceledSz` 和 `pendingFillSz`，以及与错误对应的`code`和`msg`。

### 用户的交易状态 

通过订阅 `sprd-trades`WebSocket 频道，用户可以跟踪他们的交易状态。 1\. 一笔已执行的交易在OKX上进行清算结算后，即为最终交易。 2\. 对于成功清算的交易，用户会收到一条 WebSocket 消息，其中的`state`表示`filled`。 3\. 在交易清算不成功的情况下，用户会收到一条交易更新消息，`state`反映为`rejected`。 4\. 如果交易`state`为`rejected`，交易更新消息还将包含错误代码`code`和解释拒绝原因的相应错误消息 `msg`。

### 所有交易 

所有用户都能够接收通过 OKX Nitro Spread 产品发生的所有交易的更新。 请务必注意，OKX Nitro Spreads 不会披露有关交易双方及交易方向（买入或卖出）的信息。

  1. 用户可以订阅`sprd-public-trades`频道来获取所有已成功结算的交易。

## REST API 

### 下单 

下单

#### 限速:：20次/ 2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/sprd/order`

> 请求示例
    
    
    # 下价差订单
    POST /api/v5/sprd/order
    body
    {
      "sprdId":"BTC-USDT_BTC-USDT-SWAP",
      "clOrdId":"b15",
      "side":"buy",
      "ordType":"limit",
      "px":"2.15",
      "sz":"2"
    }
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 下单
    result = spreadAPI.place_order(sprdId='BTC-USDT_BTC-USDT-SWAP',
                                   clOrdId='b16',side='buy',ordType='limit',
                                   px='2',sz='2')
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 是 | spread ID，如 BTC-USDT_BTC-USDT-SWAP  
clOrdId | String | 否 | 客户自定义订单ID字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
tag | String | 否 | 订单标签字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间。  
side | String | 是 | 订单方向  
`buy`：买，`sell`：卖  
ordType | String | 是 | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
sz | String | 是 | 委托数量。反向价差的数量单位为USD，正向及混合价差为其对应`baseCcy`  
px | String | 是 | 委托价格，仅适用于`limit`, `post_only`, `ioc`类型的订单  
  
> 返回示例
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "clOrdId": "b15",
          "ordId": "312269865356374016",
          "tag": "",
          "sCode": "0",
          "sMsg": ""
        }
      ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败或成功时的msg  
clOrdId   
clOrdId是用户自定义的唯一ID用来识别订单。如果在请求参数中传入了，那它一定会在返回参数内，并且可以用于查询订单，撤销订单，修改订单等接口。 clOrdId不能与当前所有的挂单的clOrdId重复  ordType  
订单类型，创建新订单时必须指定，您指定的订单类型将影响需要哪些订单参数和撮合系统如何执行您的订单，以下是有效的ordType：  
limit：限价单，要求指定sz 和 px   
post_only：限价委托，在下单那一刻只做maker，如果该笔订单的任何部分会吃掉当前挂单深度，则该订单将被全部撤销。   
ioc：立即成交并取消剩余  sz   
反向价差(inverse spread)的数量单位是USD，与OKX订单簿相反. 

### 撤单 

撤销之前下的未完成订单。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/sprd/cancel-order`

> 请求示例
    
    
    POST /api/v5/sprd/cancel-order
    body
    {
        "ordId":"2510789768709120"
    }
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 撤单
    result = spreadAPI.cancel_order(ordId='1905309079888199680')
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 可选 | 订单ID， `ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义ID  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "clOrdId": "oktswap6",
                "ordId": "12345689",
                "sCode": "0",
                "sMsg": ""
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败时的msg  
撤单返回sCode等于0不能严格认为该订单已经被撤销，只表示您的撤单请求被系统服务器所接受，撤单结果以订单频道推送的状态或者查询订单状态为准 

### 全部撤单 

撤销所有挂单

#### 限速：10次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/sprd/mass-cancel`

> 请求示例
    
    
    POST /api/v5/sprd/mass-cancel
     body
     {
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
    }
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 全部撤单
    result = spreadAPI.cancel_all_orders(sprdId="BTC-USDT_BTC-USDT-SWAP")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 否 | spread ID  
  
#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
result | Boolean | 请求结果`true`, `false`  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "result": true
            }
        ]
    }
    
    

返回结果中result=true 代表您的请求已被成功接收，并将会被处理。撤单的实际结果会通过`sprd-orders`频道推送。 

### 修改订单 

修改当前未成交的挂单  

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/sprd/amend-order`

> 请求示例
    
    
    POST /api/v5/sprd/amend-order
    body
    {
        "ordId":"2510789768709120",
        "newSz":"2"
    }
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 可选 | 订单ID， `ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义order ID  
reqId | String | 否 | 用户自定义修改事件ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
newSz | String | 可选 | 修改的新数量，对于部分成交订单，该数量应包含已成交数量。   
`newSz` 和 `newPx`不可同时为空。  
newPx | String | 可选 | 修改后的新价格。  
`newSz` 和 `newPx`不可同时为空。  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
             "clOrdId":"",
             "ordId":"12344",
             "reqId":"b12344",
             "sCode":"0",
             "sMsg":""
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
clOrdId | String | 用户自定义order ID  
reqId | String | 用户自定义修改事件ID  
sCode | String | 事件执行结果的code，0代表成功  
sMsg | String | 事件执行失败或成功时的msg  
newSz  
若修改订单时，订单修改后的新数量小于或等于 (accFillSz + canceledSz + pendingSettleSz)，在 pendingSettleSz 结算后，订单状态会根据 canceledSz 的不同而不同。当 canceledSz = 0，订单状态将被改为 filled；当 canceledSz > 0，订单状态将被改为 canceled。  修改订单返回sCode等于0不能严格认为该订单已经被修改，只表示您的修改订单请求被系统服务器所接受，改单结果以订单频道推送的状态或者查询订单状态为准 

### 获取订单信息 

查订单信息

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/order`

> 请求示例
    
    
    GET /api/v5/sprd/order?ordId=2510789768709120
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取订单详情
    result = spreadAPI.get_order_details(ordId='1905309079888199680')
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 可选 | 订单ID，`ordId`和`clOrdId`必须传一个，若传两个，以`ordId`为主  
clOrdId | String | 可选 | 用户自定义ID，如果`clOrdId`关联了多个订单，只会返回最近的那笔订单  
  
> 返回示例
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "sprdId": "BTC-USD-SWAP_BTC-USD-200329",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | Spread ID  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格  
sz | String | 委托数量  
ordType | String | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
side | String | 订单方向  
fillSz | String | 最新成交数量  
fillPx | String | 最新成交价格  
tradeId | String | 最近成交ID  
accFillSz | String | 累计成交数量  
pendingFillSz | String | 待成交数量（包括待结算数量）  
pendingSettleSz | String | 待结算数量  
canceledSz | String | 被取消数量  
avgPx | String | 成交均价，如果成交数量为0，该字段为"0"  
state | String | 订单状态  
`canceled`：撤单成功  
`live`：等待成交  
`partially_filled`：部分成交  
`filled`：完全成交  
cancelSource | String | 撤单原因  
`0`: 系统撤单  
`1`: 用户撤单   
`14`: 已撤单：IOC 委托订单未完全成交，仅部分成交，导致部分挂单被撤回  
`15`: 已撤单：该订单委托价不在限价范围内  
`20`: 系统倒计时撤单   
`31`: 当前只挂单订单 (Post only) 将会吃掉挂单深度  
`32`: 自成交保护  
`34`: 订单结算失败因为保证金不足   
`35`: 撤单因为其他订单保证金不足  
`44`：由于该币种的可用余额不足，无法在触发自动换币后进行兑换，您的订单已撤销，撤销订单后恢复的余额将用于自动换币。当该币种的总抵押借贷量达到平台抵押借贷风控上限时，则会触发自动换币。  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式， 如 `1597026383085`  
订单数量等式: pendingFillSz + canceledSz + accFillSz = sz 

### 获取未成交订单列表 

获取当前账户下所有未成交订单信息

#### 限速：10次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/orders-pending`

> 请求示例
    
    
    GET /api/v5/sprd/orders-pending
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取未完成订单
    result = spreadAPI.get_active_orders()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 否 | spread ID，如BTC-USDT_BTC-USDT-SWAP  
ordType | String | 否 | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
state | String | 否 | 订单状态  
`live`：等待成交  
`partially_filled`：部分成交  
beginId | String | 否 | 请求的起始订单ID，请求此ID之后（更新的数据）的分页内容，不包括 beginId  
endId | String | 否 | 请求的结束订单ID，请求此ID之前（更旧的数据）的分页内容，不包括 endId  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回示例
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID，如BTC-USDT_BTC-USDT-SWAP  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格  
sz | String | 委托数量  
ordType | String | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
side | String | 订单方向  
fillSz | String | 最新成交数量  
fillPx | String | 最新成交价格  
tradeId | String | 最近成交ID  
accFillSz | String | 累计成交数量  
pendingFillSz | String | 待成交数量（包括待结算数量）  
pendingSettleSz | String | 待结算数量  
canceledSz | String | 被取消数量  
avgPx | String | 成交均价，如果成交数量为0，该字段为"0"  
state | String | 订单状态  
`live`：等待成交  
`partially_filled`：部分成交  
cancelSource | String | 撤单原因  
`0`: 系统撤单  
`1`: 用户撤单   
`14`: 已撤单：IOC 委托订单未完全成交，仅部分成交，导致部分挂单被撤回  
`15`: 已撤单：该订单委托价不在限价范围内  
`20`: 系统倒计时撤单   
`31`: 当前只挂单订单 (Post only) 将会吃掉挂单深度  
`32`: 自成交保护   
`34`: 订单结算失败因为保证金不足   
`35`: 撤单因为其他订单保证金不足  
`44`：由于该币种的可用余额不足，无法在触发自动换币后进行兑换，您的订单已撤销，撤销订单后恢复的余额将用于自动换币。当该币种的总抵押借贷量达到平台抵押借贷风控上限时，则会触发自动换币。  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如：`1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如：`1597026383085`  
  
### 获取历史订单记录（近21天) 

获取最近21天挂单，且完全成交的订单数据，包括21天以前挂单，但近21天才成交的订单数据。按照订单创建时间倒序排序。

已经撤销的未成交单 只保留2小时。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/orders-history`

> 请求示例
    
    
    GET /api/v5/sprd/orders-history
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取历史订单
    result = spreadAPI.get_orders()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 否 | spread ID，如BTC-USDT_BTC-USDT-SWAP  
ordType | String | 否 | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
state | String | 否 | 订单状态  
`canceled`：撤单成功  
`filled`：完全成交  
beginId | String | 否 | 请求的起始订单ID，请求此ID之后（更新的数据）的分页内容，不包括 beginId  
endId | String | 否 | 请求的结束订单ID，请求此ID之前（更旧的数据）的分页内容，不包括 endId  
begin | String | 否 | 筛选的开始时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 筛选的结束时间戳，Unix 时间戳为毫秒数格式，如 `1597027383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回示例
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
         {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID，如BTC-USDT_BTC-USDT-SWAP  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格  
sz | String | 委托数量  
ordType | String | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
side | String | 订单方向  
fillSz | String | 最新成交数量  
fillPx | String | 最新成交价格  
tradeId | String | 最近成交ID  
accFillSz | String | 累计成交数量  
pendingFillSz | String | 待成交数量（包括待结算数量）  
pendingSettleSz | String | 待结算数量  
canceledSz | String | 被取消数量  
avgPx | String | 成交均价，如果成交数量为0，该字段为"0"  
state | String | 订单状态  
`canceled`：撤单成功  
`filled`：完全成交  
cancelSource | String | 撤单原因  
`0`: 系统撤单  
`1`: 用户撤单   
`14`: 已撤单：IOC 委托订单未完全成交，仅部分成交，导致部分挂单被撤回  
`15`: 已撤单：该订单委托价不在限价范围内  
`20`: 系统倒计时撤单   
`31`: 当前只挂单订单 (Post only) 将会吃掉挂单深度  
`32`: 自成交保护  
`34`: 订单结算失败因为保证金不足   
`35`: 撤单因为其他订单保证金不足  
`44`：由于该币种的可用余额不足，无法在触发自动换币后进行兑换，您的订单已撤销，撤销订单后恢复的余额将用于自动换币。当该币种的总抵押借贷量达到平台抵押借贷风控上限时，则会触发自动换币。  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如：`1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式， 如 ： `1597026383085`  
  
### 获取历史订单记录（近三月) 

获取最近三个月挂单，且完全成交的订单数据，包括三个月以前挂单，但近三个月才成交的订单数据。按照订单创建时间倒序排序。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/orders-history-archive`

> 请求示例
    
    
    GET /api/v5/sprd/orders-history-archive
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 否 | spread ID，如BTC-USDT_BTC-USDT-SWAP  
ordType | String | 否 | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
state | String | 否 | 订单状态  
`canceled`：撤单成功  
`filled`：完全成交  
instType | String | 否 | 产品类型  
`SPOT`：币币  
`FUTURES`:交割合约  
`SWAP`：永续合约   
订单任意一条腿的spread包含相应产品类型，则返回  
instFamily | String | 否 | 交易品种，如 `BTC-USDT`   
订单任意一条腿的spread包含相应交易品种，则返回  
beginId | String | 否 | 请求的起始订单ID，请求此ID之后（更新的数据）的分页内容，不包括 beginId  
endId | String | 否 | 请求的结束订单ID，请求此ID之前（更旧的数据）的分页内容，不包括 endId  
begin | String | 否 | 筛选的开始时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 筛选的结束时间戳，Unix 时间戳为毫秒数格式，如 `1597027383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回示例
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
         {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "cancelled",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085"
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID，如BTC-USDT_BTC-USDT-SWAP  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
px | String | 委托价格  
sz | String | 委托数量  
ordType | String | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
side | String | 订单方向  
fillSz | String | 最新成交数量  
fillPx | String | 最新成交价格  
tradeId | String | 最近成交ID  
accFillSz | String | 累计成交数量  
pendingFillSz | String | 待成交数量（包括待结算数量）  
pendingSettleSz | String | 待结算数量  
canceledSz | String | 被取消数量  
avgPx | String | 成交均价，如果成交数量为0，该字段为"0"  
state | String | 订单状态  
`canceled`：撤单成功  
`filled`：完全成交  
cancelSource | String | 撤单原因  
`0`: 系统撤单  
`1`: 用户撤单   
`14`: 已撤单：IOC 委托订单未完全成交，仅部分成交，导致部分挂单被撤回  
`15`: 已撤单：该订单委托价不在限价范围内  
`20`: 系统倒计时撤单   
`31`: 当前只挂单订单 (Post only) 将会吃掉挂单深度  
`32`: 自成交保护  
`34`: 订单结算失败因为保证金不足   
`35`: 撤单因为其他订单保证金不足  
uTime | String | 订单状态更新时间，Unix时间戳的毫秒数格式，如：`1597026383085`  
cTime | String | 订单创建时间，Unix时间戳的毫秒数格式， 如 ： `1597026383085`  
  
### 获取历史成交数据（近七天）

获取近7天的订单成交明细信息. 结果按时间倒序返回。

#### 限速：20次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/trades`

> 请求示例
    
    
    GET /api/v5/sprd/trades
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取私有交易
    result = spreadAPI.get_trades()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 否 | spread ID，如BTC-USDT_BTC-USDT-SWAP  
tradeId | String | 否 | 交易 ID  
ordId | String | 否 | 订单 ID  
beginId | String | 否 | 请求的起始交易ID，请求此ID之后（更新的数据）的分页内容，不包括 beginId  
endId | String | 否 | 请求的结束交易ID，请求此ID之前（更旧的数据）的分页内容，不包括 endId  
begin | String | 否 | 筛选的开始时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
end | String | 否 | 筛选的结束时间戳，Unix 时间戳为毫秒数格式，如 `1597027383085`  
limit | String | 否 | 返回结果的数量，最大为100，默认100条  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT-SWAP_BTC-USDT-200329",
                "tradeId": "123",
                "ordId": "123445",
                "clOrdId": "b16",
                "tag": "",
                "fillPx": "999",
                "fillSz": "3",
                "state": "filled",
                "side": "buy",
                "execType": "M",
                "ts": "1597026383085",
                "legs": [
                    {
                        "instId": "BTC-USDT-SWAP",
                        "px": "20000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "buy",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "1232342342"
                    },
                    {
                        "instId": "BTC-USDT-200329",
                        "px": "21000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "sell",
                        "fillpnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "5345646634"
                    }
                ],
                "code": "",
                "msg": ""
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID，如BTC-USDT_BTC-USDT-SWAP  
tradeId | String | 交易ID  
ordId | String | 订单ID  
clOrdId | String | 客户自定义订单ID  
tag | String | 订单标签  
fillPx | String | 成交价格  
fillSz | String | 成交数量  
side | String | 交易方向   
`buy`：买   
`sell`：卖  
state | String | 交易状态   
`filled`：已成交   
`rejected`：被拒绝  
execType | String | 流动性方向 `T`：taker `M`：maker  
ts | String | 成交明细产生时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
legs | Array of objects | 交易的腿  
> instId | String | 产品 ID  
> px | String | 价格  
> sz | String | 数量  
> szCont | String | 成交合约数量   
仅适用于合约，现货将返回""  
> side | String | 交易方向 `buy`：买 `sell`：卖  
> fillPnl | String | 最新成交收益，适用于有成交的平仓订单。其他情况均为0。  
> fee | String | 手续费金额或者返佣金额，手续费扣除为‘负数’，如-0.01；手续费返佣为‘正数’，如 0.01  
> feeCcy | String | 交易手续费币种或者返佣金币种  
> tradeId | String | 交易ID  
code | String | 错误码，默认0  
msg | String | 错误提示，默认 ""  
  
### 获取Spreads（公共） 

获取可交易的Spreads。

#### 限速：20次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/spreads`

> 请求示例
    
    
    GET /api/v5/sprd/spreads?instId=BTC-USDT
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取价差产品
    result = spreadAPI.get_spreads()
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
baseCcy | string | 否 | Spread 币种，如 `BTC`  
instId | String | 否 | Spread 里包含的产品ID  
sprdId | String | 否 | Spread ID  
state | string | 否 | Spread 状态  
`live`：交易中  
`suspend`：暂停中  
`expired`：订单过期  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "sprdId": "ETH-USD-SWAP_ETH-USD-231229",
                "sprdType": "inverse",
                "state": "live",
                "baseCcy": "ETH",
                "szCcy": "USD",
                "quoteCcy": "USD",
                "tickSz": "0.01",
                "minSz": "10",
                "lotSz": "10",
                "listTime": "1686903000159",
                "legs": [{
                        "instId": "ETH-USD-SWAP",
                        "side": "sell"
                    },
                    {
                        "instId": "ETH-USD-231229",
                        "side": "buy"
                    }
                ],
                "expTime": "1703836800000",
                "uTime": "1691376905595"
            },
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "sprdType": "linear",
                "state": "live",
                "baseCcy": "BTC",
                "szCcy": "BTC",
                "quoteCcy": "USDT",
                "tickSz": "0.0001",
                "minSz": "0.001",
                "lotSz": "1",
                "listTime": "1597026383085",
                "expTime": "1597029999085",
                "uTime": "1597028888085",
                "legs": [{
                        "instId": "BTC-USDT",
                        "side": "sell"
                    },
                    {
                        "instId": "BTC-USDT-SWAP",
                        "side": "buy"
                    }
                ]
            },
            {
                "sprdId": "BTC-USDT_BTC-USDT-230317",
                "sprdType": "linear",
                "state": "live",
                "baseCcy": "BTC",
                "szCcy": "BTC",
                "quoteCcy": "USDT",
                "tickSz": "0.0001",
                "minSz": "0.001",
                "lotSz": "1",
                "listTime": "1597026383085",
                "expTime": "1597029999085",
                "uTime": "1597028888085",
                "legs": [{
                        "instId": "BTC-USDT",
                        "side": "sell"
                    },
                    {
                        "instId": "BTC-USDT-230317",
                        "side": "buy"
                    }
                ]
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID  
sprdType | String | Spread类型，有效值为`linear`, `inverse`, `hybrid`  
state | String | Spread状态  
`live`：交易中  
`suspend`：暂停中  
`expired`：已过期  
baseCcy | String | Spread币种，如 `BTC`  
szCcy | String | Spread数量单位，如 USD, BTC, ETH, USD。  
quoteCcy | String | Spread计价单位。如 USDT，USD。  
tickSz | String | 下单价格精度，如 0.0001。单位为Spread计价单位quoteCcy。  
minSz | String | 最小下单数量。单位为Spread数量单位szCcy。  
lotSz | String | 下单数量精度。单位为Spread数量单位szCcy。  
listTime | String | 上线日期。Unix时间戳的毫秒数格式，如 `1597026383085`  
expTime | String | 失效日期。Unix时间戳的毫秒数格式，如 `1597026383085`  
uTime | String | 上次更新时间。Unix时间戳的毫秒数格式，如 `1597026383085`  
legs | array of objects | 腿  
> instId | String | 产品ID  
> side | String | 产品方向  
`buy`：买入  
`sell`：卖出  
  
### 获取Spread产品深度（公共） 

获取Spread产品深度列表

#### 限速：20次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/books`

> 请求示例
    
    
    GET /api/v5/sprd/books?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取深度
    result = spreadAPI.get_order_book(sprdId="BTC-USDT_BTC-USDT-SWAP", sz=20)
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 是 | spread ID，如BTC-USDT_BTC-USDT-SWAP  
sz | String | 否 | 深度档位数量。最大值为400。默认值为5。  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "asks": [
                    [
                        "41006.8", // 价格
                        "0.60038921", // 数量
                        "1" // 此价格上订单数量
                    ]
                ],
                "bids": [
                    [
                        "41006.3",
                        "0.30178218",
                        "2"
                    ]
                ],
                "ts": "1629966436396"
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
asks | Array of Arrays | 卖方深度  
bids | Array of Arrays | 买方深度  
ts | String | 深度产生的时间  
asks和bids值数组举例说明： ["411.8", "10", "4"]   
\- 411.8为深度价格   
\- 10为此价格的数量 (单位为szCcy）  
\- 4为此价格的订单数量   

### 获取单个Spread产品行情信息（公共） 

获取单个Spread产品行情信息，包括最新成交价，买一卖一价及数量。

#### 限速：20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/sprd-ticker`

> 请求示例
    
    
    GET /api/v5/market/sprd-ticker?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 是 | spread ID, 如 BTC-USDT_BTC-USDT-SWAP  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "last": "14.5",
                "lastSz": "0.5",
                "askPx": "8.5",
                "askSz": "12.0",
                "bidPx": "0.5",
                "bidSz": "12.0",
                "open24h": "4",
                "high24h": "14.5",
                "low24h": "-2.2",
                "vol24h": "6.67",
                "ts": "1715331406485"
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID  
last | String | 最新成交价  
lastSz | String | 最新成交的数量  
askPx | String | 卖一价  
askSz | String | 卖一价对应的数量  
bidPx | String | 买一价  
bidSz | String | 买一价对应的数量  
open24h | String | 24小时开盘价  
high24h | String | 24小时最高价  
low24h | String | 24小时最低价  
vol24h | String | 24小时交易量  
正向及混合价差，单位为交易货币；反向价差，单位为美元  
ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 1597026383085  
  
### 获取公共成交数据（公共） 

查询市场上的Spread成交信息数据，每次请求最多返回500条结果。结果按时间倒序返回。

#### 限速：20次/2s

#### 限速规则：IP

#### 权限：读取

#### HTTP请求

`GET /api/v5/sprd/public-trades`

> 请求示例
    
    
    GET /api/v5/sprd/public-trades?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    
    
    
    import okx.SpreadTrading as SpreadTrading
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "1"  # 实盘:0 , 模拟盘:1
    
    spreadAPI = SpreadTrading.SpreadTradingAPI(apikey, secretkey, passphrase, False, flag)
    
    # 获取公共交易信息
    result = spreadAPI.get_public_trades(sprdId='ETH-USDT-SWAP_ETH-USDT-230929')
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 否 | Spread ID，例如BTC-USDT_BTC-USDT-SWAP  
  
> 返回示例
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDC-SWAP",
                "side": "sell",
                "sz": "0.1",
                "px": "964.1",
                "tradeId": "242720719",
                "ts": "1654161641568"
            }
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
sprdId | String | spread ID  
tradeId | String | 交易ID  
px | String | 成交价格  
sz | String | 成交数量  
side | String | Taker的交易方向 `buy`：买 `sell`：卖  
ts | String | 交易时间，Unix时间戳的毫秒数格式， 如 ： `1597026383085`  
最多可以查询到最近500条公共成交信息。 

### 获取价差交易产品K线数据 

获取K线数据。K线数据按请求的粒度分组返回，K线数据每个粒度最多可获取最近1,440条。

#### 限速: 40次/2s

#### 限速规则： IP

#### HTTP请求

`GET /api/v5/market/sprd-candles`

> 请求示例
    
    
    GET /api/v5/market/sprd-candles?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 是 | Spread ID  
bar | String | 否 | 时间粒度，默认值1m，如 [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8开盘价k线：[6H/12H/1D/2D/3D/1W/1M/3M]   
UTC+0开盘价k线：[/6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的ts  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的ts, 单独使用时，会返回最新的数据。  
limit | String | 否 | 分页返回的结果集数量，最大为300，不填默认返回100条  
  
> 返回示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "0"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "1"
        ]
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 开始时间，Unix时间戳的毫秒数格式，如 1597026383085  
o | String | 开盘价格  
h | String | 最高价格  
l | String | 最低价格  
c | String | 收盘价格  
vol | String | 交易量  
confirm | String | K线状态   
`0`：K线未完结   
`1`：K线已完结  
返回的第一条K线数据可能不是完整周期k线，返回值数组顺序分别为是：[ts,o,h,l,c,vol,confirm]. 

### 获取价差交易产品历史K线数据 

获取最近几年的历史k线数据

#### 限速: 20次/2s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/market/sprd-history-candles`

> 请求示例
    
    
    GET /api/v5/market/sprd-history-candles?sprdId=BTC-USDT_BTC-USDT-SWAP
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
sprdId | String | 是 | Spread ID  
after | String | 否 | 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的ts  
before | String | 否 | 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的ts, 单独使用时，会返回最新的数据。  
bar | String | 否 | 时间粒度，默认值1m，如 [1m/3m/5m/15m/30m/1H/2H/4H]   
UTC+8开盘价k线：[6H/12H/1D/2D/3D/1W/1M/3M]   
UTC+0开盘价k线：[6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
  
> 返回示例
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
         [
            "1597026383085",
            "3.721",
            "3.743",
            "3.677",
            "3.708",
            "8422410",
            "1"
        ],
        [
            "1597026383085",
            "3.731",
            "3.799",
            "3.494",
            "3.72",
            "24912403",
            "1"
        ]
        ]
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ts | String | 开始时间，Unix时间戳的毫秒数格式，如 1597026383085  
o | String | 开盘价格  
h | String | 最高价格  
l | String | 最低价格  
c | String | 收盘价格  
vol | String | 交易量  
confirm | String | K线状态   
`0`：K线未完结   
`1`：K线已完结  
返回值数组顺序分别为是： [ts,o,h,l,c,vol,confirm] 

### 倒计时全部撤单 

在倒计时结束后，取消所有挂单。仅适用于价差交易。

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/sprd/cancel-all-after`

> 请求示例
    
    
    POST /api/v5/sprd/cancel-all-after
    {
       "timeOut":"30"
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
timeOut | String | 是 | 取消挂单的倒计时，单位为秒   
取值范围为 0, [10, 120]  
0 代表不使用该功能  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "triggerTime":"1587971460",
                "ts":"1587971400"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
triggerTime | String | 触发撤单的时间   
triggerTime=0 代表未使用该功能  
ts | String | 请求被接收到的时间  
建议用户每一秒调用接口一次。当倒计时全部撤单被触发时，交易引擎将为用户逐一取消其挂单，该操作可能持续数秒。该功能起到保护用户的作用，不应作为交易策略使用。 

## Websocket交易API

### WS / 下单 

只有当您的账户有足够的资金才能下单。

#### 服务地址

/ws/v5/business (需要登录)

#### 限速：20次/2s

#### 限速规则：User ID

同Nitro Spread`下单` REST API 共享限速 

> 请求示例
    
    
    {
      "id": "1512",
      "op": "sprd-order",
      "args": [
        {
           "sprdId":"BTC-USDT_BTC-USDT-SWAP",
           "clOrdId":"b15",
           "side":"buy",
           "ordType":"limit",
           "px":"2.15",
           "sz":"2"
        }
      ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，`sprd-order`  
args | Array of objects | 是 | 请求参数  
> sprdId | String | 是 | 产品ID，如 `BTC-USDT_BTC-USDT-SWAP`  
> clOrdId | String | 否 | 由用户设置的订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
> tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-16位之间。  
> side | String | 是 | 订单方向，`buy` `sell`  
> ordType | String | 是 | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
> sz | String | 是 | 委托数量  
> px | String | 是 | 委托价，仅适用于`limit`、`post_only`、`ioc`类型的订单  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-order",
        "data": [{
            "clOrdId": "",
            "ordId": "12345689",
            "tag": "",
            "sCode": "0",
            "sMsg": ""
        }],
        "code": "0",
        "msg": ""
    }
    

> 失败返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-order",
        "data": [{
            "clOrdId": "",
            "ordId": "",
            "tag": "",
            "sCode": "5XXXX",
            "sMsg": "not exist"
        }],
        "code": "1",
        "msg": ""
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-order",
        "data": [],
        "code": "60013",
        "msg": "Invalid args"
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> tag | String | 订单标签  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
clOrdId  
clOrdId是用户自定义的唯一ID用来识别订单。如果在请求参数中传入了，那它一定会在返回参数内，并且可以用于查询订单，撤销订单，修改订单等接口。 clOrdId不能与当前所有的挂单的clOrdId重复 

### WS / 改单 

修改当前未成交的订单

#### 服务地址

/ws/v5/business (需要登录)

#### 限速：20次/2s

#### 限速规则：User ID

同Nitro Spread`改单` REST API 共享限速 

> 请求示例
    
    
    {
       "id":"1512",
       "op":"sprd-amend-order",
       "args":[
          {
             "ordId":"2510789768709120",
             "newSz":"2"
          }
       ]
    }
    
    

#### 请求参数

Parameter | Type | Required | Description  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，`sprd-amend-order`  
args | Array of objects | 是 | 请求参数  
> ordId | String | 可选 | 订单ID   
ordId 和 clOrdId必须传一个，若传两个，以 ordId 为主  
> clOrdId | String | 可选 | 由用户设置的订单ID  
> reqId | String | 否 | 用户自定义修改事件ID   
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度要在1-32位之间。  
> newSz | String | 可选 | 修改的新数量，对于部分成交订单，该数量应包含已成交数量。  
`newSz` 或 `newPx`至少传一个。  
> newPx | String | 可选 | 修改后的新价格  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "reqId": "b12344",
          "sCode": "0",
          "sMsg": ""
        }
      ],
      "code": "0",
      "msg": ""
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [
        {
          "clOrdId": "",
          "ordId": "2510789768709120",
          "reqId": "b12344",
          "sCode": "5XXXX",
          "sMsg": "order not exist"
        }
      ],
      "code": "1",
      "msg": ""
    }
    
    

> 格式错误返回示例
    
    
    {
      "id": "1512",
      "op": "sprd-amend-order",
      "data": [],
      "code": "60013",
      "msg": "Invalid args"
    }
    
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> reqId | String | 用户自定义修改事件ID  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
newSz  
若修改订单时，订单修改后的新数量小于或等于 (accFillSz + canceledSz + pendingSettleSz)，在 pendingSettleSz 结算后，订单状态会根据 canceledSz 的不同而不同。当 canceledSz = 0，订单状态将被改为 filled；当 canceledSz > 0，订单状态将被改为 canceled。  修改订单返回sCode等于0不能严格认为该订单已经被修改，只表示您的修改订单请求被系统服务器所接受，改单结果以订单频道推送的状态或者查询订单状态为准 

### WS / 撤单 

撤销当前未完成订单

#### 服务地址

/ws/v5/business (需要登录)

#### 限速：20次/2s

#### 限速规则：User ID

同Nitro Spread`撤单` REST API 共享限速 

> 请求示例
    
    
    {
      "id": "1514",
      "op": "sprd-cancel-order",
      "args": [
        {
          "ordId": "2510789768709120"
        }
      ]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，`sprd-cancel-order`  
args | Array of objects | 是 | 请求参数  
> ordId | String | 可选 | 订单ID  
ordId和clOrdId必须传一个，若传两个，以 ordId 为主  
> clOrdId | String | 可选 | 用户提供的订单ID  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度要在1-32位之间。  
  
> 成功返回示例
    
    
    {
        "id": "1514",
        "op": "sprd-cancel-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "sCode": "0",
            "sMsg": ""
        }],
        "code": "0",
        "msg": ""
    }
    

> 失败返回示例
    
    
    {
        "id": "1514",
        "op": "sprd-cancel-order",
        "data": [{
            "clOrdId": "",
            "ordId": "2510789768709120",
            "sCode": "5XXXX",
            "sMsg": "Order not exist"
        }],
        "code": "1",
        "msg": ""
    }
    

> 格式错误返回示例
    
    
    {
        "id": "1514",
        "op": "sprd-cancel-order",
        "data": [],
        "code": "60013",
        "msg": "Invalid args"
    }
    

#### 返回参数

参数 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> sCode | String | 订单状态码，0 代表成功  
> sMsg | String | 订单状态消息  
撤单返回sCode等于0不能严格认为该订单已经被撤销，只表示您的撤单请求被系统服务器所接受，撤单结果以订单频道推送的状态或者查询订单状态为准  

### WS / 全部撤单 

#### 服务地址

/ws/v5/business (需要登录)

#### 限速：5次/2s

#### 限速规则：User ID

> 请求示例
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "args": [{
            "sprdId":"BTC-USDT_BTC-USDT-SWAP"
        }]
    }
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 是 | 消息的唯一标识   
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 支持的业务操作，`sprd-mass-cancel`  
args | Array of objects | 是 | 请求参数  
> sprdId | String | 否 | 价差ID  
  
> 成功返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "data": [
            {
                "result": true
            }
        ],
        "code": "0",
        "msg": ""
    } 
    

> 格式错误返回示例
    
    
    {
        "id": "1512",
        "op": "sprd-mass-cancel",
        "data": [],
        "code": "60013",
        "msg": "Invalid args"
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
id | String | 消息的唯一标识  
op | String | 业务操作  
code | String | 代码  
msg | String | 消息  
data | Array of objects | 请求成功后返回的数据  
> result | Boolean | 撤单结果  
`true`：全部撤单成功  
`false`：全部撤单失败  
  
## WebSocket私有频道 

  * 实盘地址: `wss://ws.okx.com:8443/ws/v5/business`
  * 模拟盘地址: `wss://wspap.okx.com:8443/ws/v5/business`

### 订单频道 

通过订阅`sprd-orders`频道获取Spread订单信息，首次订阅不推送，只有当下单、撤单等事件触发时，推送数据。

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例：单个
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-orders",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-orders",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> 请求示例：
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-orders",
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-orders",
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`sprd-orders`  
> sprdId | String | 是 | Spread ID  
  
> 成功返回示例：单个
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-orders",
        "sprdId": "BTC-USDT_BTC-UST-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-orders"
      },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-orders\", \"instType\" : \"FUTURES\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> sprdId | String | 否 | Spread ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：单个
    
    
    {
      "arg": {
            "channel": "sprd-orders",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP",
            "uid": "614488474791936"
        },
      "data": [
         {
          "sprdId": "BTC-USDT_BTC-UST-SWAP",
          "ordId": "312269865356374016",
          "clOrdId": "b1",
          "tag": "",
          "px": "999",
          "sz": "3",
          "ordType": "limit",
          "side": "buy",
          "fillSz": "0",
          "fillPx": "",
          "tradeId": "",
          "accFillSz": "0",
          "pendingFillSz": "2",
          "pendingSettleSz": "1",
          "canceledSz": "1",
          "state": "live",
          "avgPx": "0",
          "cancelSource": "",
          "uTime": "1597026383085",
          "cTime": "1597026383085",
          "code": "0",
          "msg": "",
          "reqId": "",
          "amendResult": ""
        }
      ]
    
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> sprdId | String | spread ID  
data | Array of objects | 订阅的数据  
> sprdId | String | spread ID  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID来识别您的订单  
> tag | String | 订单标签  
> px | String | 委托价格  
> sz | String | 原始委托数量，单位szCcy  
> ordType | String | 订单类型  
`market`：市价单   
`limit`：限价单   
`post_only`：只做maker单   
`ioc`：立即成交并取消剩余  
> side | String | 订单方向   
`buy`   
`sell`  
> fillSz | String | 最新成交数量，适用于结算成功的订单更新  
> fillPx | String | 最新成交价格，适用于结算成功的订单更新  
> tradeId | String | 最近成交ID  
> accFillSz | String | 累计成交数量  
> pendingFillSz | String | 待成交数量，包括待结算数量  
> pendingSettleSz | String | 待结算数量  
> canceledSz | String | 撤单数量  
> avgPx | String | 成交均价，如果成交数量为0，该字段为"0"  
> state | String | 订单状态  
`canceled`：撤单成功  
`live`：等待成交  
`partially_filled`：部分成交  
`filled`：完全成交  
> cancelSource | String | 撤单原因  
`0`: 系统撤单  
`1`: 用户撤单   
`14`: 已撤单：IOC 委托订单未完全成交，仅部分成交，导致部分挂单被撤回  
`15`: 已撤单：该订单委托价不在限价范围内  
`20`: 系统倒计时撤单  
`31`: 当前只挂单订单 (Post only) 将会吃掉挂单深度  
`32`: 自成交保护  
`34`: 订单结算失败因为保证金不足   
`35`: 撤单因为其他订单保证金不足  
`44`：由于该币种的可用余额不足，无法在触发自动换币后进行兑换，您的订单已撤销，撤销订单后恢复的余额将用于自动换币。当该币种的总抵押借贷量达到平台抵押借贷风控上限时，则会触发自动换币。  
> uTime | String | 订单更新时间，Unix时间戳的毫秒数格式，如 1597026383085  
> cTime | String | 订单创建时间，Unix时间戳的毫秒数格式，如 1597026383085  
> code | String | 错误码，默认为0  
> msg | String | 错误消息，默认为""  
> reqId | String | 修改订单时使用的request ID，如果没有修改，该字段为""  
> amendResult | String | 修改订单的结果  
`-1`：失败  
`0`：成功  
如果没有修改，该字段为""  
  
### 成交数据频道 

通过订阅 `sprd-trades` 频道接收与用户成交信息相关的更新。

已成交（`filled`）和被拒绝（`rejected`）的交易都会通过此频道推送更新。

如果你的订单与多个订单相匹配，你有可能会收到多条更新推送。

#### 服务地址

/ws/v5/business (需要登录)

> 请求示例：单个
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-trades",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

> 请求示例：
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-trades"
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPrivateAsync import WsPrivateAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPrivateAsync(
            apiKey = "YOUR_API_KEY",
            passphrase = "YOUR_PASSPHRASE",
            secretKey = "YOUR_SECRET_KEY",
            url = "wss://ws.okx.com:8443/ws/v5/business",
            useServerTime=False
        )
        await ws.start()
        args = [
            {
              "channel": "sprd-trades"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    
    asyncio.run(main())
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`sprd-trades`  
> sprdId | String | 否 | Spread ID  
  
#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> sprdId | String | 否 | Spread ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "sprd-trades",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP",
            "uid": "614488474791936"
        },
        "data":[
             {
                "sprdId":"BTC-USDT-SWAP_BTC-USDT-200329",
                "tradeId":"123",
                "ordId":"123445",
                "clOrdId": "b16",
                "tag":"",
                "fillPx":"999",
                "fillSz":"3",
                "state": "filled",
                "side":"buy",
                "execType":"M",
                "ts":"1597026383085",
                "legs": [
                    {
                        "instId": "BTC-USDT-SWAP",
                        "px": "20000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "buy",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "1232342342"
                    },
                    {
                        "instId": "BTC-USDT-200329",
                        "px": "21000",
                        "sz": "3",
                        "szCont": "0.03",
                        "side": "sell",
                        "fillPnl": "",
                        "fee": "",
                        "feeCcy": "",
                        "tradeId": "5345646634"
                    },
                ]
                "code": "",
                "msg": ""
            }
        ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> uid | String | 用户标识  
> sprdId | String | spread ID  
data | Array of objects | Subscribed data  
> sprdId | String | spread ID  
> tradeId | String | 交易ID  
> ordId | String | 订单ID  
> clOrdId | String | 由用户设置的订单ID  
> tag | String | 订单标签  
> fillPx | String | 最新成交价  
> fillSz | String | 最新成交数量  
> side | String | 交易方向   
`buy`   
`sell`  
> state | String | 交易状态。   
`filled`: 已成交   
`rejected`: 被拒绝  
> execType | String | 流动性方向   
`T`：taker   
`M`：maker  
>ts | String | 成交明细产生时间，Unix时间戳的毫秒数格式，如1597026383085  
> legs | Array of objects | 交易的腿  
>> instId | String | 产品 ID  
>> px | String | 价格  
>> sz | String | 数量  
>> szCont | String | 成交合约数量   
仅适用于合约，现货将返回""  
>> side | String | 交易方向   
`buy`：买   
`sell`：卖  
>> fillPnl | String | 最新成交收益，适用于有成交的平仓订单。其他情况均为0。  
>> fee | String | 手续费金额或者返佣金额，手续费扣除为‘负数’，如-0.01；手续费返佣为‘正数’，如 0.01  
>> feeCcy | String | 交易手续费币种或者返佣金币种  
>> tradeId | String | 交易ID  
> code | String | 错误码，默认0  
> msg | String | 错误提示，默认 ""  
  
## WebSocket公共频道 

  * 实盘地址: `wss://ws.okx.com:8443/ws/v5/business`
  * 模拟盘地址: `wss://wspap.okx.com:8443/ws/v5/business`

### 深度频道 

获取Spread深度数据。可用频道有：

  * `sprd-bbo-tbt`: 首次推1档快照数据，以后定量推送，每10毫秒当1档快照数据有变化推送一次1档数据
  * `sprd-books5`: 首次推5档快照数据，以后定量推送，每100毫秒当5档快照数据有变化推送一次5档数据
  * `sprd-books-l2-tbt`: 首次推400档快照数据，以后增量推送，每10毫秒推送一次变化的数据
  * 单个连接、交易产品维度，深度频道的推送顺序固定为：sprd-bbo-tbt -> sprd-books-l2-tbt -> sprd-books5

#### URL Path

/ws/v5/business

> 请求示例：sprd-books5
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-books5",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-books5",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

> 请求示例：sprd-books-l2-tbt
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-books-l2-tbt",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-books-l2-tbt",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
`sprd-bbo-tbt`  
`sprd-books5`  
`sprd-books-l2-tbt`  
> channel | String | 是 | 频道名  
> sprdId | String | 是 | spread ID  
  
> 返回示例：sprd-books5
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-books5",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 返回示例：sprd-books-l2-tbt
    
    
    {
      "id": "1512",
       "event":"subscribe",
       "arg":{
          "channel":"sprd-books-l2-tbt",
          "sprdId":"BTC-USDT_BTC-USDT-SWAP"
       },
       "connId":"214fdd24"
    }
    

> 失败示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"args\":[{ \"channel\" : \"sprd-books5\", \"sprdId\" : \"BTC-USD_BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
`sprd-bbo-tbt`  
`sprd-books5`  
`sprd-books-l2-tbt`  
> channel | String | 是 | 频道名  
> sprdId | String | 是 | spread ID  
msg | String | 否 | 错误消息  
code | String | 否 | 错误码  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例：sprd-books5
    
    
    {
      "arg": {
        "channel": "sprd-books5",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "data": [
        {
          "asks": [
            ["111.06","55154","2"],
            ["111.07","53276","2"],
            ["111.08","72435","2"],
            ["111.09","70312","2"],
            ["111.1","67272","2"]],
          "bids": [
            ["111.05","57745","2"],
            ["111.04","57109","2"],
            ["111.03","69563","2"],
            ["111.02","71248","2"],
            ["111.01","65090","2"]],
          "ts": "1670324386802",
          "seqId":1724294007352168320
        }
      ]
    }
    
    

> 推送示例：sprd-books-l2-tbt
    
    
    {
       "arg":{
          "channel":"sprd-books-l2-tbt",
          "sprdId":"BTC-USDT_BTC-USDT-SWAP"
       },
       "action":"snapshot",
       "data":[
          {
             "asks":[
                ["1.9","1.1","3"],
                ["2.5","0.9","1"],
                ["3.2","4.921","1"],
                ["4.8","0.165","1"],
                ["5.2","4.921","1"]
              ......
             ],
             "bids":[
                ["1.8","0.165","1"],
                ["0.6","0.2","2"],
                ["0","23.49","1"],
                ["-0.1","1","1"],
                ["-0.6","1","1"],
                ["-3.9","4.921","1"]
                ......
             ],
             "ts":"1724391380926",
             "checksum":-1285595583,
             "prevSeqId":-1,
             "seqId":1724294007352168320
          }
       ]
    }
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> sprdId | String | Spread ID  
action | String | 推送数据动作，增量推送数据还是全量推送数据  
`snapshot`：全量  
`update`：增量  
data | Array of objects | 订阅的数据  
> asks | Array of strings | 卖方深度  
> bids | Array of strings | 买方深度  
> ts | String | 数据更新时间戳，Unix时间戳的毫秒数格式，如 1597026383085  
> checksum | Integer | 检验和 （下方注解）。仅适用 `sprd-books-l2-tbt`  
> prevSeqId | Integer | 上一个推送的序列号。仅适用 `sprd-books-l2-tbt`  
> seqId | Integer | 推送的序列号 （下方注解）  
asks和bids值数组举例说明： ["411.8", "10", "4"]   
\- 411.8为深度价格   
\- 10为此价格的数量 （单位为szCcy)   
\- 4为此价格的订单数量   

#### 序列号

`seqId`是交易所行情的一个序号。如果用户通过多个websocket连接同一频道，收到的序列号会是相同的。每个`sprdId`对应一套。用户可以使用在增量推送频道的`prevSeqId`和`seqId`来构建消息序列。这将允许用户检测数据包丢失和消息的排序。正常场景下`seqId`的值大于`prevSeqId`。新消息中的`prevSeqId`与上一条消息的`seqId`匹配。最小序列号值为0，除了快照消息的`prevSeqId`为-1。  

异常情况：  
1\. 如果一段时间内没有深度更新，OKX将发一条消息`'asks': [], 'bids': []`以通知用户连接是正常的。推送的`seqId`跟上一条信息的一样，`prevSeqId`等于`seqId`。 2\. 序列号可能由于维护而重置，在这种情况下，用户将收到一条`seqId`小于`prevSeqId`的增量消息。随后的消息将遵循常规的排序规则。

##### 示例

  1. 快照推送：`prevSeqId = -1`，`seqId = 10`
  2. 增量推送1（正常更新）：`prevSeqId = 10`，`seqId = 15`
  3. 增量推送2（无更新）：`prevSeqId = 15`，`seqId = 15`
  4. 增量推送3（序列重置）：`prevSeqId = 15`，`seqId = 3`
  5. 增量推送4（正常更新）：`prevSeqId = 3`，`seqId = 5`

#### Checksum机制

此机制可以帮助用户校验深度数据的准确性。

##### 深度合并

用户订阅增量推送深度频道成功后，首先获取初始全量深度数据，当获取到增量推送数据后，更新本地全量深度数据。 

  1. 如果有相同价格，则比较数量；数量为0删除此深度，数量有变化则替换此数据。
  2. 如果没有相同价格，则按照价格优劣排序（bid为价格降序，ask为价格升序），将深度信息插入到全量数据中

##### 计算校验和

先用深度合并后前25档bids和asks组成一个字符串（其中ask和bid中的价格和数量以冒号连接），再计算其crc32值（32位有符号整型）。 

### 公共成交数据频道 

订阅`sprd-public-trades`获取最近的成交数据，有成交数据就推送，每次推送仅包含一条成交数据。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-public-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-public-trades",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`sprd-public-trades`  
> sprdId | String | 是 | Spread ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
          "channel": "sprd-public-trades",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-public-trades\", \"instId\" : \"BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> sprdId | String | 是 | Spread ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "sprd-public-trades",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "tradeId": "2499206329160695808",
                "px": "-10",
                "sz": "0.001",
                "side": "sell",
                "ts": "1726801105519"
            }
        ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> sprdId | String | spread ID  
data | Array of objects | 订阅的数据  
> sprdId | String | spread ID  
> tradeId | String | 交易 ID  
> px | String | 成交价格  
sz | String | 成交数量  
对于币币交易，成交数量的单位为交易货币  
对于交割、永续以及期权，单位为张。  
> side | String | 成交方向   
`buy`   
`sell`  
> ts | String | 成交时间，Unix时间戳的毫秒数格式，如 1597026383085  
  
### 行情频道 

订阅`sprd-tickers`获取产品的最新成交价、买一价、卖一价及数量等信息。 最快100ms推送一次，没有触发事件时最慢1s推送一次，触发推送的事件有：成交、买一卖一发生变动。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
      "id": "1512",
      "op": "subscribe",
      "args": [
        {
          "channel": "sprd-tickers",
          "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        }
      ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
            {
              "channel": "sprd-tickers",
              "sprdId": "BTC-USDT_BTC-USDT-SWAP"
            }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`  
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`sprd-tickers`  
> sprdId | String | 是 | spread ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-tickers",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-tickers\", \"instId\" : \"LTC-USD-200327\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件  
`subscribe`  
`unsubscribe`  
`error`  
arg | Object | 否 | 订阅的频道  
> channel | String | 是 | 频道名  
> sprdId | String | 是 | Spread ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
connId | String | 是 | WebSocket连接ID  
  
> 推送示例
    
    
    {
        "arg": {
            "channel": "sprd-tickers",
            "sprdId": "BTC-USDT_BTC-USDT-SWAP"
        },
        "data": [
            {
                "sprdId": "BTC-USDT_BTC-USDT-SWAP",
                "last": "4",
                "lastSz": "0.01",
                "askPx": "19.7",
                "askSz": "5.79",
                "bidPx": "5.9",
                "bidSz": "5.79",
                "open24h": "-7",
                "high24h": "19.6",
                "low24h": "-7",
                "vol24h": "9.87",
                "ts": "1715247061026"
            }
        ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> sprdId | String | spread ID  
data | Array of objects | 订阅的数据  
> sprdId | String | spread ID  
> last | String | 最新成交价  
> lastSz | String | 最新成交的数量  
> askPx | String | 卖一价  
> askSz | String | 卖一价对应的量  
> bidPx | String | 买一价  
> bidSz | String | 买一价对应的数量  
> open24h | String | 24小时开盘价  
> high24h | String | 24小时最高价  
> low24h | String | 24小时最低价  
> vol24h | String | 24小时交易量，单元为交易货币或美元  
> ts | String | 数据产生时间，Unix时间戳的毫秒数格式，如 1597026383085  
vol24h  
对于现货/U本位合约价差交易产品，以及U本位合约价差交易产品，交易量以交易货币为单位；对于币本位合约价差交易产品，交易量以USD为单位。 

### K线频道 

该频道使用业务WebSocket，不需鉴权。

获取K线数据，推送频率最快是间隔1秒推送一次数据。

#### URL Path

/ws/v5/business

> 请求示例
    
    
    {
       "id": "1512",
       "op":"subscribe",
       "args":[
          {
             "channel":"sprd-candle1D",
             "sprdId":"BTC-USDT_BTC-USDT-SWAP"
          }
       ]
    }
    
    
    
    
    import asyncio
    from okx.websocket.WsPublicAsync import WsPublicAsync
    
    def callbackFunc(message):
        print(message)
    
    async def main():
        ws = WsPublicAsync(url="wss://wspap.okx.com:8443/ws/v5/business")
        await ws.start()
        args = [
          {
             "channel":"sprd-candle1D",
             "sprdId":"BTC-USDT_BTC-USDT-SWAP"
          }
        ]
    
        await ws.subscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
        await ws.unsubscribe(args, callback=callbackFunc)
        await asyncio.sleep(10)
    
    asyncio.run(main())
    
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识。  
用户提供，返回参数中会返回以便于找到相应的请求。  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字且长度必须要在1-32位之间。  
op | String | 是 | 操作  
`subscribe`   
`unsubscribe`  
args | Array of objects | 是 | 请求订阅的频道列表  
> channel | String | 是 | 频道名  
`sprd-candle3M` `sprd-candle1M`   
`sprd-candle1W`   
`sprd-candle1D` `sprd-candle2D` `sprd-candle3D` `sprd-candle5D`   
`sprd-candle12H` `sprd-candle6H` `sprd-candle4H` `sprd-candle2H` `sprd-candle1H`   
`sprd-candle30m` `sprd-candle15m` `sprd-candle5m` `sprd-candle3m` `sprd-candle1m`   
`sprd-candle3Mutc` `sprd-candle1Mutc` `sprd-candle1Wutc` `sprd-candle1Dutc` `sprd-candle2Dutc` `sprd-candle3Dutc` `sprd-candle5Dutc` `sprd-candle12Hutc` `sprd-candle6Hutc`  
> sprdId | String | 是 | Spread ID  
  
> 成功返回示例
    
    
    {
      "id": "1512",
      "event": "subscribe",
      "arg": {
        "channel": "sprd-candle1D",
        "sprdId": "BTC-USDT_BTC-USDT-SWAP"
      },
      "connId": "a4d3ae55"
    }
    
    

> 失败返回示例
    
    
    {
      "id": "1512",
      "event": "error",
      "code": "60012",
      "msg": "Invalid request: {\"op\": \"subscribe\", \"argss\":[{ \"channel\" : \"sprd-candle1D\", \"instId\" : \"BTC-USD-191227\"}]}",
      "connId": "a4d3ae55"
    }
    
    

#### 返回参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
id | String | 否 | 消息的唯一标识  
event | String | 是 | 事件   
`subscribe`   
`unsubscribe`   
`error`  
arg | Object | 否 | 订阅的频道  
channel | String | 是 | 频道名  
sprdId | String | 是 | Spread ID  
code | String | 否 | 错误码  
msg | String | 否 | 错误消息  
  
> 推送示例
    
    
    {
      "arg": {
        "channel": "sprd-candle1D",
        "sprdId": "BTC-USDT_BTC-USD-SWAP"
      },
      "data": [
        [
          "1597026383085",
          "8533.02",
          "8553.74",
          "8527.17",
          "8548.26",
          "45247",
          "0"
        ]
      ]
    }
    
    

#### 推送数据参数

参数名 | 类型 | 描述  
---|---|---  
arg | Object | 订阅成功的频道  
> channel | String | 频道名  
> sprdId | String | Spread ID  
data | Array of Arrays | 订阅的数据  
> ts | String | 开始时间，Unix时间戳的毫秒数格式，如 1597026383085  
> o | String | 开盘价格  
> h | String | 最高价格  
> l | String | 最低价格  
> c | String | 收盘价格  
> vol | String | 交易量  
> confirm | String | K线状态   
`0`：K线未完结   
`1`：K线已完结  
返回值数组顺序分别为是： [ts,o,h,l,c,vol,confirm]