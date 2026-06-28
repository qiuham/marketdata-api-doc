---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/openorders
api_type: WebSocket
updated_at: 2026-05-27 20:09:53.368371
---

# Open Orders

CHANNEL
**Endpoint:** `wss://ws-auth.kraken.com`
    openOrdersAuthentication Required

The `openOrders` channel streams streams the open orders belonging to the authenticated user. Initial snapshot will provide list of all open orders and then any updates to the open orders will be streamed.

For status change updates, such as 'closed', the fields orderid and status will be present in the payload.

## Subscription Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `subscribe`

**subscription** `object`

    ↳ **name** `string` *required*

**Value:** `openOrders`

    ↳ **token** `string` *required*

This is a authenticated request, a session token is required.

    ↳ **ratecounter** `boolean`

**Possible values:**[`false`, `true`] 

**Default value:**`false`

Includes rate-limit counter in updates.

    ↳ **rebased** `boolean` *conditional*

**Condition:** Effective for viewing xstocks only. 

**Possible values:**[`true`, ` false`] 

**Default value:**`true`

If `true`, display in terms of underlying equity, otherwise display in terms of SPV tokens.

    ↳ **reqid** `string`

Optional client originated request identifier sent as acknowledgment in the response.
    
    
    {  
      "event": "subscribe",  
      "subscription": {  
        "name": "openOrders",  
        "ratecounter": "true",  
        "token": "WW91ciBhdXRoZW50aWNhdGlvbiB0b2tlbiBnb2VzIGhlcmUu"  
      }  
    }  
    

## Subscription Snapshot and Update Response

  * Response Schema
  * Example: Orders
  * Example: Status Only

### MESSAGE BODY

****array [

**[0] orders** array [

A list of orders.

**[many] order** object

**< order-id>** object

The key for each order is the Kraken order identifier. 

**refid** `string`

Referral order transaction id that created this order.

**userref** `integer`

An optional, numeric identifier associated with one or more orders.

**cl_ord_id** `string`

An optional, alphanumeric client identifier associated with this order.

**ext_ord_id** `string`

**Format:** UUID

An optional, external partner order identifier. 

**status** `string`

Status of order.

**opentm** `string`

Unix timestamp of when order was placed.

**starttm** `string`

Unix timestamp of order start time (if set).

**display_volume** `string` *conditional*

**Condition:** Iceberg orders only. 

The reload quantity for iceberg order types.

**display_volume_remain** `string` *conditional*

**Condition:** Iceberg orders only. 

The visible quantity remaining in the book.

**expiretm** `string`

Unix timestamp of order end time (if set).

**contingent** `object` *conditional*

**Condition:** Parameters for the conditional close order (if attached). 

    ↳ **ordertype** `string`

Conditional close order type.

    ↳ **price** `string`

Primary price of the conditional close order.

**price2** string

Secondary price of the conditional close order.

    ↳ **oflags** `string`

Comma delimited list of order flags for the conditional close order. fcib = prefer fee in base currency, fciq = prefer fee in quote currency, nompp = no market price protection, post = post only order (available when ordertype = limit).

    ↳ **descr** `object`

order description info 

        ↳ **pair** `string`

asset pair.

        ↳ **position** `string`

Optional - position ID (if applicable).

        ↳ **type** `string`

Side of order (buy/sell).

        ↳ **ordertype** `string`

Order type.

        ↳ **price** `string`

The limit price or trigger price depending on the order type:

  * **limit** price for `limit` orders.
  * **trigger** price for all triggered orders

**price2** string

The **limit** price for `stop-loss-limit`, `take-profit-limit` and `trailing-stop-limit` orders.

        ↳ **leverage** `string`

Amount of margin leverage.

        ↳ **margin** `boolean`

Indicates if the order is funded on margin.

        ↳ **order** `string`

Text summary of order.

        ↳ **close** `string`

Text summary of conditional order (if conditional close attached).

        ↳ **lastupdated** `string`

Unix timestamp of last change (for updates).

        ↳ **vol** `string`

Volume of order (base currency unless viqc set in oflags).

        ↳ **vol_exec** `string`

Total volume executed so far (base currency unless viqc set in oflags).

        ↳ **cost** `string`

Total cost (quote currency unless unless viqc set in oflags).

        ↳ **fee** `string`

Total fee (quote currency).

        ↳ **avg_price** `string`

Average price (cumulative; quote currency unless viqc set in oflags).

        ↳ **stopprice** `string`

Stop price (for trailing stops).

        ↳ **limitprice** `string`

Triggered limit price (after limit based order types are triggered).

        ↳ **misc** `string`

A comma delimited list of miscellaneous info:

  * `stopped`: triggered by stop price
  * `touched`: triggered by touch price
  * `liquidation`: liquidation event
  * `partial`: partial fill

        ↳ **oflags** `string`

A comma delimited list of order flags:

  * `viqc`: volume in quote currency
  * `fcib`: prefer fee in base currency
  * `fciq`: prefer fee in quote currency
  * `nompp`: no market price protection
  * `post`: post only order

        ↳ **sender_sub_id** `string`

For institutional accounts, identifies underlying sub-account/trader for Self Trade Prevention (STP).

        ↳ **timeinforce** `string`

**Possible values:**[`GTC`, ` GTD`, ` IOC`] 

**Default value:**`GTC`

Time-in-force specifies how long an order remains in effect before expiry.

  * `GTC`: Good Till Canceled - until user has cancelled.
  * `GTD`: Good Till Date - until `expiretm` parameter.
  * `IOC`: Immediate Or Cancel - immediately cancels back any quantity that cannot be filled on arrival.

        ↳ **cancel_reason** `string`

Cancel reason, present for all cancellation updates (status="canceled") and for some close updates (status="closed").

        ↳ **amend_reason** `string`

Amendment reason, present for all amend events.

        ↳ **amended** `boolean`

**Possible values:**[`true`, `false`] 

Indicates if the order has been amended, the modification history can be extracted from the REST `OrderAmends` endpoint.

        ↳ **ratecount** `string`

Rate-limit counter, present if requested in subscription request. See Trading Rate Limits.

]

]

