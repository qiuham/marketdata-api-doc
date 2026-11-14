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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/order-book-snapshot'
updated_at: 2026-11-13
---

# OrderBookSnapshot

> Market data schema, template 4

SBE
schema 36 · market data
template 4

One chunk of a full order-by-order (L3) book snapshot for an instrument.

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 2 | `instrumentId` | [`InstrumentId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumentid) | field | required | |
| 3 | `lastOrderBookSeqProcessed` | `uint64` | field | required | Last OrderBookIncremental orderBookSeq included, or zero if no update has been published |
| 4 | `chunkNumber` | `uint32` | field | required | One-based chunk number within this snapshot response |
| 5 | `totalChunks` | `uint32` | field | required | |
| 6 | `orders` | group | group | required | |
| 1 |   ↳ `side` | [`Side`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#side) | group field | required | |
| 2 |   ↳ `orderId` | [`OrderId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#orderid) | group field | required | |
| 3 |   ↳ `price` | [`Price`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#price) | group field | required | |
| 4 |   ↳ `quantity` | [`Quantity`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#quantity) | group field | required | |
| 5 |   ↳ `orderPriority` | `uint64` | group field | required | |

Rows marked ↳ are fields of the repeating group above them. Each group is preceded by a `groupSizeEncoding` header (`blockLength`, `numInGroup`).

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md#messageheader).
