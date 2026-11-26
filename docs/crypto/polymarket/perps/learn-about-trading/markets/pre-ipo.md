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
source_url: 'https://docs.polymarket.com/perps/learn-about-trading/markets/pre-ipo'
updated_at: 2026-11-26
---

# Pre-IPO Perps: Asset Specifications

> Pricing, market specifications, and the transition from company valuation to per-share pricing.

This page covers how Polymarket’s Pre-IPO perpetuals work and lists the current specifications for each market.

> [!NOTE]
>
> Dates and figures on this page are estimates. Listing dates can move, and
> figures taken from company filings, such as valuations, share counts and
> rebase ratios, can be amended. They are shown to explain how each contract is
> priced, not as a view on what a company is worth.

## Overview

Pre-IPO perpetuals are cash-settled, non-expiring contracts that let you trade a private company’s value 24/7. They confer no equity, voting rights, dividends or IPO allocation.

Each market moves through three stages:

| Stage | How it is priced | Price source |
| - | - | - |
| **Launch to rebase** | On company valuation, where \$1 of price equals \$1B of fully diluted valuation. | A third-party pre-IPO valuation oracle. |
| **Rebase to IPO** | Per share, where one contract references one share. | Pyth’s per-share feed for the company. |
| **After the IPO** | On the listed share price. | The same Pyth feed, with the exchange price as its leading input. |

We rebase a market once the company publicly files its S-1 with a fully diluted share count, typically a few days before listing. We coordinate the timing with market makers and announce the date and ratio to traders in advance. Open positions are converted automatically, and nothing is closed.

## Specifications

The specifications below cover each market before and after its rebase.

| Market | Status | Description | Quote Unit | Collateral | Trading Hours | Price / Size Precision | Oracle | Oracle Bounds | Funding | Margin Mode | Max Leverage | Maint. Margin | Listing Event | Listing Date | Rebase | No-IPO Resolution Date |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| **ANT** (`ANT-USD`) | Live since Oct 29, 2026; listed on Nasdaq Nov 19, 2026 | ANT references 1 share of Anthropic, PBC Class A common stock (Nasdaq: ANT), quoted in USD and priced from Pyth. Anthropic builds frontier AI models and Claude. | USD per share (1 contract = 1 share) | pUSD | 24/7 | 0.001 price tick; 0.001 size step; \$10 min notional | Pyth Pro `Equity.Index.ANT/USD` ([3618](https://app.pyth.com/explore/Equity.Index.ANT%2FUSD)), per-share, 24/7. Based on 18,012,993,379 fully diluted shares (S-1/A-2). Index and Mark both reference this feed | None (valuation bounds removed at rebase) | Standard non-crypto (0.5 scale) against the Pyth Index; hourly, ±4%/hr cap | Cross & Isolated | 10x to \$500K; 5x to \$1M; 3x to \$3M; 2x to \$5M; 1x above \$5M | 5% | Nasdaq Global Select IPO | Nov 19, 2026 | Tues Nov 17, 2026, 10:00am ET. 18.012993379-for-1 (18,012,993,379 fully diluted shares ÷ 1B): size × ratio, entry ÷ ratio | N/A (listed) |

## Pre-IPO Pricing

Until its rebase, a market is priced as follows.

| Component | How It Works |
| - | - |
| Index | The Index comes from the market’s pre-IPO oracle and updates every 200 ms. |
| Mark | The Mark is the median of the basis-adjusted Index, our order book, and the oracle provider’s mark. It drives PnL, margin, liquidations and TP/SL triggers. See [Mark price](https://docs.polymarket.com/perps/learn-about-trading/mark-price.md). |
| Funding | Polymarket’s standard funding applies against the Index. It is paid hourly and capped as shown in the table. See [Funding](https://docs.polymarket.com/perps/learn-about-trading/funding.md). |
| Oracle bounds | These are the oracle provider’s catastrophic bounds. They should not bind in normal conditions and are removed at the rebase. |

If the oracle provider changes its methodology before our planned rebase, we may move the rebase earlier and will give as much notice as possible.

## The Rebase

At the rebase, we split the existing market so that one contract references one share, and switch pricing to Pyth. The market is not delisted, and you don’t need to do anything. The ratio is the fully diluted share count divided by 1 billion.

| Kept and converted | Cancelled and not restored |
| - | - |
| Positions: size is multiplied by the ratio and entry price is divided by it. | Resting limit orders. |
| Liquidation prices, rescaled to the new units. | TP/SL, trailing stops and other triggers. |
| Leverage, margin mode and isolated margin. | TWAP and chase orders. |
| Funding already paid. | Pending margin-removal requests. |
| Position value and PnL. No fee is charged and no PnL is realized. | |

**Example:** at a ratio of 18, a position of 10 contracts at 1,350 becomes 180 contracts at 75, with the same \$13,500 notional.

**Good to know**

* Rounding of less than one lot per position goes to the insurance fund.
* Each converted position gets a “split adjustment” row in Trade History.
* Charts show price history in per-share terms, while past trades keep their original prices.
* Any gap between the last pre-IPO price and Pyth’s first price is a real price move.
* Tick size and order size limits are updated for the new price.
* Implied market cap is based on fully diluted shares, so it may differ from figures shown by data providers.

### Trading Pause

The pause is expected to last around 15 minutes. Other markets trade normally throughout.

| Phase | What you can do | Funding |
| - | - | - |
| **Paused** | Trading stops, open orders are cancelled and positions are converted. You can deposit and add margin, but cannot withdraw or remove margin. | Stops |
| **Reopening** (5+ min) | Only post-only limit orders are accepted (API: `po=true`), and no fills take place. | Paused |
| **Live** | All order types are accepted. Re-set any TP/SL or other orders you still want. | Resumes, with no catch-up charge |

The market goes Live once both sides of the book are quoted within our spread and depth thresholds. Emergency takeover and auto-deleveraging can still occur during the pause under normal rules.

### After the IPO

* **No second switch.** Pyth’s feed uses the listed price as its leading input, and the market continues as a standard equity perpetual.
* **Final share count.** If the final count differs from the one used for the rebase, the contract is unaffected, since it already references one share.
* **Market makers.** Pre-IPO oracle providers may keep their own markets in valuation units, so apply the rebase ratio when hedging across venues.
* **Delayed or withdrawn IPO.** The market keeps trading per share. If the share count changes, we will announce how the market is handled in advance. If the company is still unlisted at the No-IPO Resolution Date, the market settles under its No-IPO terms.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
