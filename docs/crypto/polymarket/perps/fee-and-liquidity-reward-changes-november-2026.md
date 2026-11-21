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
source_url: 'https://docs.polymarket.com/perps/fee-and-liquidity-reward-changes-november-2026'
updated_at: 2026-11-21
---

# Upcoming Fee and Liquidity Reward Changes

> Prepare for the Polymarket Perps trading fee, liquidation fee, and liquidity reward changes scheduled for November 25, 2026.

> [!NOTE]
>
> **Scheduled for November 25, 2026.** These changes apply to Polymarket Perps.
> The current fee and liquidity reward rules remain in effect until the changes
> go live.

## Trading Fees

Trading fees will keep the same trailing 30-day volume thresholds. The standard
rates below will apply when the changes go live.

| 30-Day Volume ≥ | Taker | Maker |
| - | - | - |
| \$0 | 0.0500% | 0.0200% |
| \$1M | 0.0400% | 0.0200% |
| \$5M | 0.0350% | 0.0100% |
| \$25M | 0.0300% | 0.0050% |
| \$100M | 0.0270% | 0.0020% |
| \$500M | 0.0250% | -0.0050% |
| \$1B | 0.0200% | -0.0100% |

For accounts in the lower 30-day volume tiers:

* **Below \$1M:** taker fees will increase from 0.0400% to 0.0500%, and maker
  fees from 0.0125% to 0.0200%.
* **\$1M to below \$5M:** taker fees will increase from 0.0370% to 0.0400%,
  and maker fees from 0.0100% to 0.0200%.
* **\$5M to below \$25M:** maker fees will increase from 0.0080% to 0.0100%.
  Taker fees will remain at 0.0350%.

A negative maker fee is a rebate. At the \$500M threshold, makers will earn a
0.5 bps rebate. At \$1B, the maker rebate will increase from 0.5 to 1 bp.
Rates at the \$25M and \$100M thresholds will remain unchanged.

Fees will continue to be calculated in pUSD on the notional value of each fill:

```text theme={null}
Fee = abs(Price * Quantity) * Rate
```