**[1] channel_name** string

**Value:** `openOrders`

The name of the channel.

**[2] feed_detail** object

        ↳ **sequence** `integer`

Sequence number for this subscription.
    
    
    [  
      [  
        {  
          "OGTT3Y-C6I3P-XRI6HX": {  
            "avg_price": "34.50000",  
            "cost": "0.00000",  
            "descr": {  
              "close": "",  
              "leverage": "0:1",  
              "order": "sell 10.00345345 XBT/EUR @ limit 34.50000 with 0:1 leverage",  
              "ordertype": "limit",  
              "pair": "XBT/EUR",  
              "price": "34.50000",  
              "price2": "0.00000",  
              "type": "sell"  
            },  
            "expiretm": "0.000000",  
            "fee": "0.00000",  
            "limitprice": "34.50000",  
            "misc": "",  
            "oflags": "fcib",  
            "opentm": "0.000000",  
            "refid": "OKIVMP-5GVZN-Z2D2UA",  
            "starttm": "0.000000",  
            "status": "open",  
            "stopprice": "0.000000",  
            "userref": 0,  
            "vol": "10.00345345",  
            "vol_exec": "0.00000000"  
          }  
        },  
        {  
          "OGTT3Y-C6I3P-XRI6HX": {  
            "avg_price": "5334.60000",  
            "cost": "0.00000",  
            "descr": {  
              "close": "",  
              "leverage": "0:1",  
              "order": "sell 0.00000010 XBT/EUR @ limit 5334.60000 with 0:1 leverage",  
              "ordertype": "limit",  
              "pair": "XBT/EUR",  
              "price": "5334.60000",  
              "price2": "0.00000",  
              "type": "sell"  
            },  
            "expiretm": "0.000000",  
            "fee": "0.00000",  
            "limitprice": "5334.60000",  
            "misc": "",  
            "oflags": "fcib",  
            "opentm": "0.000000",  
            "refid": "OKIVMP-5GVZN-Z2D2UA",  
            "starttm": "0.000000",  
            "status": "open",  
            "stopprice": "0.000000",  
            "userref": 0,  
            "vol": "0.00000010",  
            "vol_exec": "0.00000000"  
          }  
        },  
        {  
          "OGTT3Y-C6I3P-XRI6HX": {  
            "avg_price": "90.40000",  
            "cost": "0.00000",  
            "descr": {  
              "close": "",  
              "leverage": "0:1",  
              "order": "sell 0.00001000 XBT/EUR @ limit 90.40000 with 0:1 leverage",  
              "ordertype": "limit",  
              "pair": "XBT/EUR",  
              "price": "90.40000",  
              "price2": "0.00000",  
              "type": "sell"  
            },  
            "expiretm": "0.000000",  
            "fee": "0.00000",  
            "limitprice": "90.40000",  
            "misc": "",  
            "oflags": "fcib",  
            "opentm": "0.000000",  
            "refid": "OKIVMP-5GVZN-Z2D2UA",  
            "starttm": "0.000000",  
            "status": "open",  
            "stopprice": "0.000000",  
            "userref": 0,  
            "vol": "0.00001000",  
            "vol_exec": "0.00000000"  
          }  
        },  
        {  
          "OGTT3Y-C6I3P-XRI6HX": {  
            "avg_price": "9.00000",  
            "cost": "0.00000",  
            "descr": {  
              "close": "",  
              "leverage": "0:1",  
              "order": "sell 0.00001000 XBT/EUR @ limit 9.00000 with 0:1 leverage",  
              "ordertype": "limit",  
              "pair": "XBT/EUR",  
              "price": "9.00000",  
              "price2": "0.00000",  
              "type": "sell"  
            },  
            "expiretm": "0.000000",  
            "fee": "0.00000",  
            "limitprice": "9.00000",  
            "misc": "",  
            "oflags": "fcib",  
            "opentm": "0.000000",  
            "refid": "OKIVMP-5GVZN-Z2D2UA",  
            "starttm": "0.000000",  
            "status": "open",  
            "stopprice": "0.000000",  
            "userref": 0,  
            "vol": "0.00001000",  
            "vol_exec": "0.00000000"  
          }  
        }  
      ],  
      "openOrders",  
      {  
        "sequence": 234  
      }  
    ]  
    
    
    
    [  
      [  
        {  
          "OGTT3Y-C6I3P-XRI6HX": {  
            "status": "closed"  
          }  
        },  
        {  
          "OGTT3Y-C6I3P-XRI6HX": {  
            "status": "closed"  
          }  
        }  
      ],  
      "openOrders",  
      {  
        "sequence": 59342  
      }  
    ]