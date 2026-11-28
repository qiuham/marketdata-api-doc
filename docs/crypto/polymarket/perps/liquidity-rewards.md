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
source_url: 'https://docs.polymarket.com/perps/liquidity-rewards'
updated_at: 2026-11-28
---

# Liquidity Rewards

> Earn pUSD rewards by providing deep, two-sided liquidity on Perps, and earn taker rewards on new pre-IPO listings

Every Perps account is automatically considered for daily liquidity rewards.
There is no application or participant allowlist: the same eligibility threshold
and scoring rules apply to every maker.

Rewards are scored and accrued daily for 24-hour periods from 12:00 UTC to
12:00 UTC. Each period is labeled by its end date. Rewards are paid weekly in
pUSD.

## How Rewards Are Allocated

The program uses fixed daily pools across 70 markets. Each firm receives one
score per market, combining its declared and linked accounts. An account that
is not grouped with others is scored independently.

| Market Group | Markets | Daily Pool per Market |
| - | -: | -: |
| Core markets | 23 | \$325 |
| Additional markets | 45 | \$100 |
| ANT | 1 | \$3,000 |
| Pre-IPO launch markets | 1 | Set per market |
| Asset Tier 1 and Tier 4 markets | 21 | No pool |

ANT's \$3,000 daily pool runs through **November 30, 2026**. Each pre-IPO launch
market has its own daily pool, shown under Pre-IPO Launch Markets, which runs
for the 7 reward periods shown there. Tier 4 markets remain listed and may be
included in separate campaigns.

### Pre-IPO Launch Markets

| Market | Listed | Reward Window (7 reward periods) | Daily Maker Pool | Daily Taker Pool |
| - | - | - | -: | -: |
| OPENAI | November 28, 2026 | 12:00 UTC Nov 28 – 12:00 UTC Dec 5, 2026 | \$3,000 | \$3,000 |

The asset tiers below classify markets for liquidity rewards. They are
separate from the trading-volume tiers used to determine fees.