Fee tiers are re-evaluated every UTC day. Builder fees remain separate from
this schedule. Account- or market-specific fee overrides may apply; read your
effective rates from
[Trading Fees](https://docs.polymarket.com/perps/trading.md#trading-fees).

## Liquidation Fee

The liquidation fee will increase from **0.50% to 1.00% of liquidated notional**
(50 to 100 bps), in addition to the account's ordinary maker or taker fee.
100% of liquidation fees will be routed to bolster the Perps insurance fund.

## Liquidity Rewards

Liquidity Rewards 2.0 will replace the current \$75,000 daily program with fixed
daily pools on 69 markets. Each firm will receive one score per market,
combining its declared and linked accounts. An account that is not grouped
with others will be scored independently.

Before launch, give your Polymarket representative a complete list of the
accounts and sub-accounts your firm uses to quote. No application is required
to participate.

The asset tiers below classify markets for liquidity rewards. They are
separate from the trading-volume tiers used to determine fees.

### Daily Pools

| Market Group | Markets | Daily Pool per Market |
| - | -: | -: |
| Core markets | 23 | \$325 |
| ANT | 1 | \$3,000 |
| Asset Tier 1 and Tier 4 markets | 21 | No pool |

ANT's \$3,000 daily pool will run through **November 30, 2026**. Tier 4 markets
will remain listed and may be included in separate campaigns.

> [accordion] Markets by Pool, Asset Tier, and Cap Class
>
> The cap class identifies the per-side book caps used in scoring. RWA means
> real-world assets. Both distance-band caps for each class are listed under
> [Book-Level Size Caps](#scoring).
>
> | Daily Pool | Asset Tier | Cap Class | Markets |
> | - | - | - | - |
> | \$325 | 3 | Tier 3 crypto | 1000PEPE, 1000SHIB, AAVE, ADA, ARB, DOGE, ENA, FARTCOIN, JUP, LDO, LIT, LTC, ONDO, TAO, UNI, VVV, XMR, ZRO |
> | \$325 | 3 | Tier 3 RWA | BABA, CBRS, CRWV, MRVL, SOXL |
> | \$100 | 2 | Tier 2 crypto | BNB, HYPE, SOL, XRP |
> | \$100 | 2 | Tier 2 RWA | AAPL, AMD, AMZN, AVGO, BRENTOIL, CL, CRCL, DRAM, GOOGL, HOOD, INTC, LITE, META, MSFT, MSTR, MU, NBIS, NVDA, ORCL, PLTR, RKLB, SKHX, SKHY, SNDK, SPCX, TSLA, TSM |
> | \$100 | 3 | Tier 3 crypto | AVAX, LINK, NEAR, PUMP, SUI, WLD, XPL, ZEC |
> | \$100 | 3 | Tier 3 RWA | ARM, ASML, COIN, EWY, QCOM, SMSN |
> | \$3,000 | ANT | ANT | ANT |
> | No pool | 1 | Not applicable | BTC, ETH, GOLD, NAS100, SILVER, SP500 |
> | No pool | 4 | Not applicable | CASHCAT, CXMT, DELL, ETHFI, KAITO, MORPHO, NCLD, PENDLE, PONS, PRL, STRC, UNITREE, USELESS, VIRTUAL, ZM |

### Maker-Share Requirement

To qualify for rewards in a market, a firm's combined maker volume across all
markets in that asset tier must represent at least **1% of the tier's total
maker volume over the trailing seven days**. ANT will have a separate
calculation using ANT volume only. Maker share will determine eligibility;
it will not multiply the reward score.

The calculation will include fills against all takers except the firm's own
accounts, sub-accounts, linked accounts, and mirrored pairs.

### Quoting Requirements

The order book will be sampled throughout each reward period. Each sample is
a snapshot. Quoted notional is order price multiplied by quantity.

The reference midpoint will be the average of the highest bid and lowest ask
price levels that each contain at least \$1,000 in aggregate resting order
notional. The \$1,000 minimum applies to each price level separately, rather
than cumulative depth across levels. Distances in the table below are measured
from this midpoint.

| Requirement | Asset Tier 2 | Asset Tier 3 | ANT |
| - | - | - | - |
| Minimum quoted notional per side | \$5,000 within 10 bps | \$1,000 within 10 bps | \$1,000 within 50 bps |
| Minimum uptime | 70% of snapshots | 50% of snapshots | 50% of snapshots |

ANT will use Asset Tier 3 scoring weights, with its minimum-size requirement
measured within 50 bps instead of 10 bps.

Uptime is the percentage of snapshots meeting the minimum quoted notional on
both sides. It will use a trailing seven-day lookback, starting no earlier
than the new program's launch or the market's listing. Minimum quoted notional
will be measured before the book-level caps below are applied.

### Scoring

A firm's snapshot will score zero unless it meets the minimum quoted notional
on both sides. Qualifying resting notional will be weighted by its distance from the
reference midpoint, after applying the book-level caps.

> [accordion] Book-Level Size Caps
>
> The current \$100,000 cap per account, side, and distance band will be
> replaced by a cap shared across eligible firms in each market. The cap will
> apply separately to each side and to two distance groups: within 10 bps,
> and more than 10 bps through 50 bps. The market list above identifies each
> market's cap class.
>
> | Cap Class | Within 10 bps per Side | More Than 10 bps Through 50 bps per Side |
> | - | -: | -: |
> | Tier 2 crypto | \$130,000 | \$120,000 |
> | Tier 2 RWA | \$200,000 | \$200,000 |
> | Tier 3 crypto | \$25,000 | \$45,000 |
> | Tier 3 RWA | \$15,000 | \$55,000 |
> | ANT | \$30,000 | \$110,000 |
>
> If eligible firms' combined size exceeds a cap, their credited size in that
> side and distance group will be reduced proportionally before the scoring
> weights are applied.
>
> Their quoted notional counts toward the cap even in snapshots where they fail the minimum two-sided
> size requirement.

The scoring weights will be:

| Distance From Midpoint | Asset Tier 2 Weight | Asset Tier 3 and ANT Weight |
| - | -: | -: |
| Within 5 bps | 1.00 | 1.00 |
| More than 5 bps and within 10 bps | 0.50 | 0.60 |
| More than 10 bps and within 20 bps | 0.25 | 0.40 |
| More than 20 bps and within 50 bps | 0.10 | 0.20 |
| Beyond 50 bps | 0 | 0 |

Each snapshot's score will use the smaller of the firm's weighted bid and ask
sizes:

```text theme={null}
snapshot_score = 2 × min(weighted_bid, weighted_ask)
```

A firm's daily score will be the average of all its snapshot scores during
the reward period. Snapshots with no quotes will count as zero. Eligible firms
will receive a share of each market's daily pool proportional to their daily
scores. This replaces the current maker-score formula.

Reward periods will remain 12:00 UTC to 12:00 UTC. Rewards will be scored and
accrued daily, with **weekly payouts in pUSD**. Open-interest rewards will not
be part of this program.

### Account Disclosure

Polymarket will combine accounts it identifies as linked and score them as one
firm

Polymarket may change program parameters or disqualify activity that is
manipulative, abusive, or violates the Terms of Service.

Until the changes take effect, refer to the current
[Fees](https://docs.polymarket.com/perps/learn-about-trading/fees.md),
[Liquidation Mechanics](https://docs.polymarket.com/perps/learn-about-trading/liquidation-mechanics.md), and
[Liquidity Rewards](https://docs.polymarket.com/perps/liquidity-rewards.md) pages.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
