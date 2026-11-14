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
source_url: 'https://docs.kraken.com/exchange/guides/websockets/book-checksum-v2'
updated_at: 2026-11-13
---

# Book checksum (WebSocket v2)

> How to maintain the order book and validate the CRC32 checksum on the WebSocket v2 book channel

The `book` channel includes a CRC32 checksum with each update. Validating it confirms your local book is correctly synchronised with the exchange.

Checksum verification is optional. You can validate on every update or periodically depending on throughput requirements. The checksum is always calculated over the **top 10 price levels** regardless of subscription depth.

## Maintaining the book

* Process all price level updates in a message before calculating the checksum.
* An update with `"qty": 0` means that price level should be removed.
* After each update, truncate your book to the subscribed depth — you will not receive `"qty": 0` for levels that fall out of scope.

## Checksum calculation

> [!TIP]
>
> Parse `price` and `qty` fields using a decimal or string decoder to preserve full precision through deserialisation.

```python theme={null}
async for bytes in websocket:
    message = json.loads(bytes, parse_float=Decimal)
    self.on_message(message)
```

### Algorithm

**1. Build the asks string**

For each of the top 10 ask price levels, sorted by price **low to high**:

* Remove `.` from `price` → `"45285.2"` → `"452852"`
* Remove leading zeros → `"452852"` → `"452852"`
* Remove `.` from `qty` → `"0.00100000"` → `"000100000"`
* Remove leading zeros → `"000100000"` → `"100000"`
* Append `price + qty` to the asks string → `"452852100000"`

**2. Build the bids string**

For each of the top 10 bid price levels, sorted by price **high to low**, apply the same formatting and append to the bids string.

**3. Concatenate and hash**

Concatenate **asks + bids** strings, then pass the result to a CRC32 function. Cast the result to an unsigned 32-bit integer and compare to the `checksum` field in the message.

### Example

Input snapshot:

```json theme={null}
{
  "channel": "book",
  "type": "snapshot",
  "data": [{
    "symbol": "BTC/USD",
    "bids": [
      {"price": "45283.5", "qty": "0.10000000"},
      {"price": "45283.4", "qty": "1.54582015"},
      {"price": "45282.1", "qty": "0.10000000"},
      {"price": "45281.0", "qty": "0.10000000"},
      {"price": "45280.3", "qty": "1.54592586"},
      {"price": "45279.0", "qty": "0.07990000"},
      {"price": "45277.6", "qty": "0.03310103"},
      {"price": "45277.5", "qty": "0.30000000"},
      {"price": "45277.3", "qty": "1.54602737"},
      {"price": "45276.6", "qty": "0.15445238"}
    ],
    "asks": [
      {"price": "45285.2", "qty": "0.00100000"},
      {"price": "45286.4", "qty": "1.54571953"},
      {"price": "45286.6", "qty": "1.54571109"},
      {"price": "45289.6", "qty": "1.54560911"},
      {"price": "45290.2", "qty": "0.15890660"},
      {"price": "45291.8", "qty": "1.54553491"},
      {"price": "45294.7", "qty": "0.04454749"},
      {"price": "45296.1", "qty": "0.35380000"},
      {"price": "45297.5", "qty": "0.09945542"},
      {"price": "45299.5", "qty": "0.18772827"}
    ],
    "checksum": 3310070434
  }]
}
```

Asks string (low → high):

```text theme={null}
45285210000045286415457195345286615457110945289615456091145290215890660452918154553491452947445474945296135380000452975994554245299518772827
```

Bids string (high → low):

```text theme={null}
452835100000004528341545820154528211000000045281010000000452803154592586452790799000045277633101034527753000000045277315460273745276615445238
```

Concatenated input to CRC32:

```text theme={null}
45285210000045286415457195345286615457110945289615456091145290215890660452918154553491452947445474945296135380000452975994554245299518772827452835100000004528341545820154528211000000045281010000000452803154592586452790799000045277633101034527753000000045277315460273745276615445238
```

Expected result: **`3310070434`**
