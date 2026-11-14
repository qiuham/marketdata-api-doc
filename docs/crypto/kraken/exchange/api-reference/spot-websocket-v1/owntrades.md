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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/owntrades'
updated_at: 2026-11-13
---

# Own Trades

> Subscribe to real-time trade execution updates for the authenticated user

WSS
ws-auth.kraken.com
ownTrades

The `ownTrades` channel streams executions for the authenticated user. A snapshot of the last 50 trades is sent on subscription, followed by real-time updates for any new trades.

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
> Value: `ownTrades`
>
> **token** `string` *required*
>
> Session token from the GetWebSocketsToken REST endpoint.
>
> **snapshot** `boolean`
>
> One of: `false`, `true`\\
>
> Default: `true`
>
> Includes initial snapshot of historical data.
>
> **consolidate\_taker** `boolean`
>
> One of: `false`, `true`\\
>
> Default: `true`
>
> If true, fills are consolidated by taker, otherwise all fills are shown.
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

The snapshot and update responses share the same schema. The payload is a JSON array containing the trade data, the channel name, and feed detail.

**\[0]** `object[]`

A list of trade objects. Each object is keyed by the Kraken trade identifier.

**properties**

**\<trade-id>** `object`

The key for each trade is the Kraken trade identifier.

**properties**

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

**margin\_borrow** `boolean`

Indicates if an execution is on margin, i.e. if the trade increased or reduced size of margin borrowing. On trade events only.

**cl\_ord\_id** `string`

An optional, alphanumeric client identifier associated with this order. Available on update messages only.

**ext\_exec\_id** `string`

Format: UUID

An optional, external partner execution identifier.

**userref** `integer`

An optional, numeric identifier associated with one or more orders. Available on update messages only.

**\[1]** `string`

Value: `ownTrades`

**\[2]** `object`

**properties**

**sequence** `integer`

Sequence number for this subscription.

```json Subscribe theme={null}
{
    "event": "subscribe",
    "subscription": {
        "name": "ownTrades",
        "token": "WW91ciBhdXRoZW50aWNhdGlvbiB0b2tlbiBnb2VzIGhlcmUu"
    }
}
```

```json Snapshot / Update theme={null}
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
        }
    ],
    "ownTrades",
    {
        "sequence": 2948
    }
]
```
