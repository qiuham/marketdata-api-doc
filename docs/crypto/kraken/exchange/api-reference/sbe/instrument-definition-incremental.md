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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/instrument-definition-incremental'
updated_at: 2026-11-13
---

# InstrumentDefinitionIncremental

> Market data schema, template 7

SBE
schema 36 · market data
template 7

One instrument addition, modification or deletion.

Each message carries exactly one instrument, with no repeating group. `instrumentDefinitionSeq` is global to the instrument definition feed and advances once per message, including Add, Modify and Delete. It is not a per-instrument sequence.

* **Add** and **Modify** carry the full replacement definition.
* **Delete**: process `instrumentDefinitionSeq` for gap detection, as for every message, and use `instrumentId` and `instrumentUpdateAction`. Ignore the remaining definition fields: required numeric fields are zero, `minPrice`, `maxPrice` and `variation` are null, and `symbol` may be empty.

> [!NOTE]
>
> `contractMultiplier`, `currency`, `underlyingSymbol`, `description`, `productType`, `marketSector` and `maturityType` are not part of this message. See [Instrument definitions](https://docs.kraken.com/exchange/api-reference/sbe.md#instrument-definitions).

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `instrumentDefinitionSeq` | `uint64` | field | required | Contiguous instrument-definition feed sequence, starting at one |
| 2 | `instrumentId` | [`InstrumentId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumentid) | field | required | |
| 3 | `priceScale` | [`Scale`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#scale) | field | required | |
| 4 | `qtyScale` | [`Scale`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#scale) | field | required | |
| 5 | `tickSize` | [`Price`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#price) | field | required | Minimum valid price increment |
| 6 | `qtyIncrement` | [`Quantity`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#quantity) | field | required | Smallest valid quantity step |
| 7 | `maxTradeVol` | [`Quantity`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#quantity) | field | required | Largest quantity accepted for one order, or zero when no public limit is configured |
| 8 | `instrumentUpdateAction` | [`InstrumentUpdateAction`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumentupdateaction) | field | required | |
| 9 | `minPrice` | [`OptionalPrice`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#optionalprice) | field | required | Inclusive absolute minimum permitted order price, null when unavailable |
| 10 | `maxPrice` | [`OptionalPrice`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#optionalprice) | field | required | Inclusive absolute maximum permitted order price, null when unavailable |
| 11 | `variation` | [`OptionalPrice`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#optionalprice) | field | required | Non-negative absolute price-band offset, not a percentage, null when unavailable |
| 12 | `symbol` | [`SymbolEncoding`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#symbolencoding) | var data | required | External instrument symbol, at most 128 UTF-8 bytes. Empty only for Delete. |

`minPrice`, `maxPrice` and `variation` are null when their `exponent` is `127`. Ignore the mantissa in that case. See [Price controls](https://docs.kraken.com/exchange/api-reference/sbe.md#price-controls).

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md#messageheader).
