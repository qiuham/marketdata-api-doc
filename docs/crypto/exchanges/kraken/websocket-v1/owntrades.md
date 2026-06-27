---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/owntrades
api_type: WebSocket
updated_at: 2026-05-27 20:10:00.548128
---

# Own Trades

CHANNEL
**Endpoint:** `wss://ws-auth.kraken.com`
    ownTradesAuthentication Required

The `ownTrades` channel streams executions for this account. A snapshot of the last 50 trades for the user will be sent, followed by real-time updates for any new trades.

## Subscription Request

  * Request Schema
  * Example

### MESSAGE BODY

**event** `string` *required*

**Value:** `subscribe`

**subscription** `object`

    ↳ **name** `string` *required*

**Value:** `ownTrades`

    ↳ **token** `string` *required*

This is a authenticated request, a session token is required.

    ↳ **snapshot** `boolean`

**Possible values:**[`false`, `true`] 

**Default value:**`true`

Includes initial snapshot of historical data.

    ↳ **consolidate_taker** `boolean`

**Possible values:**[`false`, `true`] 

**Default value:**`true`

If true, fills are consolidated by taker, otherwise all fills are shown.

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
        "name": "ownTrades",  
        "token": "WW91ciBhdXRoZW50aWNhdGlvbiB0b2tlbiBnb2VzIGhlcmUu"  
      }  
    }  
    

## Subscription Snapshot and Update Response

  * Response Schema
  * Example

### MESSAGE BODY

****array [

**[0] trades** array [

A list of trades.

**[many] trade** object

**< trade-id>** object

The key for each trade is the Kraken trade identifier. 

**ordertxid** `string`

Order identifier.

**postxid** `integer`

Position identifier.

**pair** `string`

Asset pair.

**time** `string`

Unix timestamp of trade.

**type** `string`

Side of order (buy/sell).

**ordertype** `string`

Order type.

**price** `string`

Average price order was filled in quote currency.

**cost** `string`

Total cost of order in the quote currency.

**fee** `string`

Total fees in the quote currency.

**vol** `string`

Volume of the trade in base currency.

**margin** `string`

Initial margin (quote currency).

**margin_borrow** `boolean`

Indicates if an execution is on margin, i.e. if the trade increased or reduced size of margin borrowing. On trade events only.

**cl_ord_id** `string`

An optional, alphanumeric client identifier associated with this order. Available on update messages only. 

**ext_exec_id** `string`

**Format:** UUID

An optional, external partner execution identifier. 

**userref** `integer`

An optional, numeric identifier associated with one or more orders. Available on update messages only. 

]

**[1] channel_name** string

**Value:** `ownTrades`

The name of the channel.

**[2] feed_detail** object

**sequence** `integer`

Sequence number for this subscription.

]
    
    
    [  
      [  
        {  
          "TDLH43-DVQXD-2KHVYY": {  
            "cost": "1000000.00000",  
            "fee": "1600.00000",  
            "margin": "0.00000",  
            "ordertxid": "TDLH43-DVQXD-2KHVYY",  
            "ordertype": "limit",  
            "pair": "XBT/EUR",  
            "postxid": "OGTT3Y-C6I3P-XRI6HX",  
            "price": "100000.00000",  
            "time": "1560516023.070651",  
            "type": "sell",  
            "vol": "1000000000.00000000"  
          }  
        },  
        {  
          "TDLH43-DVQXD-2KHVYY": {  
            "cost": "1000000.00000",  
            "fee": "600.00000",  
            "margin": "0.00000",  
            "ordertxid": "TDLH43-DVQXD-2KHVYY",  
            "ordertype": "limit",  
            "pair": "XBT/EUR",  
            "postxid": "OGTT3Y-C6I3P-XRI6HX",  
            "price": "100000.00000",  
            "time": "1560516023.070658",  
            "type": "buy",  
            "vol": "1000000000.00000000"  
          }  
        },  
        {  
          "TDLH43-DVQXD-2KHVYY": {  
            "cost": "1000000.00000",  
            "fee": "1600.00000",  
            "margin": "0.00000",  
            "ordertxid": "TDLH43-DVQXD-2KHVYY",  
            "ordertype": "limit",  
            "pair": "XBT/EUR",  
            "postxid": "OGTT3Y-C6I3P-XRI6HX",  
            "price": "100000.00000",  
            "time": "1560520332.914657",  
            "type": "sell",  
            "vol": "1000000000.00000000"  
          }  
        },  
        {  
          "TDLH43-DVQXD-2KHVYY": {  
            "cost": "1000000.00000",  
            "fee": "600.00000",  
            "margin": "0.00000",  
            "ordertxid": "TDLH43-DVQXD-2KHVYY",  
            "ordertype": "limit",  
            "pair": "XBT/EUR",  
            "postxid": "OGTT3Y-C6I3P-XRI6HX",  
            "price": "100000.00000",  
            "time": "1560520332.914664",  
            "type": "buy",  
            "vol": "1000000000.00000000"  
          }  
        }  
      ],  
      "ownTrades",  
      {  
        "sequence": 2948  
      }  
    ]