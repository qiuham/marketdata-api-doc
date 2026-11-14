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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/trade-incremental'
updated_at: 2026-11-13
---

# TradeIncremental

> Market data schema, template 3

SBE
schema 36 · market data
template 3

One trade on an instrument.

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `instrumentId` | [`InstrumentId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#instrumentid) | field | required | |
| 2 | `transactTime` | [`TimestampNs`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#timestampns) | field | required | Time the trade occurred at the source |
| 4 | `tradeSeq` | `uint64` | field | required | Contiguous per-instrument trade sequence, starting at one |
| 5 | `tradeId` | [`TradeId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#tradeid) | field | required | |
| 6 | `orderId` | [`OrderId`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#orderid) | field | required | Aggressor order ID for this trade |
| 7 | `price` | [`Price`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#price) | field | required | |
| 8 | `quantity` | [`Quantity`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#quantity) | field | required | |
| 9 | `aggressorSide` | [`AggressorSide`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#aggressorside) | field | optional | |
| 10 | `ordType` | [`OrdTypeMD`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#ordtypemd) | field | optional | |

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md#messageheader).
