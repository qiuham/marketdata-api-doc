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
source_url: 'https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/book'
updated_at: 2026-11-13
---

# Book

> Subscribe to order book levels (Level 2)

WSS
ws.kraken.com
book

Order book levels. On subscription, a snapshot is published at the specified depth, followed by level updates. Subscription depth options are 10, 25, 100, 500, or 1000 levels per side.

## Subscribe

> [tab] Request
>
> **event** `string` *required*
>
> Value: `subscribe`
>
> **pair** `string[]` *required*
>
> Example: `["BTC/USD", "MATIC/GBP"]`
>
> The currency pairs for this request.
>
> **subscription** `object`
>
> **properties**
>
> **name** `string` *required*
>
> Value: `book`
>
> **depth** `integer`
>
> One of: `10`, `25`, `100`, `500`, `1000`\\
>
> Default: `10`
>
> Specifies the number of price levels (in each side of the book) to be received.
>
> **reqid** `string`
>
> Optional client originated request identifier sent as acknowledgment in the response.

> [tab] Response
>
> The subscription status is returned via the [subscriptionStatus](https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/subscriptionstatus.md) message.

## Snapshot

Note, there is no checksum on the snapshot.

**elements**

**\[0] channel\_id** `integer` *deprecated*

Deprecated: use `channelName` and `pair`

Channel identifier.

**\[1] book** `object`

**properties**

**as** `array`

Ask price levels, ascending from best ask.

**elements**

**level** `array`

**elements**

**\[0] price** `string`

The price of this level.

**\[1] volume** `string`

Price level volume, for updates volume = 0 for level removal/deletion.

**\[2] timestamp** `string`

Format: Epoch Seconds\\

Example: `1534614248.456738`

Timestamp when the level last updated.

**bs** `array`

Bid price levels, ascending from best bid.

**elements**

**level** `array`

**elements**

**\[0] price** `string`

Price level.

**\[1] volume** `string`

Price level volume, for updates volume = 0 for level removal/deletion.

**\[2] timestamp** `string`

Format: Epoch Seconds\\

Example: `1534614248.456738`

Timestamp when the level last updated.

**\[2] pair** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**\[3] channel\_name** `string`

Value: `book-[depth]`

## Update

**elements**

**\[0] channel\_id** `integer` *deprecated*

Deprecated: use `channelName` and `pair`

Channel identifier.

**\[1] book** `object`

**properties**

**a** `array`

Ask price levels.

**elements**

**level** `array`

**elements**

**\[0] price** `string`

The price for this level.

**\[1] volume** `string`

The cumulative volume at this price level. If volume is 0, remove level from book.

**\[2] timestamp** `string`

Format: Epoch Seconds\\

Example: `1534614248.456738`

Timestamp when the level was last updated.

**\[3] update\_type** `string`

One of: `r`\\

Condition: Republish only

**c** `string`

Example: `"4088505763"`\\

Condition: Only present on last update

Book checksum as a quoted unsigned 32-bit integer.

**b** `array`

Bid price levels.

**elements**

**level** `array`

**elements**

**\[0] price** `string`

The price for this level.

**\[1] volume** `string`

The cumulative volume at this price level. If volume is 0, remove level from book.

**\[2] timestamp** `string`

Format: Epoch Seconds\\

Example: `1534614248.456738`

Timestamp when the level was last updated.

**\[3] update\_type** `string`

One of: `r`\\

Condition: Republish only

**c** `string`

Example: `"4088505763"`\\

Condition: Only present on last update

Book checksum as a quoted unsigned 32-bit integer.

**\[2] pair** `string`

Example: `"BTC/USD"`

The symbol of the currency pair.

**\[3] channel\_name** `string`

Value: `book-[depth]`

## Unsubscribe

> [tab] Request
>
> **event** `string` *required*
>
> Value: `unsubscribe`
>
> **pair** `string[]`
>
> Example: `["BTC/USD", "MATIC/GBP"]`\\
>
> Condition: All channels which support pair subscriptions
>
> The currency pairs to unsubscribe.
>
> **reqid** `string`
>
> Optional client originated request identifier sent as acknowledgment in the response.
>
> **subscription** `object`
>
> **properties**
>
> **name** `string` *required*
>
> Value: `book`
>
> **depth** `integer`
>
> Condition: 'book' channel only
>
> Unsubscribe to a specific depth.

> [tab] Response
>
> The unsubscription status is returned via the [subscriptionStatus](https://docs.kraken.com/exchange/api-reference/spot-websocket-v1/subscriptionstatus.md) message.

```json Subscribe theme={null}
{
  "event": "subscribe",
  "pair": [
    "XBT/USD",
    "XBT/EUR"
  ],
  "subscription": {
    "name": "book"
  }
}
```

```json Snapshot theme={null}
[
  0,
  {
    "as": [
      [
        "5541.30000",
        "2.50700000",
        "1534614248.123678"
      ],
      [
        "5541.80000",
        "0.33000000",
        "1534614098.345543"
      ],
      [
        "5542.70000",
        "0.64700000",
        "1534614244.654432"
      ]
    ],
    "bs": [
      [
        "5541.20000",
        "1.52900000",
        "1534614248.765567"
      ],
      [
        "5539.90000",
        "0.30000000",
        "1534614241.769870"
      ],
      [
        "5539.50000",
        "5.00000000",
        "1534613831.243486"
      ]
    ]
  },
  "book-100",
  "XBT/USD"
]
```

```json Update: Asks theme={null}
[
  1234,
  {
    "a": [
      [
        "5541.30000",
        "2.50700000",
        "1534614248.456738"
      ],
      [
        "5542.50000",
        "0.40100000",
        "1534614248.456738"
      ]
    ],
    "c": "974942666"
  },
  "book-10",
  "XBT/USD"
]
```

```json Update: Bids theme={null}
[
  1234,
  {
    "b": [
      [
        "5541.30000",
        "0.00000000",
        "1534614335.345903"
      ]
    ],
    "c": "974942666"
  },
  "book-10",
  "XBT/USD"
]
```

```json Update: Bids and Asks theme={null}
[
  1234,
  {
    "a": [
      [
        "5541.30000",
        "2.50700000",
        "1534614248.456738"
      ],
      [
        "5542.50000",
        "0.40100000",
        "1534614248.456738"
      ]
    ]
  },
  {
    "b": [
      [
        "5541.30000",
        "0.00000000",
        "1534614335.345903"
      ]
    ],
    "c": "974942666"
  },
  "book-10",
  "XBT/USD"
]
```

```json Update: Republish theme={null}
[
  1234,
  {
    "a": [
      [
        "5541.30000",
        "2.50700000",
        "1534614248.456738",
        "r"
      ],
      [
        "5542.50000",
        "0.40100000",
        "1534614248.456738",
        "r"
      ]
    ],
    "c": "974942666"
  },
  "book-25",
  "XBT/USD"
]
```

```json Unsubscribe theme={null}
{
  "event": "unsubscribe",
  "pair": [
    "XBT/EUR",
    "XBT/USD"
  ],
  "subscription": {
    "name": "book"
  }
}
```
