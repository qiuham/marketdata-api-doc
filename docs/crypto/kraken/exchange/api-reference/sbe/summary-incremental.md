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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/summary-incremental'
updated_at: 2026-11-13
---

# SummaryIncremental

> Market data schema, template 12

SBE
schema 36 · market data
template 12

The complete current summary for one instrument after an update.

Each message replaces the whole current summary, not only the fields that changed. Null does not mean unchanged: a null `referencePrice` clears the retained value, and zero is a real price. `referencePriceTime` belongs to the value or clear it is sent with.

See [Instrument summaries](https://docs.kraken.com/exchange/api-reference/sbe.md#instrument-summaries).

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `instrumentId` | [`InstrumentId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumentid) | field | required | |
| 2 | `summarySeq` | `uint64` | field | required | Contiguous sequence per instrument, starting at one and shared by all summary metrics. |
| 3 | `referencePrice` | [`OptionalPrice`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#optionalprice) | field | required | Current reference price accepted by ME. Null clears the retained value. |
| 4 | `referencePriceTime` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#timestampns) | field | required | Producer timestamp of the retained reference price or clear. Zero when unavailable. |

`referencePrice` is null when its `exponent` is `127`. Ignore the mantissa in that case.

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md#messageheader).
