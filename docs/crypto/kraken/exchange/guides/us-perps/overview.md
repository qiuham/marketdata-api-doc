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
source_url: 'https://docs.kraken.com/exchange/guides/us-perps/overview'
updated_at: 2026-11-13
---

# US Perps overview

> Kraken US Perps — perpetual futures on equities and crypto, with an initial focus on equity perpetuals

**Kraken US Perps** offers perpetual futures contracts on both **equities** and **crypto** assets, with an initial focus on equity perpetuals. Contracts have no expiry date, so a position can be held for as long as it remains open.

## Products

| | Equity Perps | Crypto Perps |
| :- | :- | :- |
| **Underlying** | Equities | Crypto assets |
| **Contract type** | Perpetual future | Perpetual future |
| **Status** | Initial focus | Covered by the same APIs |

### Equity Perps

Equity Perps give perpetual futures exposure to equities. Equity instruments can follow a scheduled trading session: outside it, an instrument reports the `Closed` trading status on the market data feed.

### Crypto Perps

Crypto Perps give perpetual futures exposure to crypto assets. They use the same order entry, market data and drop copy APIs as Equity Perps.

## Instruments

Every US Perps contract is described by an instrument definition on the market data feed, which includes its symbol, tick size, quantity increment, maximum trade volume, price controls and trading status. Ten contracts are listed at launch.

## Documentation

The complete US Perps documentation is available as a single PDF:

* [Kraken US Perps — consolidated documentation (PDF)](https://docs.kraken.com/exchange/api-reference/us-perps/doc-consolidated.pdf)

## Next steps

> [card] [API](https://docs.kraken.com/exchange/guides/us-perps/api.md)
>
> Order entry over FIX, market data over SBE, and drop copy over FIX.

> [card] [Connectivity](https://docs.kraken.com/exchange/guides/us-perps/connectivity.md)
>
> Connectivity and colocation guides.
