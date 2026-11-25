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
source_url: 'https://docs.polymarket.com/perps/learn-about-trading/markets/compute'
updated_at: 2026-11-25
---

# Compute Perps: Asset Specifications

> Pricing, trading parameters, and settlement for GPU rental-price perpetuals.

This page covers how Polymarket’s compute perpetuals work and lists the current specifications for each market.

> [!NOTE]
>
> Figures on this page are subject to change before launch. Index values come
> from a third-party data provider and can be corrected by that provider. They
> are shown to explain how each contract is priced, not as a view on future
> compute prices.

## Overview

Compute perpetuals are cash-settled, non-expiring contracts that let you trade the rental price of AI compute 24/7. Each contract tracks a GPU rental price index, quoted in USD per GPU-hour. They confer no right to, or obligation for, any compute capacity, and nothing is delivered.

| Component | How it works | Source |
| - | - | - |
| **Index** | The planned 24-hour average of the provider’s hourly rental price for the GPU, recalculated as each new hourly print arrives. All 24 prints must be consecutive hourly prints. If any hour is missing or a print is not hourly, the update is skipped and the last value remains in use until the staleness limit. | Ornn GPU price index, polled every 60 seconds. |
| **Mark** | The median of the smoothed book mid, local book activity and the Index. There is no Ornn mark feed, so the external mark input falls back to the Index. It drives PnL, margin, liquidations and TP/SL triggers. | Polymarket order book and the Index. See [Mark price](https://docs.polymarket.com/perps/learn-about-trading/mark-price.md). |
| **Funding** | Polymarket’s standard non-crypto funding against the Index, paid hourly. | See [Funding](https://docs.polymarket.com/perps/learn-about-trading/funding.md). |

### Why a 24-Hour Average?

Hourly GPU rental prints are noisy: on H100, single hours have moved more than 20% while the daily level stayed flat. Pricing on the average of the latest 24 consecutive hourly prints removes that intraday noise while still following the real rental price. The average is time-stamped with its newest hourly print.

## Specifications

| Market | Status | Description | Quote Unit | Collateral | Trading Hours | Price / Size Precision | Oracle | Oracle Staleness | Funding | Margin Mode | Max Leverage | Maint. Margin | Liquidation Fee | Max Open Orders |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| **H100** (`H100-USD`) | Created on production (disabled); launch date TBD in November | H100 tracks the rental price of one NVIDIA H100 SXM GPU for one hour, quoted in USD and priced from Ornn’s H100 SXM index. | USD per GPU-hour (1 contract = 1 H100 SXM GPU-hour) | pUSD | 24/7 | 0.001 price tick; 0.001 size step; \$10 min notional | Ornn H100 SXM, planned 24-hour average: mean of the latest 24 consecutive hourly prints, polled every 60 s. The production feed is not yet attached; staging still uses the raw hourly print. Index only; the Mark is derived from it. | Index stops updating if the newest hourly print is more than 120 min old | Standard non-crypto (0.5 scale) against the Index; hourly, ±4%/hr cap | Cross & Isolated | 3x up to \$500k; 2x from \$500k to \$1M; 1x above \$1M | 16.67%, 25%, and 50% respectively, applied incrementally across notional tiers | 0.5% as of Nov 23; 0.1% planned for Nov 25 | 200 |

**Order caps:** Maximum market order: \$50k notional. Maximum limit order: \$250k notional.

## Settlement

| Component | How It Works |
| - | - |
| Cash settlement | All PnL, fees and funding settle in pUSD. There is no expiry and no delivery of compute. |
| PnL | Unrealized PnL is marked to the Mark price. PnL is realized in pUSD when a position is reduced or closed. |
| Funding | Premium is sampled every 5 seconds and settled against every open position at the end of each hour. Payments go directly between longs and shorts; Polymarket takes no cut. |
| Liquidation | Positions are liquidated when account equity falls below maintenance margin, measured at the Mark. See [Liquidation](https://docs.polymarket.com/perps/learn-about-trading/liquidation-mechanics.md). |
| Index outage | If Ornn stops publishing, the last 24-hour average stays in use until its newest hourly print is 120 minutes old. After that the Index freezes at its last value. Positions are not closed. Whether a stalled Index causes risk-increasing orders to be rejected remains to be tested in staging. |
| Index corrections | If Ornn corrects a published hourly print, the corrected value is used from the next poll. Past trades, funding and liquidations are not revised. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
