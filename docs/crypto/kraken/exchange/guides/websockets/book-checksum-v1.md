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
source_url: 'https://docs.kraken.com/exchange/guides/websockets/book-checksum-v1'
updated_at: 2026-11-13
---

# Book checksum (WebSocket v1)

> How to maintain the order book and validate the CRC32 checksum on the WebSocket v1 book channel

The `book` channel includes a CRC32 checksum with each update message. Validating it confirms your local book is correctly synchronised with the exchange.

Checksum verification is optional. You can validate on every update or periodically depending on throughput requirements. The checksum is always calculated over the **top 10 price levels** regardless of subscription depth.

> [!WARNING]
>
> Processing order matters. Price level updates arrive in the correct sequence from the exchange — the last entries in the array are the most recent. Do not sort by timestamp, as multiple updates for the same price level can occur within a single microsecond.

Checksums are not sent in snapshot messages — only in update messages. The checksum field (`"c"`) appears in the last bid or ask map structure in the message.

### Example `book` update

```json theme={null}
[
    0,
    {
        "a": [
            ["0.05120", "0.00000500", "1582905486.493008"],
            ["0.05275", "0.00000500", "1582905486.493034"]
        ]
    },
    {
        "b": [
            ["0.04765", "0.00000500", "1582905486.493008"],
            ["0.04940", "0.00000500", "1582905486.493034"]
        ],
        "c": "974947235"
    },
    "book-1000",
    "BTC/USD"
]
```

## Checksum calculation

### Algorithm

**1. Apply the update**

Apply all price level updates in the message to your local book before calculating the checksum.

**2. Build the asks string**

For each of the top 10 ask price levels, sorted by price **low to high**:

* Remove `.` from the price → `"0.05000"` → `"005000"`
* Remove leading zeros → `"005000"` → `"5000"`
* Apply the same formatting to the volume
* Append `price + volume` to the asks string

For example, price `"0.05000"` with volume `"0.00000304"` formats as `"5000304"`. Timestamps are not included.

**3. Build the bids string**

For each of the top 10 bid price levels, sorted by price **high to low**, apply the same formatting and append to the bids string.

**4. Concatenate and hash**

Concatenate **asks + bids** strings, then pass the result to a CRC32 function. Cast the result to an unsigned 32-bit integer and compare to the `"c"` field in the message.

### Example

Input book state:

```json theme={null}
{
  "as": [
    ["0.05005", "0.00000500", "1582905487.684110"],
    ["0.05010", "0.00000500", "1582905486.187983"],
    ["0.05015", "0.00000500", "1582905484.480241"],
    ["0.05020", "0.00000500", "1582905486.645658"],
    ["0.05025", "0.00000500", "1582905486.859009"],
    ["0.05030", "0.00000500", "1582905488.601486"],
    ["0.05035", "0.00000500", "1582905488.357312"],
    ["0.05040", "0.00000500", "1582905488.785484"],
    ["0.05045", "0.00000500", "1582905485.302661"],
    ["0.05050", "0.00000500", "1582905486.157467"]
  ],
  "bs": [
    ["0.05000", "0.00000500", "1582905487.439814"],
    ["0.04995", "0.00000500", "1582905485.119396"],
    ["0.04990", "0.00000500", "1582905486.432052"],
    ["0.04980", "0.00000500", "1582905480.609351"],
    ["0.04975", "0.00000500", "1582905476.793880"],
    ["0.04970", "0.00000500", "1582905486.767461"],
    ["0.04965", "0.00000500", "1582905481.767528"],
    ["0.04960", "0.00000500", "1582905487.378907"],
    ["0.04955", "0.00000500", "1582905483.626664"],
    ["0.04950", "0.00000500", "1582905488.509872"]
  ]
}
```

Concatenated input to CRC32 (newlines added for readability):

```text theme={null}
50055005010500501550050205005025500
50305005035500504050050455005050500
50005004995500499050049805004975500
49705004965500496050049555004950500
```

Expected result: **`974947235`**
