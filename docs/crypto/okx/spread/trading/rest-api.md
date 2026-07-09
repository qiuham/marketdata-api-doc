---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#spread-trading-rest-api
anchor_id: spread-trading-rest-api
api_type: REST
updated_at: 2026-07-09 19:38:00.825486
---

# REST API

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

---

# REST API

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