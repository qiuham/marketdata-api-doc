---
exchange: kraken
source_url: https://docs.kraken.com/exchange/api-reference/sbe/instrument-status-incremental
api_type: SBE
updated_at: 2026-11-18 01:44:53.829914
---

# InstrumentStatusIncremental

> Market data schema, template 5

SBE
schema 36 · market data
template 5

A live change to an instrument's trading status.

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `instrumentId` | [`InstrumentId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumentid) | field | required | |
| 2 | `instrumentStatus` | [`InstrumentTradingStatus`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumenttradingstatus) | field | required | |
| 3 | `instrumentStatusSeq` | `uint64` | field | required | Contiguous per-instrument status sequence, starting at one |
| 4 | `reason` | [`StatusReasonEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#statusreasonencoding) | var data | required | Human-readable reason for this status update, empty when no reason was supplied |

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md#messageheader).