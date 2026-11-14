---
api_type: reference
source_type: llms_txt
version: ''
scope: crypto
asset_class: prediction_market
domain: exchanges
provider: polymarket
provider_name: Polymarket
product: api
product_id: polymarket
source_url: 'https://docs.polymarket.com/perps/learn-about-trading/markets'
updated_at: 2026-11-13
---

# Markets

> Listed perpetual markets and trading parameters

Polymarket Perps markets track underlying assets across indices, commodities,
crypto assets, and equities. Each market has its own trading parameters.

## Instruments

Perps markets are represented by instruments, which are the listed perpetual
contracts available to trade.

Each instrument also includes details that shape how it trades:

* Underlying asset
* Collateral and quote asset
* Price and quantity precision
* Tick size
* Minimum order size
* Risk tiers and leverage caps
* Mark, index, and funding configuration

> [!NOTE]
>
> Market parameters can change as markets evolve. Builders should read live
> instrument details from [Market Data](https://docs.polymarket.com/perps/market-data.md#fetch-instruments)
> before submitting orders.

## Price Feeds

Each market tracks an underlying market through external price feeds. Those
feeds drive the [Index Price](https://docs.polymarket.com/perps/learn-about-trading/index-price.md), and the Index Price helps anchor the [Mark Price](https://docs.polymarket.com/perps/learn-about-trading/mark-price.md).

## Pre-IPO Markets

Pre-IPO perpetuals track a private company's valuation before it lists. Each
pre-IPO market has its own specification page covering its price sources,
contract terms, and what happens when the company goes public.

> [card] [Anthropic (ANT)](https://docs.polymarket.com/perps/learn-about-trading/markets/pre-ipo-anthropic.md)
>
> Specifications and the November 16 rebase to a per-share market.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
