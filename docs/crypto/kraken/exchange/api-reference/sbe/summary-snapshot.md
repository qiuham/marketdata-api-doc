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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/summary-snapshot'
updated_at: 2026-11-13
---

# SummarySnapshot

> Market data schema, template 11

SBE
schema 36 · market data
template 11

The complete current summary for exactly one instrument at `lastSummarySeqProcessed`. A snapshot response contains one message per instrument.

`summaryNumber` is the position of this message in the complete response, from one through `totalSummaries`. The response is complete once every number has arrived. An unavailable price is still a valid row, with a null `referencePrice`.

See [Instrument summaries](https://docs.kraken.com/exchange/api-reference/sbe.md#instrument-summaries).

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `instrumentId` | [`InstrumentId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumentid) | field | required | |
| 2 | `lastSummarySeqProcessed` | `uint64` | field | required | Last summarySeq included for this instrument, or zero before any summary update. |
| 3 | `referencePrice` | [`OptionalPrice`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#optionalprice) | field | required | Current reference price accepted by ME. Null when no value is retained. |
| 4 | `referencePriceTime` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#timestampns) | field | required | Producer timestamp of the retained reference price or clear. Zero when unavailable. |
| 5 | `summaryNumber` | `uint32` | field | required | Position of this instrument's message in the complete snapshot response, starting at one. |
| 6 | `totalSummaries` | `uint32` | field | required | Total number of single-instrument summary messages in this snapshot response. |

`referencePrice` is null when its `exponent` is `127`. Ignore the mantissa in that case.

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md#messageheader).
