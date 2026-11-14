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
source_url: 'https://docs.kraken.com/exchange/api-reference/sbe/trading-session-status-incremental'
updated_at: 2026-11-13
---

# TradingSessionStatusIncremental

> Market data schema, template 6

SBE
schema 36 · market data
template 6

A change to the trading session status.

> [!NOTE]
>
> **Spot and Futures only.** US Perps does not expose a global trading session status. For US Perps the status is provided per instrument: use the `InstrumentStatus` feed, and the status carried by each `InstrumentDefinition`.

**Direction:** Kraken → client

| ID | Field | Type | Encoding | Presence | Description |
| :- | :- | :- | :- | :- | :- |
| 1 | `tradingSessionStatus` | [`TradingSessionStatusCode`](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types#tradingsessionstatuscode) | field | required | |
| 2 | `tradingSessionSeq` | `uint64` | field | required | Contiguous trading-session status sequence, starting at one |

Every message is preceded by the standard SBE `messageHeader` (`blockLength`, `templateId`, `schemaId`, `version`). See [encodings](https://docs.kraken.com/exchange/api-reference/sbe/market-data-types.md#messageheader).