> [accordion] Markets by Pool, Asset Tier, and Cap Class
>
> The cap class identifies the per-side book caps used in scoring. RWA means
> real-world assets. Both distance-band caps for each class are listed under
> [Book-Level Size Caps](#liquidity-score).
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
> | Set per market | Pre-IPO launch | Pre-IPO | OPENAI |
> | No pool | 1 | Not applicable | BTC, ETH, GOLD, NAS100, SILVER, SP500 |
> | No pool | 4 | Not applicable | CASHCAT, CXMT, DELL, ETHFI, KAITO, MORPHO, NCLD, PENDLE, PONS, PRL, STRC, UNITREE, USELESS, VIRTUAL, ZM |

A firm's reward is its share of the market's total daily score multiplied by
the market's daily pool. Open-interest rewards are not part of this program.

## Eligibility And Maker Share

To qualify for rewards in a market, a firm's combined maker volume across all
markets in that asset tier must represent at least **1% of the tier's total
maker volume over the trailing seven days**. ANT and each pre-IPO launch market
have a separate calculation using that market's volume only. Maker share
determines eligibility; it does not multiply the reward score.

Fills against the firm's own accounts, sub-accounts, linked accounts, and
mirrored pairs do not count toward maker share.

Give your Polymarket representative a complete list of the accounts and
sub-accounts your firm uses to quote. Polymarket combines accounts it identifies
as linked and scores them as one firm.

## Liquidity Score

The order book is sampled repeatedly throughout each reward period. Each
sample is a snapshot. Resting liquidity within 50 basis points of the reference
midpoint can score.

### Distance Tiers

| Distance From Midpoint | Asset Tier 2 Weight | Asset Tier 3, ANT and Pre-IPO Launch Weight |
| - | -: | -: |
| Within 5 bps | 1.00 | 1.00 |
| More than 5 bps and within 10 bps | 0.50 | 0.60 |
| More than 10 bps and within 20 bps | 0.25 | 0.40 |
| More than 20 bps and within 50 bps | 0.10 | 0.20 |
| Beyond 50 bps | 0 | 0 |

The reference midpoint is the average of the highest bid and lowest ask price
levels that each contain at least \$1,000 in aggregate resting order notional.
The \$1,000 minimum applies to each price level separately, rather than
cumulative depth across levels. Quoted notional is order price multiplied by
quantity.

> [accordion] Book-Level Size Caps
>
> Each market has a cap shared across eligible firms. The cap applies
> separately to each side and to two distance groups: within 10 bps, and more
> than 10 bps through 50 bps.
>
> | Cap Class | Within 10 bps per Side | More Than 10 bps Through 50 bps per Side |
> | - | -: | -: |
> | Tier 2 crypto | \$130,000 | \$120,000 |
> | Tier 2 RWA | \$200,000 | \$200,000 |
> | Tier 3 crypto | \$25,000 | \$45,000 |
> | Tier 3 RWA | \$15,000 | \$55,000 |
> | ANT | \$30,000 | \$110,000 |
> | Pre-IPO | \$30,000 | \$110,000 |
>
> If eligible firms' combined size exceeds a cap, their credited size in that
> side and distance group is reduced proportionally before the scoring weights
> are applied. Their quoted notional counts toward the cap even in snapshots
> where they fail the minimum two-sided size requirement.

### Two-Sided Liquidity

A snapshot scores only when the firm meets the minimum quoted notional on both
sides. The minimum is measured before the book-level caps are applied.

| Requirement | Asset Tier 2 | Asset Tier 3 | ANT and Pre-IPO Launch |
| - | - | - | - |
| Minimum quoted notional per side | \$5,000 within 10 bps | \$1,000 within 10 bps | \$1,000 within 50 bps |
| Minimum uptime | 70% of snapshots | 50% of snapshots | 50% of snapshots |

ANT and pre-IPO launch markets use Asset Tier 3 scoring weights, with their
minimum-size requirement measured within 50 bps instead of 10 bps.

Weighted bid and ask sizes are added separately, then combined using the
smaller side:

```text theme={null}
snapshot_score = 2 × min(weighted_bid, weighted_ask)
```

A snapshot scores zero if the minimum two-sided quoted notional is not met.

## Uptime

Uptime is the share of completed snapshots in which the firm meets the minimum
quoted notional on both sides:

```text theme={null}
uptime = qualifying_snapshots / completed_snapshots
```

It uses a trailing seven-day lookback, starting no earlier than the new
program's launch or the market's listing. Firms must meet the minimum uptime
for their market shown above.

A firm's daily score is the average of all its snapshot scores during the
reward period. Snapshots with no quotes count as zero.

## Summary Of Program Parameters

| Parameter | Value |
| - | - |
| Daily pools | Fixed pools across 70 markets |
| Reward period | 12:00 UTC to 12:00 UTC |
| Reward payouts | Weekly, in pUSD |
| Maker-share lookback | 7 days |
| Eligibility threshold | 1% maker share within the asset tier; ANT and each pre-IPO launch market measured separately |
| Minimum uptime | 70% for Asset Tier 2; 50% for Asset Tier 3, ANT and pre-IPO launch markets |
| Uptime lookback | 7 days, starting no earlier than program launch or market listing |
| Scoring bands | 5, 10, 20, and 50 bps |
| Band weights | Vary by asset tier; see Distance Tiers |
| Credited notional cap | Shared per market, side, and distance group; varies by cap class |
| Reference price | Midpoint of bid and ask price levels with at least \$1,000 each |
| Side combination | Twice the smaller weighted bid or ask size |

## Pre-IPO Launch Taker Rewards

Each pre-IPO launch market has its own fixed daily taker pool, shown in the
Pre-IPO Launch Markets table, for the 7 reward periods shown in that table.
Pool sizes can differ between markets. Every Perps account is automatically
considered. There is no application.

Taker rewards use the same 12:00 UTC to 12:00 UTC reward periods as liquidity
rewards and are paid weekly in pUSD.

### How Taker Rewards Are Allocated

An account's reward in a market is its share of that day's total eligible taker
volume in that market, multiplied by the market's daily pool, up to 5% of the
pool. Volume in one market does not count toward another market's pool.

```text theme={null}
daily_reward = min(account_volume / total_volume × daily_pool, 5% × daily_pool)
```

Amounts not paid out because of the cap are not redistributed.

### Taker Eligibility

An account qualifies in a market for a reward period when its eligible taker
volume in that market in that period is at least **\$1,000**. Linked accounts
are combined and scored as one account.

| Counts | Does not count |
| - | - |
| Taker fills in the market, by notional | Maker fills |
| Fills within the reward period | Liquidations |
| | Fills against your own, sub- or linked accounts |
| | Volume flagged as wash trading or self-trading |

### Taker Program Parameters

| Parameter | Value |
| - | - |
| Daily pool | Set per market; see Pre-IPO Launch Markets |
| Duration | 7 reward periods; dates per market in the Pre-IPO Launch Markets table |
| Reward period | 12:00 UTC to 12:00 UTC |
| Reward payouts | Weekly, in pUSD |
| Minimum to qualify | \$1,000 eligible taker volume per market per period |
| Max per account | 5% of the market's daily pool (for example, \$150 on a \$3,000 pool) |

> [!NOTE]
>
> Polymarket may change program parameters or disqualify activity that is
> manipulative, abusive, or otherwise violates the Terms of Service.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
