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
source_url: 'https://docs.kraken.com/exchange/guides/websockets/l3-checksum-v2'
updated_at: 2026-11-13
---

# L3 checksum (WebSocket v2)

> How to maintain the level3 order book and validate the CRC32 checksum on the WebSocket v2 level3 channel

The `level3` channel includes a CRC32 checksum with each update. Validating it confirms your local book is correctly synchronised with the exchange, including the order sequence within each price level.

Checksum verification is optional. You can validate on every update or periodically depending on throughput requirements. The checksum is always calculated over the **top 10 price levels** regardless of subscription depth.

The `level3` checksum logic is similar to the `book` feed — see the [Book checksum (v2)](https://docs.kraken.com/exchange/guides/websockets/book-checksum-v2.md) guide. The key difference is that `level3` iterates through individual orders within each price level, so it also verifies queue priority.

## Maintaining the book

* Process all orders in a message before calculating the checksum.
* A price level with no remaining orders or quantity should be removed from your book.
* After each update, truncate your book to the subscribed depth. If a price level drops out of scope, all orders at the next available price level will be published to maintain the subscription depth.

## Checksum calculation

> [!TIP]
>
> Parse `limit_price` and `order_qty` fields using a decimal or string decoder to preserve full precision through deserialisation.

```python theme={null}
async for bytes in websocket:
    message = json.loads(bytes, parse_float=Decimal)
    self.on_message(message)
```

### Algorithm

**1. Build the asks string**

For each of the top 10 ask price levels, sorted by price **low to high**, iterate through each order in the price level:

* Remove `.` from `limit_price` → `"44939.5"` → `"449395"`
* Remove leading zeros → `"449395"` → `"449395"`
* Remove `.` from `order_qty` → `"4.52308393"` → `"452308393"`
* Remove leading zeros → `"452308393"` → `"452308393"`
* Append `limit_price + order_qty` to the asks string → `"449395452308393"`

**2. Build the bids string**

For each of the top 10 bid price levels, sorted by price **high to low**, iterate through each order in the price level and apply the same formatting, appending to the bids string.

**3. Concatenate and hash**

Concatenate **asks + bids** strings, then pass the result to a CRC32 function. Cast the result to an unsigned 32-bit integer and compare to the `checksum` field in the message.

### Example

Input snapshot:

```json theme={null}
{
  "channel": "level3",
  "type": "snapshot",
  "data": [{
    "symbol": "BTC/USD",
    "checksum": 1063832831,
    "bids": [
      {"order_id": "OTCFZG-YOE2Q-LQKNM3", "limit_price": "44939.4", "order_qty": "0.88968699", "timestamp": "2024-01-08T12:26:39.526146327Z"},
      {"order_id": "OFGP5R-B3E7G-54EZD6", "limit_price": "44939.4", "order_qty": "0.45210000", "timestamp": "2024-01-08T12:26:39.530287934Z"},
      {"order_id": "OMPHVY-IZPJ4-KOKA3P", "limit_price": "44939.4", "order_qty": "0.10000000", "timestamp": "2024-01-08T12:26:39.576380340Z"},
      {"order_id": "OAI5QZ-AMPLW-NBNO72", "limit_price": "44939.4", "order_qty": "0.14296323", "timestamp": "2024-01-08T12:26:39.602118534Z"},
      {"order_id": "O7VFZI-CTFWH-FF6EIR", "limit_price": "44939.4", "order_qty": "0.25000000", "timestamp": "2024-01-08T12:26:41.780601700Z"},
      {"order_id": "O472V3-ZG4EZ-OLD66C", "limit_price": "44939.4", "order_qty": "0.10292988", "timestamp": "2024-01-08T12:26:43.087136366Z"},
      {"order_id": "OEK26P-BGPUK-LDHMD2", "limit_price": "44939.4", "order_qty": "0.33880000", "timestamp": "2024-01-08T12:26:43.822433365Z"},
      {"order_id": "OSMYPE-S5VOC-YSS3WM", "limit_price": "44939.4", "order_qty": "1.28140860", "timestamp": "2024-01-08T12:26:45.066096694Z"},
      {"order_id": "OJPMIN-NXZL5-SOWP6V", "limit_price": "44937.1", "order_qty": "0.03346877", "timestamp": "2024-01-08T12:26:39.691304329Z"},
      {"order_id": "O6PUGE-SQWYQ-TRJEEE", "limit_price": "44934.7", "order_qty": "0.35630000", "timestamp": "2024-01-08T12:26:44.129718463Z"},
      {"order_id": "OPUOGC-Q532V-3OKLPM", "limit_price": "44930.2", "order_qty": "0.22734299", "timestamp": "2024-01-08T12:26:30.769031831Z"},
      {"order_id": "OCIU7J-VB3CI-HPULSF", "limit_price": "44930.2", "order_qty": "0.01000000", "timestamp": "2024-01-08T12:26:36.054352106Z"},
      {"order_id": "ORWVAF-LJFLY-ZWEHDQ", "limit_price": "44930.2", "order_qty": "0.05550000", "timestamp": "2024-01-08T12:26:36.635882793Z"},
      {"order_id": "OYRAHE-PI5AN-7KOQ4E", "limit_price": "44930.2", "order_qty": "0.70000000", "timestamp": "2024-01-08T12:26:37.296554518Z"},
      {"order_id": "OGBHYU-UILDD-6DLLYJ", "limit_price": "44930.2", "order_qty": "0.15000000", "timestamp": "2024-01-08T12:26:41.222733191Z"},
      {"order_id": "O74ZBU-K2TKC-R76XSW", "limit_price": "44928.0", "order_qty": "0.00105240", "timestamp": "2024-01-08T12:26:23.542563322Z"},
      {"order_id": "OQVTQF-Y56MR-BM6LWL", "limit_price": "44919.6", "order_qty": "0.33870000", "timestamp": "2024-01-08T12:26:42.808132842Z"},
      {"order_id": "OYEH6U-ZCHA2-3HFR3W", "limit_price": "44919.5", "order_qty": "0.07610000", "timestamp": "2024-01-08T12:26:34.269600037Z"},
      {"order_id": "OLGPG7-HVKXU-J6SANK", "limit_price": "44912.0", "order_qty": "0.35630000", "timestamp": "2024-01-08T12:26:34.961292766Z"},
      {"order_id": "OHGC3L-FRZQ3-UIVZRU", "limit_price": "44909.7", "order_qty": "0.06690000", "timestamp": "2024-01-08T12:26:31.912880024Z"},
      {"order_id": "O73C6Y-VZXYA-H4LDFY", "limit_price": "44901.9", "order_qty": "0.00088982", "timestamp": "2024-01-08T12:26:42.883315043Z"}
    ],
    "asks": [
      {"order_id": "OFVLAA-HRSSP-BK75KB", "limit_price": "44939.5", "order_qty": "4.52308393", "timestamp": "2024-01-08T12:18:05.770906486Z"},
      {"order_id": "OYBAMK-O5DKX-WMPUTM", "limit_price": "44939.5", "order_qty": "0.00111261", "timestamp": "2024-01-08T12:18:12.847426441Z"},
      {"order_id": "O3DRCT-J5M2S-KYV526", "limit_price": "44939.5", "order_qty": "0.00100000", "timestamp": "2024-01-08T12:26:42.108176464Z"},
      {"order_id": "OF3X3A-72WZY-6EKA5F", "limit_price": "44939.5", "order_qty": "0.01000000", "timestamp": "2024-01-08T12:26:43.955098263Z"},
      {"order_id": "OF5UA6-6IIZ2-YGQTSJ", "limit_price": "44950.0", "order_qty": "0.10334926", "timestamp": "2024-01-08T12:25:52.800473795Z"},
      {"order_id": "OSDOZX-7UZ6Y-QDNPVI", "limit_price": "44953.0", "order_qty": "0.00064537", "timestamp": "2024-01-08T12:24:58.086806970Z"},
      {"order_id": "OV7KTS-A2TWV-3XKRIA", "limit_price": "44955.0", "order_qty": "0.00250000", "timestamp": "2024-01-08T12:21:52.257936228Z"},
      {"order_id": "OOF2V5-RYOHC-GLRNPM", "limit_price": "44959.6", "order_qty": "0.35630000", "timestamp": "2024-01-08T12:26:44.202823127Z"},
      {"order_id": "OTVOVS-QLST3-3JG7JI", "limit_price": "44959.6", "order_qty": "0.35630000", "timestamp": "2024-01-08T12:26:44.203383999Z"},
      {"order_id": "OGZCIU-RDQ77-DAAL3P", "limit_price": "44960.1", "order_qty": "0.00338072", "timestamp": "2024-01-08T12:26:42.724829715Z"},
      {"order_id": "OVLG3E-HYBQM-CWNGCY", "limit_price": "44960.2", "order_qty": "0.88967575", "timestamp": "2024-01-08T12:26:12.935924248Z"},
      {"order_id": "OWEOFO-HUCJC-T37MVO", "limit_price": "44967.0", "order_qty": "3.14392283", "timestamp": "2024-01-08T12:26:39.474431925Z"},
      {"order_id": "OVYTHY-D2N76-5QYREQ", "limit_price": "44978.5", "order_qty": "0.06778960", "timestamp": "2024-01-08T12:26:41.229379178Z"},
      {"order_id": "OFO525-PHRVS-236RMN", "limit_price": "44979.2", "order_qty": "0.35630000", "timestamp": "2024-01-08T12:26:20.271584488Z"}
    ]
  }]
}
```

Asks string (low → high, order by order within each level):

```text theme={null}
44939545230839344939511126144939510000044939510000004495001033492644953064537449550250000449596356300004495963563000044960133807244960288967575449670314392283449785677896044979235630000
```

Bids string (high → low, order by order within each level):

```text theme={null}
449394889686994493944521000044939410000000449394142963234493942500000044939410292988449394338800004493941281408604493713346877449347356300004493022273429944930210000004493025550000449302700000004493021500000044928010524044919633870000449195761000044912035630000449097669000044901988982
```

Concatenated input to CRC32:

```text theme={null}
44939545230839344939511126144939510000044939510000004495001033492644953064537449550250000449596356300004495963563000044960133807244960288967575449670314392283449785677896044979235630000449394889686994493944521000044939410000000449394142963234493942500000044939410292988449394338800004493941281408604493713346877449347356300004493022273429944930210000004493025550000449302700000004493021500000044928010524044919633870000449195761000044912035630000449097669000044901988982
```

Expected result: **`1063832831`**
