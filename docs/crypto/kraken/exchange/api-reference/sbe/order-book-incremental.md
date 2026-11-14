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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/order-book-incremental'
updated_at: 2026-11-13
---

# OrderBookIncremental

> Market data schema, template 2

SBE
schema 36 · market data
template 2

Order-by-order (L3) book updates for one instrument.

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `instrumentId` | [`InstrumentId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumentid) | field | required | |
| 2 | `orderBookSeq` | `uint64` | field | required | Contiguous per-instrument update sequence, starting at one |
| 3 | `transactTime` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#timestampns) | field | required | Time the matching event occurred at the source |
| 4 | `orders` | group | group | required | |
| 1 |   ↳ `updateAction` | [`OrderUpdateAction`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#orderupdateaction) | group field | required | |
| 2 |   ↳ `side` | [`Side`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#side) | group field | required | |
| 3 |   ↳ `orderId` | [`OrderId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#orderid) | group field | required | |
| 4 |   ↳ `price` | [`Price`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#price) | group field | required | |
| 5 |   ↳ `quantity` | [`Quantity`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#quantity) | group field | required | |
| 6 |   ↳ `orderPriority` | `uint64` | group field | required | Opaque queue priority comparable within one price level |

Rows marked ↳ are fields of the repeating group above them. Each group is preceded by a `groupSizeEncoding` header (`blockLength`, `numInGroup`).

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md#messageheader).
