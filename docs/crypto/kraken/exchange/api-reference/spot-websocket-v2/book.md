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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v2/book'
updated_at: 2026-11-13
---

# Book (Level 2)

> Subscribe to level 2 order book data with aggregated quantities at each price level

WSS
ws.kraken.com/v2
book

The `book` channel streams level 2 (L2) order book. It describes the individual price levels in the book with aggregated order quantities at each level.

Subscriptions to this channel can be made for multiple symbols at once by specifying a list of pairs in the `symbol`.

For more detail on maintaining the order book and generating a checksum, see [guide](https://docs.kraken.com/exchange/guides/websockets/book-checksum-v2.md).

## Subscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `subscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `book`
>
> **symbol** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> A list of currency pairs.
>
> **depth** `integer`
>
> One of: `10`, `25`, `100`, `500`, `1000`\\
>
> Default: `10`
>
> The number of price levels to be received.
>
> **snapshot** `boolean`
>
> One of: `true`, `false`\\
>
> Default: `true`
>
> Request a snapshot after subscribing.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> There is a separate acknowledgement response for each symbol in the subscription list.
>
> **method** `string` *required*
>
> Value: `subscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `book`
>
> **symbol** `string` *required*
>
> Example: `"BTC/USD"`
>
> The currency pair associated with this subscription.
>
> **depth** `integer`
>
> One of: `10`, `25`, `100`, `500`, `1000`
>
> Specifies the number of price levels (in each side of the book) to be received.
>
> **snapshot** `boolean`
>
> Indicates if a snapshot is requested.
>
> **warnings** `string[]`
>
> An advisory message, highlighting deprecated fields or upcoming changes to the channel.
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot

The returned snapshot data contains the specified number of bids and asks for the symbol including a CRC32 checksum of the top 10 bids and asks.

**channel** `string`

Value: `book`

**type** `string`

One of: `snapshot`

**data** `object[]`

**properties**

**asks** `object[]`

**properties**

**price** `float`

The ask price.

**qty** `float`

The ask quantity.

**bids** `object[]`

**properties**

**price** `float`

The bid price.

**qty** `float`

The bid quantity.

**checksum** `integer`

CRC32 checksum for the top 10 bids and asks.

**symbol** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**timestamp** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

The timestamp of the order book snapshot.

## Update

The data contains the updates of the bids and asks for the relevant symbol including a CRC32 checksum of the top 10 bids and asks.

Note, it is possible to have multiple updates to the same price level in a single update message. Updates should always be processed in sequence.

**channel** `string`

Value: `book`

**type** `string`

One of: `update`

**data** `object[]`

**properties**

**asks** `object[]`

**properties**

**price** `float`

The ask price.

**qty** `float`

The ask quantity.

**bids** `object[]`

**properties**

**price** `float`

The bid price.

**qty** `float`

The bid quantity.

**checksum** `integer`

CRC32 checksum for the top 10 bids and asks.

**symbol** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**timestamp** `string`

Format: RFC3339\\

Example: `2022-12-25T09:30:59.123456Z`

The book order update timestamp.

## Unsubscribe

> [tab] Request
>
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **params** `object` *required*
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `book`
>
> **symbol** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> A list of currency pairs.
>
> **depth** `integer`
>
> One of: `10`, `25`, `100`, `500`, `1000`
>
> The number of price levels to be unsubscribed.
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> There is a separate acknowledgement response for each symbol in the unsubscription list.
>
> **method** `string` *required*
>
> Value: `unsubscribe`
>
> **result** `object`
>
> **properties**
>
> **channel** `string` *required*
>
> Value: `book`
>
> **symbol** `string` *required*
>
> Example: `"BTC/USD"`
>
> The currency pair associated with this subscription.
>
> **depth** `integer`
>
> One of: `10`, `25`, `100`, `500`, `1000`
>
> Specifies the number of price levels (in each side of the book) to be unsubscribed.
>
> **success** `boolean`
>
> Indicates if the request was successfully processed by the engine. One of: `true`, `false`
>
> **error** `string`
>
> Error message. Condition: if `success` is `false`.
>
> **time\_in** `string`
>
> The timestamp when the subscription was received on the wire, just prior to parsing data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **time\_out** `string`
>
> The timestamp when the acknowledgement was sent on the wire, just prior to transmitting data. Format: RFC3339. Example: `2022-12-25T09:30:59.123456Z`
>
> **req\_id** `integer`
>
> Optional client originated request identifier sent as acknowledgment in the response.

```json Subscribe Request theme={null}
{
    "method": "subscribe",
    "params": {
        "channel": "book",
        "symbol": [
            "ALGO/USD",
            "MATIC/USD"
        ]
    }
}
```

```json Subscribe Response theme={null}
{
    "method": "subscribe",
    "result": {
        "channel": "book",
        "depth": 10,
        "snapshot": true,
        "symbol": "ALGO/USD"
    },
    "success": true,
    "time_in": "2023-10-06T17:35:55.219022Z",
    "time_out": "2023-10-06T17:35:55.219067Z"
}

{
    "method": "subscribe",
    "result": {
        "channel": "book",
        "depth": 10,
        "snapshot": true,
        "symbol": "MATIC/USD"
    },
    "success": true,
    "time_in": "2023-10-06T17:35:55.219022Z",
    "time_out": "2023-10-06T17:35:55.219067Z"
}
```

```json Snapshot theme={null}
{
    "channel": "book",
    "type": "snapshot",
    "data": [
        {
            "symbol": "MATIC/USD",
            "bids": [
                {
                    "price": 0.5666,
                    "qty": 4831.75496356
                },
                {
                    "price": 0.5665,
                    "qty": 6658.22734739
                },
                {
                    "price": 0.5664,
                    "qty": 18724.91513344
                },
                {
                    "price": 0.5663,
                    "qty": 11563.92544914
                },
                {
                    "price": 0.5662,
                    "qty": 14006.65365711
                },
                {
                    "price": 0.5661,
                    "qty": 17454.85679807
                },
                {
                    "price": 0.566,
                    "qty": 18097.1547
                },
                {
                    "price": 0.5659,
                    "qty": 33644.89175666
                },
                {
                    "price": 0.5658,
                    "qty": 148.3464
                },
                {
                    "price": 0.5657,
                    "qty": 606.70854372
                }
            ],
            "asks": [
                {
                    "price": 0.5668,
                    "qty": 4410.79769741
                },
                {
                    "price": 0.5669,
                    "qty": 4655.40412487
                },
                {
                    "price": 0.567,
                    "qty": 49844.89424998
                },
                {
                    "price": 0.5671,
                    "qty": 24306.41678
                },
                {
                    "price": 0.5672,
                    "qty": 29783.25223475
                },
                {
                    "price": 0.5673,
                    "qty": 57234.71239278
                },
                {
                    "price": 0.5674,
                    "qty": 45065.04744
                },
                {
                    "price": 0.5675,
                    "qty": 5912.76380354
                },
                {
                    "price": 0.5676,
                    "qty": 42514.92434778
                },
                {
                    "price": 0.5677,
                    "qty": 36304.0847022
                }
            ],
            "checksum": 2439117997,
            "timestamp": "2023-10-06T17:35:55.440295Z"
        }
    ]
}
```

```json Update theme={null}
{
    "channel": "book",
    "type": "update",
    "data": [
        {
            "symbol": "MATIC/USD",
            "bids": [
                {
                    "price": 0.5657,
                    "qty": 1098.3947558
                }
            ],
            "asks": [],
            "checksum": 2114181697,
            "timestamp": "2023-10-06T17:35:55.440295Z"
        }
    ]
}
```

```json Unsubscribe Request theme={null}
{
    "method": "unsubscribe",
    "params": {
        "channel": "book",
        "symbol": [
            "ALGO/USD",
            "MATIC/USD"
        ]
    }
}
```

```json Unsubscribe Response theme={null}
{
    "method": "unsubscribe",
    "result": {
        "channel": "book",
        "depth": 10,
        "snapshot": true,
        "symbol": "ALGO/USD"
    },
    "success": true,
    "time_in": "2023-10-06T17:35:55.219022Z",
    "time_out": "2023-10-06T17:35:55.219067Z"
}

{
    "method": "unsubscribe",
    "result": {
        "channel": "book",
        "depth": 10,
        "snapshot": true,
        "symbol": "MATIC/USD"
    },
    "success": true,
    "time_in": "2023-10-06T17:35:55.219022Z",
    "time_out": "2023-10-06T17:35:55.219067Z"
}
```
