---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: digital_asset
domain: exchanges
provider: kraken
provider_name: Kraken
product: api
product_id: kraken
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/openorders'
updated_at: 2026-11-13
---

# Open Orders

> Subscribe to real-time open order updates for the authenticated user

WSS
ws-auth.kraken.com
openOrders

The `openOrders` channel streams the open orders belonging to the authenticated user. The initial snapshot provides a list of all open orders, followed by real-time updates. For status change updates, such as `closed`, the fields `orderid` and `status` will be present in the payload.

## Subscribe

> [tab] Request
>
> **event** `string` *required*
>
> Value: `subscribe`
>
> **subscription** `object`
>
> **properties**
>
> **name** `string` *required*
>
> Value: `openOrders`
>
> **token** `string` *required*
>
> Session token from the GetWebSocketsToken REST endpoint.
>
> **ratecounter** `boolean`
>
> One of: `false`, `true`\\
>
> Default: `false`
>
> Includes rate-limit counter in updates.
>
> **rebased** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`\\
>
> Condition: Effective for viewing xStocks only
>
> If `true`, display in terms of underlying equity, otherwise display in terms of SPV tokens.
>
> **reqid** `string`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> The subscription status is returned via the [subscriptionStatus](https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/subscriptionstatus.md) message.

## Snapshot / Update

The snapshot and update responses share the same schema. The payload is a JSON array containing the order data, the channel name, and feed detail.

**\[0]** `object[]`

A list of order objects. Each object is keyed by the Kraken order identifier.

**properties**

**\<order-id>** `object`

The key for each order is the Kraken order identifier.

**properties**

**refid** `string`

Referral order transaction id that created this order.

**userref** `integer`

An optional, numeric identifier associated with one or more orders.

**cl\_ord\_id** `string`

An optional, alphanumeric client identifier associated with this order.

**ext\_ord\_id** `string`

Format: UUID

An optional, external partner order identifier.

**status** `string`

Status of order.

**opentm** `string`

Unix timestamp of when order was placed.

**starttm** `string`

Unix timestamp of order start time (if set).

**display\_volume** `string`

Condition: Iceberg orders only

The reload quantity for iceberg order types.

**display\_volume\_remain** `string`

Condition: Iceberg orders only

The visible quantity remaining in the book.

**expiretm** `string`

Unix timestamp of order end time (if set).

**contingent** `object`

Parameters for the conditional close order (if attached).

**properties**

**ordertype** `string`

Conditional close order type.

**price** `string`

Primary price of the conditional close order.

**price2** `string`

Secondary price of the conditional close order.

**oflags** `string`

Comma delimited list of order flags for the conditional close order. `fcib` = prefer fee in base currency, `fciq` = prefer fee in quote currency, `nompp` = no market price protection, `post` = post only order (available when ordertype = limit).

**descr** `object`

Order description info.

**properties**

**pair** `string`

Asset pair.

**position** `string`

Optional - position ID (if applicable).

**type** `string`

Side of order (buy/sell).

**ordertype** `string`

Order type.

**price** `string`

The limit price or trigger price depending on the order type:

* **limit** price for `limit` orders.
* **trigger** price for all triggered orders.

**price2** `string`

The **limit** price for `stop-loss-limit`, `take-profit-limit` and `trailing-stop-limit` orders.

**leverage** `string`

Amount of margin leverage.

**margin** `boolean`

Indicates if the order is funded on margin.

**order** `string`

Text summary of order.

**close** `string`

Text summary of conditional order (if conditional close attached).

**lastupdated** `string`

Unix timestamp of last change (for updates).

**vol** `string`

Volume of order (base currency unless viqc set in oflags).

**vol\_exec** `string`

Total volume executed so far (base currency unless viqc set in oflags).

**cost** `string`

Total cost (quote currency unless viqc set in oflags).

**fee** `string`

Total fee (quote currency).

**avg\_price** `string`

Average price (cumulative; quote currency unless viqc set in oflags).

**stopprice** `string`

Stop price (for trailing stops).

**limitprice** `string`

Triggered limit price (after limit based order types are triggered).

**misc** `string`

A comma delimited list of miscellaneous info:

* `stopped`: triggered by stop price
* `touched`: triggered by touch price
* `liquidation`: liquidation event
* `partial`: partial fill

**oflags** `string`

A comma delimited list of order flags:

* `viqc`: volume in quote currency
* `fcib`: prefer fee in base currency
* `fciq`: prefer fee in quote currency
* `nompp`: no market price protection
* `post`: post only order

**sender\_sub\_id** `string`

For institutional accounts, identifies underlying sub-account/trader for Self Trade Prevention (STP).

**timeinforce** `string`

One of: `GTC`, `GTD`, `IOC`, `FOK`\\

Default: `GTC`

Time-in-force specifies how long an order remains in effect before expiry.

* `GTC`: Good Till Canceled - until user has cancelled.
* `GTD`: Good Till Date - until `expiretm` parameter.
* `IOC`: Immediate Or Cancel - immediately cancels back any quantity that cannot be filled on arrival.
* `FOK`: Fill Or Kill - immediately fills the full order quantity or cancels it entirely.

**cancel\_reason** `string`

Cancel reason, present for all cancellation updates (status="canceled") and for some close updates (status="closed").

**amend\_reason** `string`

Amendment reason, present for all amend events.

**amended** `boolean`

One of: `true`, `false`

Indicates if the order has been amended, the modification history can be extracted from the REST `OrderAmends` endpoint.

**ratecount** `string`

Rate-limit counter, present if requested in subscription request. See Trading Rate Limits.

**\[1]** `string`

Value: `openOrders`

**\[2]** `object`

**properties**

**sequence** `integer`

Sequence number for this subscription.

```json Subscribe theme={null}
{
    "event": "subscribe",
    "subscription": {
        "name": "openOrders",
        "ratecounter": "true",
        "token": "WW91ciBhdXRoZW50aWNhdGlvbiB0b2tlbiBnb2VzIGhlcmUu"
    }
}
```

```json Snapshot / Update theme={null}
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
        }
    ],
    "openOrders",
    {
        "sequence": 234
    }
]
```

```json Status Update theme={null}
[
    [
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
```
