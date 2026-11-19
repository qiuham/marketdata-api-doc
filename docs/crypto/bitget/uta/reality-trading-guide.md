---
exchange: bitget
source_url: https://www.bitget.com/docs/uta/reality-trading-guide
api_type: Guide
updated_at: 2026-11-19 19:07:14.377011
---

# rToken Trading Guide

## Overview

rToken refers to Bitget's tokenized US stock trading pairs, identified by symbols prefixed with `r` (e.g.,
`rAAPLUSDT`).

For more details about rToken, please refer to:

- [Introduction to the Reality Protocol and rToken Tokenization](https://www.bitget.com/academy/what-is-reality-protocol-and-rtokens-rwa-tokenization-defi-guide).
- [Bitget Stock Spot Trading FAQ: rTokens, Dividends, Fees, and Trading Hours](https://www.bitget.com/support/articles/12560603887176)
- [Transfer US Stocks to Bitget](https://www.bitget.com/support/articles/12560603897720)

## Order Routing & Matching Mechanism

rToken orders are matched through **Super Match**, an internal matching layer that sits between Bitget's
trading engine and the external broker (used to route unmatched order flow to the US stock market). Every rToken
spot order — regardless of whether the US market is open — is first evaluated by Super Match before any unmatched
quantity is routed externally.

### Order parameter `venue`: choosing where your order can match

The `venue` parameter (available on [Place Order](/docs/catalog/trading/order-management#place-order) and
[Place Reality Order](/docs/catalog/reality/trading#place-reality-order)) controls routing behavior:

| `venue` value           | Behavior                                                                                                                                       |
|:-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| Omitted (default strategy; order details return `default`) | Super Match first attempts to match the order internally at the best price. Any unmatched quantity is then routed to the external broker (lit market).<br/><u>For certain trading pairs that are tradable on weekends, resting orders still unmatched externally are moved back to the internal order book, and if they remain unmatched over the weekend, they are routed externally again to continue resting;</u> |
| `internal_market`       | The order only ever matches inside Super Match, Bitget's internal matching engine. It is never submitted to the US stock broker, is not affected by market open/close transitions, and does not participate in the weekend/Monday-pre-open batch re-routing of resting orders. |
| `lit_market`            | The order is submitted to the US stock broker for execution. During US market hours it is not matched within the exchange (Super Match); while the US market is closed (e.g. weekends) the broker is unavailable, so the order rests internally within the exchange and the unfilled portion is routed to the broker once the market reopens. |

The accepted `venue` values when placing an order are `internal_market` and `lit_market`; omitting `venue` applies the
default strategy. In order details (REST order queries and WebSocket order pushes), `venue` is returned as one of
`default` / `internal_market` / `lit_market`.

:::warning{title="venue enum adjustment (effective November 5, 2026)"}
- `internalization` is renamed to `internal_market` with no change in meaning. Please replace this enum value with `internal_market`.
- Orders previously shown as `lit_market` in order details (matched internally at the best price first, with any unfilled portion submitted to the broker) are now shown as `default`. Please update your order-detail parsing logic accordingly.
- The new `lit_market` means "orders are submitted to the broker for execution and are not matched within the exchange", which differs from the meaning of `lit_market` shown in order details before the adjustment. Please distinguish between the two carefully.
:::

**As a general guideline:**

- Use `internal_market` for quoting/market-making flow that you intend to keep entirely within Super Match.
- Omit `venue` (default strategy) for flow where you want internal price-compared matching first, with unmatched
  quantity also reaching the external broker (e.g., building or reducing inventory).
- Use `lit_market` for flow you want submitted directly to the US stock broker without internal matching.

Order validity is controlled separately via `rTokenTimeInForce`: `gtd` (valid for the current trading session) or
`gtc` (valid for 90 days). See the field descriptions on [Place Order](/docs/catalog/trading/order-management#place-order) and
[Place Reality Order](/docs/catalog/reality/trading#place-reality-order) for the exact session-boundary rules.

:::warning{title="Order modification is not supported"}
rToken orders cannot be modified. To change the price or quantity of a resting order, cancel it and place a new one.
:::

### When your resting order gets filled

Default strategy (`venue` omitted; order details return `default`)

During US market trading hours (pre-market, regular, after-hours, and overnight), Super Match determines whether your
resting limit order can be matched internally using a dynamic price band around the **NBBO** (National Best Bid and
Offer):

- **ΔP** is a per-order, real-time estimate of the additional slippage a retail order would incur if it were instead
  routed directly to the external broker. ΔP is calculated per order (not a fixed constant) and widens with the
  order's size relative to average daily volume, current volatility, the NBBO spread, and how thin external
  liquidity is at that moment. (ΔP is currently set to 0 and is subject to change in the future.)
- The **tradable price band** for internal matching is **[NBB − ΔP, NBO + ΔP]**:
  - A retail buy order can match against any resting internal sell (ask) order priced at or below `NBO + ΔP`.
  - A retail sell order can match against any resting internal buy (bid) order priced at or above `NBB − ΔP`.
- Matching within the band walks the book **level by level** (not only the best level) until the incoming order is
  filled or the band is exhausted. Any quantity that cannot be matched within the band is routed externally
  (subject to `venue`).
- **The execution price is your resting (quoted) price** — not the NBBO, and not the band boundary. If your resting
  ask is inside the band and gets hit, the retail taker pays your quoted price, not `NBO + ΔP`. This means the full
  spread captured between your quote and the NBBO accrues to you as the market maker.

Pre-market, after-hours, and overnight sessions are an intermediate case: the NBBO still exists, but external
liquidity is thin, so the internally tradable price range is effectively wider than during regular hours.

`venue` = `internal_market`

The order only ever matches inside Super Match, Bitget's internal matching engine. It is never forwarded to the
external broker, is not affected by market open/close transitions, does not participate in the weekend/Monday-pre-open
batch re-routing of resting orders, and is not subject to the NBBO price band.

`venue` = `lit_market`

The order is submitted to the US stock broker for execution. During US market trading hours it is not matched within the exchange (Super Match), so it does not take part in the internal price-band comparison.

### When your order takes liquidity (US market trading hours)

Default strategy (`venue` omitted; order details return `default`)

When your order enters Super Match as the taker, the system first compares prices, then determines how much is
matched internally and how much is routed externally:

1. **Price comparison**: Super Match takes the better of the external quote (including ΔP) and the best internal
   level as the best price:
   - Best ask = MIN(`NBO + ΔP`, best internal ask)
   - Best bid = MAX(`NBB − ΔP`, best internal bid)

   The order enters internal matching when the buy price ≥ the best ask, or the sell price ≤ the best bid.
2. **Internal matching**: The order takes resting internal orders within the price band level by level, in price
   priority — a buy order takes up to `NBO + ΔP`, and a sell order takes down to `NBB − ΔP`. The execution price is
   the counterparty's resting price.
3. **Routing the remainder**: Once internal liquidity within the band is exhausted, the remaining quantity is routed
   to the external broker (subject to `venue`; `internal_market` orders are never routed externally). **If the
   notional value of the remaining quantity to be routed is less than 2 USD**, the order goes directly to a terminal
   state and is not submitted to the external broker.

Market orders are internally converted into limit orders valid for 2 seconds, with limit price = last traded price ×
(1 ± slippage (max 1%)). Any quantity still unfilled after 2 seconds is automatically canceled.

**Example**: A user places a market order to buy 2.5 shares of TSLA. The last price is 100 USD and slippage is 1%, so
the order enters Super Match as a limit order at 101 USD. Assume NBO = 100 USD, ΔP = 0.5 USD, and the best internal
ask is 1.2 shares at 99.8 USD:

- Price comparison: best ask = MIN(100.5, 99.8) = 99.8 USD; the buy price 101 ≥ 99.8, so the order enters internal
  matching;
- Internal matching: the 1.2 shares at 99.8 USD are below `NBO + ΔP` = 100.5 and are fully filled at 99.8 USD; there
  are no more in-band resting orders internally, so internal matching ends;
- Routing the remainder: the remaining 1.3 shares (≥ 2 USD) are routed to the external broker and filled.

In the end, 1.2 shares are filled internally and 1.3 shares externally, and the order is fully filled.

`venue` = `internal_market`

The order only ever matches inside Super Match, Bitget's internal matching engine. It is never forwarded to the
external broker, is not affected by market open/close transitions, does not participate in the weekend/Monday-pre-open
batch re-routing of resting orders, and is not subject to the NBBO price band.

`venue` = `lit_market`

The order is submitted to the US stock broker for execution. During US market trading hours it is not matched within the exchange (Super Match), so it does not take part in the internal price-band comparison.

### Outside regular US market trading hours

Outside of regular US market trading hours there is no live NBBO and the external broker is unavailable, so Super
Match's internal order book is the only source of pricing. Matching follows standard price-then-time priority, with
no ΔP band involved. To prevent erroneous pricing while the market is closed, orders are validated against a price
guard: **reference price × an off-hours price deviation limit**. Orders priced outside that bound are rejected.

During this period, `lit_market` orders rest internally within the exchange because the external broker is
unavailable; once the US market reopens, any unfilled portion is routed to the external broker.
(The reference price is the last closing price, and the off-hours price deviation limit is currently 20%.)

### Liquidity direction

- Only the portion of an `internal_market` resting order that is passively matched inside Super Match is recorded
  as **maker**; every other fill — including all fills of default-strategy (`default`) and `lit_market` orders, and any portion of an `internal_market` order
  that actively takes liquidity — is recorded as **taker**.

## Core Trading Capabilities

| Category    | Function          | Implementation                                     | Access             | Protocol Support                        |
|:------------|:------------------|:---------------------------------------------------|:-------------------|:----------------------------------------|
| Market Data | Instruments       | Reused existing endpoint, returns `isReality` flag | Public             | REST                                    |
| Market Data | Ticker            | Reused existing endpoint                           | Public             | REST                                    |
| Market Data | Candlesticks      | Reused existing endpoint                           | Public             | REST + WebSocket                        |
| Market Data | OrderBook (Depth) | Reality-specific endpoint                          | Whitelist required | REST + WebSocket                        |
| Market Data | Platform Fills    | Reality-specific endpoint                          | Whitelist required | REST only                               |
| Market Data | Stock Reference Data (stock info/market states/market calendar) | Reality-specific endpoint | Public | REST only |
| Trading     | Place Order       | Reality-specific endpoint + regular UTA place-order endpoint | Public | REST + WebSocket |
| Trading     | Cancel Order      | Reality-specific endpoint + regular UTA cancel-order endpoint | Public | REST + WebSocket |
| Trading     | Modify Order      | Not supported yet                                  | —                  | —                                       |
| Trading     | Batch Operations  | Not supported yet                                  | —                  | —                                       |
| Assets      | Asset Balances    | Reused existing endpoint                           | Public             | REST + WebSocket                        |

**Note:** Reality market data endpoints are currently only open to whitelisted users. Please contact your BD to apply.

## Market Data

| API                                                                                                                                                                                     | Description                                                                                                                         |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [Get Instruments](/docs/catalog/market/market-data#get-instruments)                                                                                                                | rToken can be identified via the `isReality` field. `yes` indicates a Reality stock token, `no` indicates a non-Reality stock token |
| [Get Tickers](/docs/catalog/market/market-data#get-tickers)                                                                                                                        | Pass an rToken symbol (e.g., `RMUUSDT`) to `symbol` to get its ticker data                                                          |
| [Get Reality OrderBook](/docs/catalog/reality/market-data#get-reality-orderbook)                                                                                            | Get the merged (onshore + offshore) order book depth snapshot. Requires whitelist access                                           |
| [Reality Orderbook Channel](/docs/uta/websocket/reality/public/Reality-OrderBook-Channel)                                                                             | Subscribe to the merged (onshore + offshore) order book depth. Requires whitelist access                                           |
| [Get Reality OrderBook Segmented](/docs/catalog/reality/market-data#get-reality-orderbook-segmented)                                                                        | Get the order book depth snapshot with onshore (internal) and offshore (external) quantities reported separately. Requires whitelist access |
| [Reality Orderbook Segmented Channel](/docs/uta/websocket/reality/public/Reality-OrderBook-Segmented-Channel)                                                         | Subscribe to the segmented depth (onshore/offshore quantities reported separately). Requires whitelist access                      |
| [Get Kline/Candlestick](/docs/catalog/market/market-data#get-kline-candlestick) / [Get Kline/Candlestick History](/docs/catalog/market/market-data#get-kline-candlestick-history) | Get rToken candlestick data<br/>  - Note: For candlesticks before July 9, 2026, `volume`/`turnover` may be empty                    |
| [Candlestick Channel](/docs/uta/websocket/public/Candlesticks-Channel)                                                                                         | Subscribe to rToken candlestick data<br/>                                                                                           |
| [Get Recent Public Fills](/docs/catalog/market/market-data#get-recent-public-fills)                                                                                              | No longer returns fills of rToken trading pairs. Use [Get Reality Fills](/docs/catalog/reality/market-data#get-reality-fills) instead |
| [Public Trades Channel](/docs/uta/websocket/public/New-Trades-Channel)                                                                                           | No longer pushes trades of rToken trading pairs. Use the [Reality Fills Channel](/docs/uta/websocket/reality/public/Reality-Fills-Channel) instead |
| [Get Reality Fills](/docs/catalog/reality/market-data#get-reality-fills)                                                                                                    | Query the latest 100 platform fill records for rToken from the last 3 months, covering both market hours and off-hours. Requires whitelist access |
| [Reality Fills Channel](/docs/uta/websocket/reality/public/Reality-Fills-Channel)                                                                                           | Subscribe to real-time platform fills (internal + lit market) for rToken, with the execution venue `execVenue`. Public channel, no login required |

:::warning{title="Notes for Reality (rToken) candlesticks"}

- rToken only supports the `market` candlestick type.
- rToken only supports the `1m`, `5m`, `15m`, `1H`, `4H`, `1D` intervals.
- For the WebSocket Candlestick Channel, the `1m` interval push data does not include `volume`/`turnover`.
:::

### Depth: merged vs. segmented

[Get Reality OrderBook](/docs/catalog/reality/market-data#get-reality-orderbook) /
[Reality Orderbook Channel](/docs/uta/websocket/reality/public/Reality-OrderBook-Channel) return the
**merged** depth — onshore (Super Match internal) and offshore (external broker) liquidity combined into a single
view of each price level, without distinguishing where the liquidity originates.

[Get Reality OrderBook Segmented](/docs/catalog/reality/market-data#get-reality-orderbook-segmented) /
[Reality Orderbook Segmented Channel](/docs/uta/websocket/reality/public/Reality-OrderBook-Segmented-Channel)
return the same price levels but **report onshore and offshore quantities separately** at each level, so you can see
how much of the depth at a given price is internal versus external.

Both WebSocket channels push depth updates at the same cadence: every 500ms when the depth snapshot has changed, or every
10s if it has not changed.

:::note{title="Additional notes"}
During market hours (pre-market/regular/after-hours), the Bitget API/WebSocket returns/pushes market-maker depth
data in addition to the top-of-book levels present in the US stock market's L2 data. The order book shown to
App/Web users, however, filters out levels that are not also present in the US stock market's L2 data, rounds
displayed quantities down, and merges price levels at a coarser precision.<br/>This is a **display-only** behavior
for the Web/App front end — it does not affect which levels are actually matchable via Super Match.
:::

### Standard depth channels behave differently for rToken pairs

Outside of the rToken-specific endpoints above, the standard depth channels change behavior for rToken
trading pairs:

| Channel / Endpoint                       | During US market trading hours                    | Outside US market trading hours                                      |
|:-------------------------------------------|:------------------------------------------------------|:-------------------------------------------------------------------------|
| WebSocket `books1`                        | Pushes the merged best bid/ask, as usual              | Continues to push the merged best bid/ask                               |
| WebSocket `books5` / `books50` / `books`  | Does not push for rToken pairs                       | Pushes internal (onshore) depth only; every 10s if unchanged            |
| REST standard order book (`orderbook`)    | Returns only 1 level for rToken pairs                | Returns the full internal (onshore) depth, up to the requested limit    |

### Trade data coverage

| Source                                                                                                            | During US market trading hours      | Outside US market trading hours     |
|:---------------------------------------------------------------------------------------------------------------------|:---------------------------------------|:----------------------------------------|
| [Public Trades Channel](/docs/uta/websocket/public/New-Trades-Channel) (`publicTrades`)                          | Not available for rToken pairs     | Not available for rToken pairs      |
| [Get Recent Public Fills](/docs/catalog/market/market-data#get-recent-public-fills) (`fills`)                      | Not available for rToken pairs      | Not available for rToken pairs      |
| [Get Reality Fills](/docs/catalog/reality/market-data#get-reality-fills) (whitelist)                                | Full coverage (internal + external) | Full coverage (internal + external) |
| [Reality Fills Channel](/docs/uta/websocket/reality/public/Reality-Fills-Channel) (`reality-fills`)          | Full coverage (internal + external) | Full coverage (internal + external) |
| Private Fast Fill channel                                                                                          | Covers both internal and external fills for your own orders | Covers both internal and external fills for your own orders |

## Stock Reference Data

The following endpoints provide reference information about the underlying US stock for rToken (tokenized US stock) trading pairs. These are all public endpoints and do not require whitelist access.

| API                                                                                | Description                                                                             |
|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [Get Stock Info](/docs/catalog/reality/market-data#get-stock-info)         | Get the underlying US stock information for a specified rToken trading pair             |
| [Get Market States](/docs/catalog/reality/market-data#get-market-states)   | Get the current US stock market trading session status (pre-market/regular/after-hours/overnight) |
| [Get Market Calendar](/docs/catalog/reality/market-data#get-market-calendar) | Get the market holiday and closure calendar for US stocks                                |

## Trading

| API                                                                                           | Description                                                                                    |
|:----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [Place Reality Order](/docs/catalog/reality/trading#place-reality-order)   | rToken order placement endpoint. Rate limit depends on `venue`: `internal_market` (on-exchange) follows the Crypto rate limit, 10/sec/UID; the default strategy (`venue` omitted) and `lit_market` (off-exchange) default to 5/sec/UID, 30/sec/UID for whitelisted users |
| [Cancel Reality Order](/docs/catalog/reality/trading#cancel-reality-order) | rToken order cancellation endpoint. Rate limit follows the same rules as Crypto |

**Note:** The regular UTA [Place Order](/docs/catalog/trading/order-management#place-order) and [Cancel Order](/docs/catalog/trading/order-management#cancel-order) endpoints and the WebSocket [place-order](/docs/uta/websocket/private/Place-Order-Channel)/[cancel-order](/docs/uta/websocket/private/Cancel-Order-Channel) channels now support Reality trading pairs. For order placement the rate limit depends on `venue` (on-exchange follows the Crypto rate limit, off-exchange follows the rToken rate limit); for order cancellation the rate limit follows the same rules as Crypto.<br/>
Order modification is not supported. Batch order placement and batch cancellation are not supported for rToken
trading pairs — if you need to adjust a resting order, cancel it and place a new one individually.

### Limit Order Trading Rules for rToken

:::warning{title="Scope"}
These rules apply to off-exchange trading only; on-exchange trading is not subject to these restrictions.
:::

**1. Trigger conditions**

The system monitors the status of terminal orders for each UID on each trading pair over a statistical cycle. The limit order function will be restricted when both of the following conditions are met:

- The total number of terminal orders for a single UID on a single trading pair exceeds 1,000 within the statistical cycle (effective from the start of the statistical cycle on November 19, 2026);
- The fill rate is below 10%.

Filled order: an order that is fully filled.<br/>
Fill rate = number of filled orders / total number of orders.

**2. Restriction details**

Once the above conditions are triggered, the spot limit order function for the corresponding trading pair of that UID will be restricted.<br/>
When the user attempts to submit a limit order, the system will return:

```
41121 Abnormal trading detected. Limit order functionality has been restricted.
```

**3. Automatic lifting mechanism**

- If the UID triggers the above conditions again in the next statistical cycle, the limit order restriction will remain in effect;
- If the restriction conditions are not triggered again within a new statistical cycle, the system will automatically lift the restriction and resume normal limit order functionality;
- The system recalculates and re-evaluates at the start of each new statistical cycle (05:00 UTC+8 daily).

Please use the limit order function reasonably and avoid high-frequency, large-volume orders with abnormally low fill rates.

## Trading Strategies & Use Cases

### Delta Neutral Mode

#### Overview and use cases

Delta Neutral Mode is a toggle in the trading settings of the Unified Trading Account's (UTA) "Multi-Asset Margin Mode", designed
for traders running hedging strategies such as funding rate arbitrage and basis arbitrage within the UTA. When enabled,
qualifying hedged positions are moved to the back of the auto-deleveraging (ADL) queue — they are only reached after
all non-qualifying positions have been processed — reducing the chance that a hedged position is auto-deleveraged in
extreme market conditions and leaves the strategy with a "broken leg". This mode only affects ADL ranking priority; it
does not change margin calculation, liquidation rules, or risk control policies.

Delta Neutral Mode now supports treating an rToken and its underlying stock as the same asset for hedging
calculations. For example, rAAPL and AAPL are calculated together: a user's rAAPL spot holding and AAPLUSDT futures
position can form a hedged position and jointly participate in hedge determination and ADL ranking protection. This
extension takes effect automatically once the conditions are met, with no additional settings required. This means
users can use rToken spot, priced at the "real stock price", as the long leg and the highly liquid stock perpetual
futures as the short leg, completing the hedge within a single UTA — while the spot holding itself continues to serve
as futures margin.

Typical use cases include: funding rate arbitrage, holding rToken spot and shorting the futures on the same underlying
to collect positive funding; basis arbitrage, buying spot and shorting futures when futures trade at a premium to the
rToken spot, then waiting for the spread to converge; and position protection, temporarily locking in price risk
ahead of earnings or macro events while holding long-term US stock exposure.

#### Eligibility

**Identity requirements:** When enabling, you must meet any one of the following — VIP3 or above / Pro user / market
maker / institutional loan user. The identity check is performed only once at the time of enabling; subsequent changes
in identity do not affect the enabled status. Demo trading is not subject to identity requirements.

**Additional rToken requirement:** The rToken must be a margin coin supported by the UTA. For the list of rTokens
currently supported as UTA margin, see [Discount Rate | Bitget Unified Trading Account](https://www.bitget.com/trade-info/discount-rate).

**How to enable and more details:** [How Does Delta Neutral Mode Work in the Unified Trading Account?](https://www.bitget.com/support/articles/12560603881602)

### Underlying Asset Mapping

#### rToken vs. underlying stock, spot and futures trading pairs

Each rToken is issued by the Reality protocol and backed 1:1 by a real US stock or ETF held in custody by a licensed
broker. On Bitget, the same underlying stock may have both an rToken spot trading pair and a USDT-M stock perpetual
futures contract. Naming conventions are as follows:

| Instrument | Naming convention | Example (Apple) | How to identify via API |
|:-----|:-----|:-----|:-----|
| Bitget Spot trading pair | R + stock ticker + USDT | `RAAPLUSDT` | `isReality` = `yes` in [Get Instruments](/docs/catalog/market/market-data#get-instruments) (`category=SPOT`) |
| Bitget Futures trading pair | Stock ticker + USDT | `AAPLUSDT` | `instrumentType` = `stock` / `etf` in [Get Instruments](/docs/catalog/market/market-data#get-instruments) (`category=USDT-FUTURES`) |

#### Asset mappings and scope

In Delta Neutral Mode, the following groups of coins are treated as the same asset: an rToken and its underlying
stock futures (e.g., rAAPL and AAPL), BGBTC and BTC, BGSOL and SOL, and XAU, XAUT and PAXG.

Note the scope: **hedging only applies within the "same underlying"; different assets cannot hedge each other**. For
example, using rQQQ to hedge an NVDAUSDT short, or using the leveraged ETF rTSLL (Direxion 2x long TSLA) to hedge
TSLAUSDT, will not be recognized as a hedged position, because their underlying assets differ. In addition, holding
large amounts of stablecoins or other assets cannot hedge the futures position of a given asset; isolated-margin
futures positions are not included in the calculation; and the rToken itself must be on the UTA margin coin list.

### Trading Examples

Prices and funding rates in the following examples are illustrative only and are used to explain the calculations.
Refer to the actual order book, funding rates, and fee tiers in practice.

#### Example 1: rNVDA + NVDAUSDT funding rate arbitrage

**Background:** The user is a VIP3 institutional client with Delta Neutral Mode enabled in UTA Multi-Asset Margin Mode, and has
10,000 USDT in the account. NVDAUSDT funding has been consistently positive, and the user wants to collect funding
without taking NVDA directional price risk.

**Steps:**

1. During US market hours, buy rNVDA with a limit order. Assume 50 shares are filled at an average price of 200 USDT,
   for a notional value of 10,000 USDT (API: [Place Reality Order](/docs/catalog/reality/trading#place-reality-order),
   or the UTA [Place Order](/docs/catalog/trading/order-management#place-order) endpoint with `category=SPOT`,
   `symbol=RNVDAUSDT`; to route unfilled quantity to the US stock market, omit `venue` to use the default strategy);
2. After confirming the spot leg has actually filled 50 shares, short NVDAUSDT perpetual futures for 50 NVDA in
   cross-margin mode within the same UTA (API: the UTA [Place Order](/docs/catalog/trading/order-management#place-order)
   endpoint with `category=USDT-FUTURES`);
3. The rNVDA holding is now 50 and the net futures position is −50 — opposite directions and equal size. The net
   futures position = 0 and the ratio is 0% ≤ 5%, so it is recognized as a hedged position and receives ADL ranking
   protection;
4. While holding, stock futures settle funding every 8 hours; when funding is positive, the short side receives it.

#### Example 2: Partial fill pushes the ratio over the limit, and rebalancing

**Background:** Same account as Example 1. The user first places a futures short for 53 NVDA, but the rNVDA limit buy
order only fills 50 shares, and the remainder is unfilled.

**Determination:** rNVDA holding is 50 and the net futures position is −53, opposite directions with |50| &lt; |−53|.
Net futures position = |50 − 53| = 3; total position = MAX[50 + 0, |0 − 53|] = 53; ratio = 3 ÷ 53 ≈ 5.66% &gt; 5%. The
hedge condition is not met, and the asset participates in ADL ranking under the normal rules.

**Resolution:** Buy at least 1 more share of rNVDA to bring the ratio down to 2 ÷ 53 ≈ 3.77%, or reduce the futures
short to 52 or less. Once the ratio falls back, the system automatically restores the hedged-position determination —
there is no need to re-enable the toggle. In practice, "spot first, futures second" is recommended: drive the futures
order size from the actual filled quantity of the spot leg, and use the [private Fill channel](/docs/uta/websocket/private/Fill-Channel)
to monitor fills on both legs in real time. Note that rToken orders cannot be modified; to change the price, cancel
and place a new order.

#### Example 3: rTSLA + TSLAUSDT basis arbitrage

**Background:** During periods of exuberant sentiment, the TSLAUSDT perpetual trades at a premium to rTSLA spot.
Assume the rTSLA spot price is 400 USDT and the TSLAUSDT futures price is 404 USDT, a premium of about 1%.

**Steps:** Buy 20 shares of rTSLA (about 8,000 USDT) and simultaneously short 20 TSLA of TSLAUSDT (about 8,080 USDT).
The combined ratio is 0%, so it is recognized as a hedged position. When the futures premium converges to 0, close
both legs at the same time: regardless of whether TSLA rises or falls, the locked-in spread profit is about
20 × 4 = 80 USDT (about 1%). If funding is positive while holding, the short side also collects funding.

**Things to watch:** During market hours, rTSLA execution prices are in sync with the US stock market, so the spread
comes mainly from the futures-side premium; use the [Reality segmented order book](/docs/catalog/reality/market-data#get-reality-orderbook-segmented)
to assess internal and external depth before executing. Outside US market hours, rToken pricing relies on Super
Match internal liquidity, orders are protected by "reference price × off-hours price deviation limit (currently
20%)", and depth is thinner — opening or closing large positions outside market hours is not recommended. Significant
slippage on the other leg could wipe out the entire basis profit.

## Assets

rToken assets have no dedicated asset query endpoint — reuse the
existing [Get Account Assets](/docs/catalog/account/assets-balance#get-account-assets) endpoint to query them.

---

# rToken 交易指南

## 概述

rToken指 Bitget 的美股代币化交易对，交易对名称以 `r` 为前缀（如 `rAAPLUSDT`）。

关于rToken的详情信息，请参考：

- [Reality协议及rToken代币化介绍](https://www.bitget.com/academy/what-is-reality-protocol-and-rtokens-rwa-tokenization-defi-guide)。
- [Bitget 股票现货交易常见问题：rTokens、分红、费用与交易时间](https://www.bitget.com/zh-CN/support/articles/12560603887176)
- [美股持仓转移到Bitget](https://www.bitget.com/zh-CN/support/articles/12560603897720)


## 订单路由与撮合机制

rToken订单通过 **Super Match** 完成撮合——这是 Bitget 交易引擎与外部券商（用于将未成交的订单流路由至美股市场）之间的一层内部撮合机制。无论美股当前是否开市，每一笔 rToken 现货订单都会先经过 Super Match 评估，未成交的部分才会路由至场外。

### 下单参数`venue`：选择订单可成交的范围

`venue` 参数（在[下单](/zh-CN/docs/catalog/trading/order-management#place-order)与[创建Reality股票订单](/zh-CN/docs/catalog/reality/trading#place-reality-order)接口均可使用）控制订单的路由行为：

| `venue` 取值            | 行为说明                                                                                                     |
|:--------------------------|:----------------------------------------------------------------------------------------------------------------|
| 不传（默认策略，订单详情返回 `default`） | Super Match 优先在交易所内部比价撮合，未成交的部分再路由至外部券商（场外公开市场）。<br/><u>针对部分周末可交易的币对，仍挂在场外未成交的挂单会被转回场内挂单，如果周末仍未成交，会转到场外继续挂单；</u> |
| `internal_market`        | 订单只会在 Super Match Bitget内部撮合，不会提交至美股券商，不受开市/休市切换的影响，也不参与周末/周一开市前对挂单的批量重路由 |
| `lit_market`             | 订单提交至美股券商执行。美股开市时段不在交易所内（Super Match）撮合；<u>美股休市（如周末）时外部券商不可用，订单会先在场内挂单等待撮合，开市后未成交部分再路由至券商</u> |

下单时可传入的 `venue` 取值为 `internal_market` 或 `lit_market`，不传即为默认策略；订单详情（REST 订单查询及 WebSocket 订单推送）返回的 `venue` 为 `default` / `internal_market` / `lit_market` 之一。

:::warning{title="venue 枚举调整（2026 年 11 月 5 日起生效）"}
- 原 `internalization` 更名为 `internal_market`，含义不变，请将该枚举值替换为 `internal_market`。
- 订单详情中原本展示为 `lit_market` 的订单（优先场内比价撮合、未成交部分提交至券商），调整后展示为 `default`，请同步更新订单详情的解析逻辑。
- 新的 `lit_market` 含义为"订单提交至券商执行，不在交易所内撮合"，与调整前订单详情中的 `lit_market` 含义不同，请注意区分。
:::

**一般使用建议：**

- 若您希望订单流完全保留在 Super Match 内部（如报价/做市场景），使用 `internal_market`。
- 若您希望优先在场内比价撮合、未成交的部分也能到达外部券商（如建仓或减仓），不传 `venue`（默认策略）。
- 若您希望订单直接提交至美股券商执行、不参与场内撮合，使用 `lit_market`。

订单有效期由 `rTokenTimeInForce` 单独控制：`gtd`（当前交易时段内有效）或 `gtc`（有效期 90 天）。具体的时段边界规则详见[下单](/zh-CN/docs/catalog/trading/order-management#place-order)与[创建Reality股票订单](/zh-CN/docs/catalog/reality/trading#place-reality-order)接口的字段说明。

:::warning{title="暂不支持改单"}
rToken订单暂不支持改单。如需调整挂单的价格或数量，请先撤单，再重新下单。
:::

### 挂单成交逻辑（美股交易时段）

- 默认策略（不传 `venue`，订单详情返回 `default`）

美股交易时段内(盘前、盘中、盘后、夜盘)，Super Match 会围绕 **NBBO**（全美最优报价）构建一个动态价格带，用于判断您的挂单限价单能否在场内撮合：

- **ΔP** 是针对每笔订单实时估算的滑点补偿——即该订单若改为直接路由至外部券商，预计会多承受的滑点。ΔP 按单独订单计算（并非固定常数），会随订单规模相对日均成交量的占比、当前波动率、NBBO 价差，以及当下外部流动性的厚薄而扩大。（当前ΔP暂时设置为0，后续可能会更改）
- 场内可撮合的 **价格带** 为 **[NBB − ΔP, NBO + ΔP]**：
  - 散户买单可与价格不高于 `NBO + ΔP` 的任意场内挂卖单（ask）撮合；
  - 散户卖单可与价格不低于 `NBB − ΔP` 的任意场内挂买单（bid）撮合。
- 价格带内的撮合按 **逐档位** 进行（不仅限于最优档位），直到来单完全成交或价格带内流动性耗尽。价格带内无法成交的部分将路由至场外（受 `venue` 约束）。
- **成交价格始终为您的挂单（报价）价格**——而非 NBBO，也非价格带边界价。若您的挂卖单落在价格带内并被吃掉，散户吃单方支付的是您的报价，而不是 `NBO + ΔP`。这意味着您的报价与 NBBO 之间的全部价差都归您（作为做市方）所得。

盘前与盘后、夜盘时段属于中间状态：NBBO 仍然存在，但外部流动性较薄，因此场内可成交的价格范围相比常规时段实际上会更宽。

- `venue`= `internal_market`

订单只会在 Super Match Bitget内部撮合，不会路由至外部券商，不受开市/休市切换的影响，也不参与周末/周一开市前对挂单的批量重路由，不受NBBO价格带限制

- `venue`= `lit_market`

订单提交至美股券商执行，美股交易时段内不在交易所内（Super Match）撮合，不参与场内价格带比价


### 吃单成交逻辑（美股交易时段）

- 默认策略（不传 `venue`，订单详情返回 `default`）

当您的订单作为吃单方进入 Super Match 时，系统会先比价，再决定场内撮合与路由至场外的数量：

1. **比价**：Super Match 取场外报价（含 ΔP）与场内最优档位中更优的一方作为最优价：
   - 最优卖价 = MIN(`NBO + ΔP`, 场内卖一价)
   - 最优买价 = MAX(`NBB − ΔP`, 场内买一价)

   买单价格 ≥ 最优卖价，或卖单价格 ≤ 最优买价时，订单进入场内撮合。
2. **场内撮合**：订单按价格优先逐档吃掉价格带内的场内挂单——买单最多吃到 `NBO + ΔP`，卖单最多吃到 `NBB − ΔP`。成交价为对手方的挂单价格。
3. **剩余路由**：价格带内的场内流动性耗尽后，剩余部分路由至外部券商（受 `venue` 约束，`internal_market` 订单不会路由至场外）。若剩余待路由部分的金额不足 2 美元，订单直接进入终态，不再提交至外部券商。

市价单在内部会转换为有效期 2 秒的限价单，限价 = 最新成交价 ×（1 ± 滑点(最大1%)），2 秒后未成交部分自动撤销。

**示例**：用户市价买入 2.5 股 TSLA，最新价 100 USD、滑点 1%，即以 101 USD 限价进入 Super Match。假设当前 NBO = 100 USD、ΔP = 0.5 USD，场内卖一为 99.8 USD × 1.2 股：

- 比价：最优卖价 = MIN(100.5, 99.8) = 99.8 USD，买入价 101 ≥ 99.8，进入场内撮合；
- 场内撮合：99.8 USD 的 1.2 股低于 `NBO + ΔP` = 100.5，全部成交，成交价 99.8 USD；场内无更多带内挂单，撮合结束；
- 剩余路由：剩余 1.3 股（ ≥ 2 美元）路由至外部券商成交。

最终该订单场内成交 1.2 股、场外成交 1.3 股，订单全部成交。

- `venue`= `internal_market`

订单只会在 Super Match Bitget内部撮合，不会路由至外部券商，不受开市/休市切换的影响，也不参与周末/周一开市前对挂单的批量重路由，不受NBBO价格带限制

- `venue`= `lit_market`

订单提交至美股券商执行，美股交易时段内不在交易所内（Super Match）撮合，不参与场内价格带比价

### 美股其他交易时段

美股常规交易时段之外没有实时 NBBO(周末/假期)，外部券商也不可用，因此 Super Match 的内部订单簿是唯一的定价来源。此时撮合遵循标准的价格优先、时间优先规则，不涉及 ΔP 价格带。为防止休市期间出现异常定价，订单会受到价格保护机制校验：**参考价 × 休市期间价格偏离限制**。超出该范围的订单将被拒绝。（参考价格为上次收盘价格，价格偏离限制当前限制为20%）

该时段内，`lit_market` 订单因外部券商不可用，会先在场内挂单等待撮合；待美股开市后，仍未成交的部分再路由至外部券商。


### 流动性方向说明

- 仅 `internal_market` 挂单中被动在 Super Match 内部撮合的部分记为 **Maker**；其余所有成交——包括默认策略（`default`）与 `lit_market` 订单的全部成交，以及 `internal_market` 订单中主动吃单的部分——均记为 **Taker**。


## 核心交易链路

| 分类  | 功能   | 接口实现                     | 开放范围 | 协议支持                     |
|:----|:-----|:-------------------------|:-----|:-------------------------|
| 行情类 | 币对信息 | 复用现有接口，返回 `isReality` 标识 | 公开   | REST                     |
| 行情类 | 行情   | 复用现有接口                   | 公开   | REST                     |
| 行情类 | K 线  | 复用现有接口                   | 公开   | REST + WebSocket         |
| 行情类 | 深度   | Reality 独立接口             | 需白名单 | REST + WebSocket         |
| 行情类 | 平台成交 | Reality 独立接口             | 需白名单 | 仅支持 REST                 |
| 行情类 | 股票基础数据（股票信息/市场状态/休市日历） | Reality 独立接口 | 公开 | 仅支持 REST |
| 交易类 | 下单   | Reality 独立接口 + 常规下单接口   | 公开 | REST + WebSocket |
| 交易类 | 撤单   | Reality 独立接口 + 常规撤单接口   | 公开 | REST + WebSocket |
| 交易类 | 改单   | 暂不支持                     | —    | —                        |
| 交易类 | 批量操作 | 暂不支持                     | —    | —                        |
| 资产类 | 资产查询 | 复用现有接口                   | 公开   | REST + WebSocket         |

**注意：** Reality 行情接口暂时面向白名单用户开放，请联系您的 BD 进行申请。

## 行情数据

| 接口                                                                                                                                                          | 说明                                                                      |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [获取交易产品信息](/zh-CN/docs/catalog/market/market-data#get-instruments)                                                                                     | rToken可以通过 `isReality` 字段识别。`yes` 表示 Reality 股票代币，`no` 表示非 Reality 股票代币 |
| [获取行情数据](/zh-CN/docs/catalog/market/market-data#get-tickers)                                                                                           | symbol传入rToken即可获取行情数据，如RMUUSDT                                         |
| [获取Reality深度数据](/zh-CN/docs/catalog/reality/market-data#get-reality-orderbook)                                                                  | 获取融合（场内+场外）深度快照。需白名单权限                                                |
| [Reality深度频道](/zh-CN/docs/uta/websocket/reality/public/Reality-OrderBook-Channel)                                                         | 订阅融合（场内+场外）深度数据。需白名单权限                                                |
| [获取Reality分层订单簿](/zh-CN/docs/catalog/reality/market-data#get-reality-orderbook-segmented)                                                                        | 获取深度快照，各档位场内（内部）与场外（外部）数量分别展示。需白名单权限 |
| [Reality分层订单簿频道](/zh-CN/docs/uta/websocket/reality/public/Reality-OrderBook-Segmented-Channel)                                                         | 订阅分层深度数据（场内/场外数量分别展示）。需白名单权限                      |
| [K线数据](/zh-CN/docs/catalog/market/market-data#get-kline-candlestick) / [历史k线数据](/zh-CN/docs/catalog/market/market-data#get-kline-candlestick-history) | 获取 rToken K线数据<br/>  - 注：2026年7月9日之前的K线数据，`volume`/`turnover`可能为空       |
| [K线频道](/zh-CN/docs/uta/websocket/public/Candlesticks-Channel)                                                                      | 订阅 rToken K线数据<br/>                                                     |
| [获取平台近期成交数据](/zh-CN/docs/catalog/market/market-data#get-recent-public-fills)                                                                              | 不再返回 rToken 交易对的成交数据，请改用 [获取Reality平台成交数据](/zh-CN/docs/catalog/reality/market-data#get-reality-fills) |
| [最新成交频道](/zh-CN/docs/uta/websocket/public/New-Trades-Channel)                                                                           | 不再推送 rToken 交易对的成交数据，请改用 [Reality公共成交频道](/zh-CN/docs/uta/websocket/reality/public/Reality-Fills-Channel) |
| [获取Reality平台成交数据](/zh-CN/docs/catalog/reality/market-data#get-reality-fills)                                                                    | 查询 rToken 近3个月最新的100条平台成交记录，覆盖开市与休市时段，需白名单权限                                      |
| [Reality公共成交频道](/zh-CN/docs/uta/websocket/reality/public/Reality-Fills-Channel)                                                                    | 实时订阅 rToken 平台成交（内部成交 + 公开市场成交），带成交发生地 `execVenue`。公共频道，无需登录                    |

:::warning{title="Reality（rToken）K线注意事项"}

- rToken仅支持 `market` 类型K线。
- rToken仅支持 `1m`、`5m`、`15m`、`1H`、`4H`、`1D` 时间粒度。
- WebSocket K线频道的`1m` 粒度推送数据不包含 `volume` 和 `turnover`。
:::

### 深度数据：融合深度与分层深度

[获取Reality深度数据](/zh-CN/docs/catalog/reality/market-data#get-reality-orderbook) /
[Reality深度频道](/zh-CN/docs/uta/websocket/reality/public/Reality-OrderBook-Channel) 返回的是**融合**深度——将场内（Super Match 内部）与场外（外部券商）的流动性合并展示在同一档位视图中，不区分流动性来源。

[获取Reality分层订单簿](/zh-CN/docs/catalog/reality/market-data#get-reality-orderbook-segmented) /
[Reality分层订单簿频道](/zh-CN/docs/uta/websocket/reality/public/Reality-OrderBook-Segmented-Channel)
返回相同的价格档位，但会**分别展示每个档位的场内与场外数量**，让您能看出某个价位的深度中有多少来自场内、多少来自场外。

两个Websocket频道的推送频率一致：深度副本有变化则每 500ms 推送一次，无变化则每 10s 推送一次。

:::note{title="其他说明"}
开市时段(盘前/盘中/盘后)，Bitget API/Websocket会返回/推送除了美股市场L2数据中的最优档位数据外，也会推送做市商的深度数据；而App/Web用户展示的订单簿会过滤掉未出现在美股市场 L2 数据中的最优档位，并对展示数量向下取整、按更粗的精度合并档位。<br/>这只是面向Web/App的**展示层行为**——不影响 Super Match 实际可撮合的档位。
:::

### 标准深度频道对 rToken 交易对的行为差异

除上述 rToken 专用接口外，标准深度频道对 rToken交易对的行为也有所不同：

| 频道/接口                                   | 美股开市时段                                   | 美股休市时段                                             |
|:----------------------------------------------|:--------------------------------------------------|:-------------------------------------------------------------|
| WebSocket `books1`                           | 正常推送融合最优买卖价                             | 继续推送融合最优买卖价                                        |
| WebSocket `books5` / `books50` / `books`     | 不针对 rToken 交易对推送                           | 仅推送场内（内部）深度；无变化时每 10s 推送一次                 |
| REST 标准深度（`orderbook`）                  | 针对 rToken 交易对仅返回1档                        | 返回完整场内（内部）深度，最多至请求的档位数上限                  |

### 成交数据覆盖范围

| 数据来源                                                                                                | 美股开市时段                           | 美股休市时段                           |
|:-----------------------------------------------------------------------------------------------------------|:------------------------------------------|:------------------------------------------|
| [最新成交频道](/zh-CN/docs/uta/websocket/public/New-Trades-Channel)（`publicTrades`）                   | 不支持 rToken 交易对                      | 不支持 rToken 交易对                       |
| [获取平台近期成交数据](/zh-CN/docs/catalog/market/market-data#get-recent-public-fills)（`fills`）         | 不支持 rToken 交易对                        | 不支持 rToken 交易对                        |
| [获取Reality平台成交数据](/zh-CN/docs/catalog/reality/market-data#get-reality-fills)（需白名单）           | 全量覆盖（场内+场外）                       | 全量覆盖（场内+场外）                       |
| [Reality公共成交频道](/zh-CN/docs/uta/websocket/reality/public/Reality-Fills-Channel)（`reality-fills`）   | 全量覆盖（场内+场外）                       | 全量覆盖（场内+场外）                       |
| 私有快速成交频道                                                                                          | 覆盖您自己订单的场内与场外成交               | 覆盖您自己订单的场内与场外成交               |

## 股票基础数据

以下接口用于查询 rToken（美股代币化交易对）底层股票的基础信息，均为公开接口，无需白名单权限。

| 接口                                                                                    | 说明                                                     |
|:----------------------------------------------------------------------------------------|:---------------------------------------------------------|
| [获取股票信息](/zh-CN/docs/catalog/reality/market-data#get-stock-info)     | 获取指定 rToken 交易对对应的美股股票信息                    |
| [获取市场状态](/zh-CN/docs/catalog/reality/market-data#get-market-states)  | 获取美股市场当前所处的交易时段状态（盘前/持续交易/盘后/夜盘） |
| [获取休市日历](/zh-CN/docs/catalog/reality/market-data#get-market-calendar) | 获取美股市场的休市日历信息                                  |

## 交易下单

| 接口                                                                                           | 说明                                         |
|:---------------------------------------------------------------------------------------------|:-------------------------------------------|
| [创建Reality股票订单](/zh-CN/docs/catalog/reality/trading#place-reality-order)  | rToken 下单接口。限频按 `venue` 区分：`internal_market`（场内）按 Crypto 限频 10次/秒/UID；默认策略（不传 `venue`）及 `lit_market`（场外）默认5次/秒/UID，白名单用户30次/秒/UID |
| [撤销Reality股票订单](/zh-CN/docs/catalog/reality/trading#cancel-reality-order) | rToken 撤单接口，限频规则与 Crypto 一致            |

**注：**
统一账户[下单](/zh-CN/docs/catalog/trading/order-management#place-order)及[撤单](/zh-CN/docs/catalog/trading/order-management#cancel-order)接口、WebSocket [place-order](/zh-CN/docs/uta/websocket/private/Place-Order-Channel)/[cancel-order](/zh-CN/docs/uta/websocket/private/Cancel-Order-Channel) 下单撤单频道现已支持 Reality 交易对。下单限频按 `venue` 区分（场内按 Crypto 限频，场外按 rToken 限频）；撤单限频规则与 Crypto 一致。<br/>
暂不支持改单。rToken 交易对暂不支持批量下单与批量撤单——如需调整挂单，请逐笔撤单后重新下单。

### rToken 限价单交易规则

:::warning{title="适用范围"}
仅限场外交易，场内交易不受此限制。
:::

**一、限制触发条件**

系统将按统计周期监测单个 UID 在单个币对下的终态订单情况。若同时满足以下条件，将触发限价单功能限制：

- 单个 UID、单个币对在统计周期内的终态订单总数超过 1,000 笔（自 2026 年 11 月 19 日统计周期开始生效）；
- 成交率低于 10%。

成交订单：完全成交订单；<br/>
成交率 = 成交订单数 / 总订单数。

**二、限制内容**

触发上述条件后，该 UID 对应币对的现货限价单功能将被限制。<br/>
用户尝试提交限价单时，系统将提示：

```
41121 异常交易，限价功能已限制。
```

**三、自动解除机制**

- 若该 UID 在下一个统计周期内再次触发上述条件，限价单限制将继续生效；
- 若在新的统计周期内未再次触发限制指标，系统将自动解除限制，限价单功能恢复正常；
- 系统将在进入下一统计周期时（每日 05:00 UTC+8）重新进行计算和评估。

请用户合理使用限价单功能，避免高频、大量低成交率的异常挂单行为。感谢您的理解与支持。

## 交易策略与应用场景

### Delta 中性模式（Delta Neutral Mode）

#### 功能介绍及适用场景

Delta 中性模式是统一账户「多币种保证金模式」交易设置中的一个功能开关，面向在统一账户下运行资金费率套利、基差套利等对冲策略的交易者。开启后，符合条件的对冲仓位在自动减仓（ADL）队列中的排名会整体后移——只有当所有不符合条件的仓位都已处理后，才会轮到对冲仓位，从而降低极端行情下对冲仓位被自动减仓、导致策略"断腿"的概率。该模式只影响 ADL 排序优先级，不改变保证金计算、强平规则或风控政策。

Delta 中性模式已支持将 rToken 与其底层股票视为同一资产进行对冲计算。例如 rAAPL 与 AAPL 将被统一计算：用户持有的 rAAPL 现货与 AAPLUSDT 合约仓位可以形成对冲仓位，共同参与对冲判定与 ADL 排名保护。该扩展在满足条件后自动生效，无需额外设置。这意味着用户可以用"真实股票价格"的 rToken 现货作为多头腿，用流动性充足的股票永续合约作为空头腿，在同一个 UTA 内完成对冲，并且现货持仓本身还能继续作为合约保证金使用。

典型适用场景包括：持有 rToken 现货、希望通过做空同标的合约收取正资金费率的资金费率套利；当合约价格相对 rToken 现货出现溢价时，买现货、空合约等待价差收敛的基差套利；以及长期持有美股敞口、但在财报或宏观事件前希望临时锁定价格风险的持仓保护。

#### 开启条件

**身份条件：** 点击开启时需满足任一身份——VIP3 及以上 / Pro 用户 / 做市商 / 机构借贷用户。身份校验仅在开启时触发一次，之后身份变化不影响已开启状态；模拟盘不受身份限制。

**rToken 额外条件：** 对应的 rToken 必须是 UTA 支持的保证金币种，rToken 当前支持作为 UTA 保证金的币种名单，请参考 [币种抵押率 | Bitget 统一交易账户](https://www.bitget.com/zh-CN/trade-info/discount-rate)。

**开启方法及详细介绍可参考：** [统一账户中的 Delta 中性模式如何运作？](https://www.bitget.com/zh-CN/support/articles/12560603881602)

### 标的资产映射（Underlying Asset Mapping）

#### rToken 与底层股票、现货及合约交易对的对应关系

每个 rToken 由 Reality 协议发行，背后对应持牌经纪商处 1:1 托管的真实美股或 ETF。在 Bitget 上，同一只底层股票可能同时存在 rToken 现货交易对和 U 本位股票永续合约两种交易工具，命名规则如下：

| 工具 | 命名规则 | 示例（Apple） | API 识别方式 |
|:-----|:-----|:-----|:-----|
| Bitget Spot 交易对 | R + 股票代码 + USDT | `RAAPLUSDT` | [获取交易产品信息](/zh-CN/docs/catalog/market/market-data#get-instruments)（`category=SPOT`）中 `isReality` = `yes` |
| Bitget Futures 交易对 | 股票代码 + USDT | `AAPLUSDT` | [获取交易产品信息](/zh-CN/docs/catalog/market/market-data#get-instruments)（`category=USDT-FUTURES`）中 `instrumentType` = `stock` / `etf` |

#### 不同资产之间的 Mapping 关系及适用范围

Delta 中性模式下，以下几组币种会被视为同一资产统一计算：rToken 与其底层股票合约（如 rAAPL 与 AAPL）、BGBTC 与 BTC、BGSOL 与 SOL，以及 XAU、XAUT 与 PAXG。

需要注意适用边界：**对冲只在"同一标的"内成立，不同资产之间不能互相对冲**。例如用 rQQQ 对冲 NVDAUSDT 空单、用杠杆 ETF rTSLL（Direxion 2 倍做多 TSLA）对冲 TSLAUSDT，都不会被认定为对冲仓位，因为它们的底层资产并不相同。此外，持有大量稳定币或其他资产也不能对冲某一资产的合约仓位；逐仓合约不参与计算；rToken 本身必须在 UTA 保证金币种名单内。

### 实际交易案例

以下案例中的价格、资金费率均为示意数值，仅用于说明计算方式，实际请以盘口、资金费率及费率等级为准。

#### 案例一：rNVDA + NVDAUSDT 资金费率套利

**背景：** 用户为 VIP3 机构客户，UTA 多币种保证金模式已开启 Delta 中性开关，账户内有 10,000 USDT。观察到 NVDAUSDT 资金费率持续为正，希望在不承担 NVDA 价格方向风险的情况下收取资金费。

**操作步骤：**

1. 美股盘中，以限价单买入 rNVDA，假设成交 50 股、成交均价 200 USDT，名义价值 10,000 USDT（API：[创建Reality股票订单](/zh-CN/docs/catalog/reality/trading#place-reality-order)，或统一账户[下单](/zh-CN/docs/catalog/trading/order-management#place-order)接口 `category=SPOT`、`symbol=RNVDAUSDT`；如需未成交部分路由至美股市场，不传 `venue` 使用默认策略）；
2. 确认现货腿实际成交 50 股后，在同一 UTA 内以全仓模式做空 50 NVDA 数量的 NVDAUSDT 永续合约（API：统一账户[下单](/zh-CN/docs/catalog/trading/order-management#place-order)接口 `category=USDT-FUTURES`）；
3. 此时 rNVDA 持仓 50、合约净持仓 −50，方向相反且数量相等，合约净仓位 = 0，比例 0% ≤ 5%，判定为对冲仓位，享受 ADL 排名保护；
4. 持有期间，股票合约每 8 小时结算一次资金费，资金费率为正时空头收取资金费。

#### 案例二：部分成交导致比例超限与再平衡

**背景：** 沿用案例一的账户。用户先下了 53 NVDA 数量的合约空单，但 rNVDA 限价买单只成交了 50 股，剩余部分未成交。

**判定过程：** rNVDA 持仓 50，合约净持仓 −53，方向相反且 |50| &lt; |−53|，合约净仓位 = |50 − 53| = 3；总仓位 = MAX[50 + 0, |0 − 53|] = 53；比例 = 3 ÷ 53 ≈ 5.66% &gt; 5%，不满足对冲条件，该资产按普通规则参与 ADL 排序。

**处理方式：** 补买至少 1 股 rNVDA，使比例降至 2 ÷ 53 ≈ 3.77%；或减空合约至 52 以内。系统在比例回落后自动恢复对冲仓位判定，无需重新开启开关。实践中建议"先现货、后合约"，并以现货腿的实际成交数量驱动合约下单，同时用[私有成交频道](/zh-CN/docs/uta/websocket/private/Fill-Channel)实时监听两腿成交。注意 rToken 暂不支持改单，调价需撤单后重新下单。

#### 案例三：rTSLA + TSLAUSDT 基差套利

**背景：** 市场情绪亢奋时，TSLAUSDT 永续合约价格相对 rTSLA 现货出现溢价。假设 rTSLA 现货价格 400 USDT，TSLAUSDT 合约价格 404 USDT，溢价约 1%。

**操作步骤：** 买入 20 股 rTSLA（约 8,000 USDT），同时做空 20 TSLA 数量的 TSLAUSDT（约 8,080 USDT），组合比例为 0%，判定为对冲仓位。当合约溢价收敛至 0 时，同时平掉两腿：无论 TSLA 价格涨跌，组合锁定的价差收益约为 20 × 4 = 80 USDT（约 1%），持有期间若资金费率为正，空头还可额外收取资金费。

**需要关注：** 开市时段 rTSLA 的成交价与美股同步，价差主要来自合约侧的溢价，执行时可通过 [Reality分层订单簿](/zh-CN/docs/catalog/reality/market-data#get-reality-orderbook-segmented)评估场内外深度；美股休市时段 rToken 依靠 Super Match 场内流动性定价，订单受「参考价 × 休市期间价格偏离限制（当前 20%）」保护，深度更薄，不建议在休市时段大额建仓或平仓。若对手腿出现大幅滑点，可能侵蚀全部基差收益。

## 资产

rToken 资产没有独立的资产查询接口，如需获取请复用现有的[获取账户资产](/zh-CN/docs/catalog/account/assets-balance#get-account-assets)接口查询。