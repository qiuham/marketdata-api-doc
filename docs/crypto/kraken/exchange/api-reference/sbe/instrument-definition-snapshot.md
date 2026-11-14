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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/instrument-definition-snapshot'
updated_at: 2026-11-13
---

# InstrumentDefinitionSnapshot

> Market data schema, template 1

SBE
schema 36 · market data
template 1

One instrument definition within a snapshot cycle, including the instrument's trading status.

> [!NOTE]
>
> `contractMultiplier`, `currency`, `underlyingSymbol`, `description`, `productType`, `marketSector` and `maturityType` are not part of this message. See [Instrument definitions](https://docs.kraken.com/exchange/api-reference/sbe.md#instrument-definitions).

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `instrumentId` | [`InstrumentId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumentid) | field | required | |
| 2 | `lastInstrumentDefinitionSeqProcessed` | `uint64` | field | required | Last InstrumentDefinitionIncremental instrumentDefinitionSeq included, or zero if no update has been published |
| 3 | `lastInstrumentStatusSeqProcessed` | `uint64` | field | required | Last InstrumentStatusIncremental instrumentStatusSeq reflected in instrumentStatus for this instrument, or zero if no update has been published |
| 4 | `instrumentNumber` | `uint32` | field | required | One-based position of this instrument in the serialized snapshot response |
| 5 | `totalInstruments` | `uint32` | field | required | Total number of instruments in this snapshot cycle |
| 6 | `priceScale` | [`Scale`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#scale) | field | required | |
| 7 | `qtyScale` | [`Scale`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#scale) | field | required | |
| 8 | `tickSize` | [`Price`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#price) | field | required | Minimum valid price increment |
| 9 | `qtyIncrement` | [`Quantity`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#quantity) | field | required | Smallest valid quantity step |
| 10 | `maxTradeVol` | [`Quantity`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#quantity) | field | required | Largest quantity accepted for one order, or zero when no public limit is configured |
| 11 | `instrumentStatus` | [`InstrumentTradingStatus`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumenttradingstatus) | field | required | Trading status at lastInstrumentStatusSeqProcessed |
| 12 | `minPrice` | [`OptionalPrice`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#optionalprice) | field | required | Inclusive absolute minimum permitted order price. Null when unavailable. |
| 13 | `maxPrice` | [`OptionalPrice`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#optionalprice) | field | required | Inclusive absolute maximum permitted order price. Null when unavailable. |
| 14 | `variation` | [`OptionalPrice`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#optionalprice) | field | required | Non-negative absolute price-band offset from the selected reference, not a percentage. Null when unavailable. |
| 16 | `symbol` | [`SymbolEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#symbolencoding) | var data | required | External instrument symbol, at most 128 UTF-8 bytes |
| 15 | `instrumentStatusReason` | [`StatusReasonEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#statusreasonencoding) | var data | required | Human-readable reason for instrumentStatus, empty when no reason was supplied |

`minPrice`, `maxPrice` and `variation` are null when their `exponent` is `127`. Ignore the mantissa in that case. See [Price controls](https://docs.kraken.com/exchange/api-reference/sbe.md#price-controls).

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md#messageheader).
