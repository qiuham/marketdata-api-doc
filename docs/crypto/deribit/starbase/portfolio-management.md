---
exchange: deribit
source_url: https://docs.deribit.com/starbase/portfolio-management
api_type: Starbase
updated_at: 2026-11-19 19:05:49.430870
---

# Portfolio Management

> Portfolio-scoped Starbase controls for mass cancellation, direct-access order entry, and lock or unlock endpoints used in risk operations workflows.

The Starbase REST API exposes a set of portfolio-scoped management operations. All endpoints require authentication; the authenticated session determines which portfolio is acted upon. Any Starbase API key belonging to a direct-access-enabled portfolio can call these endpoints. The REST gateway does not currently enforce API key scopes (see [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md#front-end-interface)).

## Mass Cancel

Mass cancel removes every open order and quote belonging to the authenticated portfolio in a single call. Unlike the binary [Mass Cancel](https://docs.deribit.com/starbase/mass-cancel.md) message, which targets orders by instrument or side, the REST endpoint applies unconditionally. No filters are accepted.

The typical use case is risk reduction: a single call clears the entire book across all instruments and both sides. The endpoint returns the total number of orders cancelled across all matching engine shards.

> [!NOTE]
>
> Mass cancel via REST is always available and cannot be disabled by admin configuration.

→ [`GET /api/v2/private/cancel_all`](https://docs.deribit.com/api-reference/portfolio-management/mass-cancel)

## Portfolio Lock State

The portfolio lock controls whether `DIRECT_ACCESS` (SBE binary) order entry is accepted. The lock is a portfolio-level toggle, independent of individual sessions or gateway connections.

### Locking

Locking a portfolio has two immediate effects:

1. All open `DIRECT_ACCESS` orders and quotes for the portfolio are cancelled.
2. Any subsequent `DIRECT_ACCESS` order or quote submission is rejected until the portfolio is unlocked.

REST-submitted orders are not subject to the lock. Only binary `DIRECT_ACCESS` order flow is gated.

→ [`GET /api/v2/private/lock_portfolio`](https://docs.deribit.com/api-reference/portfolio-management/lock-portfolio)

### Unlocking

Unlocking restores normal acceptance of `DIRECT_ACCESS` order entry. Orders cancelled by the preceding lock are not reinstated; clients must resubmit any desired positions.

→ [`GET /api/v2/private/unlock_portfolio`](https://docs.deribit.com/api-reference/portfolio-management/unlock-portfolio)

> [!WARNING]
>
> After a lock, cancelled orders are gone permanently. Unlocking the portfolio does **not** restore them.

## Position Limits

`GET /api/v2/private/get_starbase_risk_limits` returns the effective position limits for the authenticated portfolio. The response has one entry per underlying (currency pair) that has a currency-pair default or an override for this portfolio.

Each numeric field is resolved on its own: a portfolio override replaces the currency-pair default only for the fields that are set. A field unset at both levels is omitted. `-1` means the limit is explicitly unlimited. The call does not change limits.

An optional `currency` query parameter selects one underlying. Use the currency-pair name from the response (for example `BTC_USDC`). The match ignores case and separators (`btc-usdc`, `BTCUSDC`). An unknown name returns HTTP 400. A known pair with no configured limit returns an empty list.

An order or replace that would breach a position size limit, such as `sm_max_future_position_size`, is rejected with `POSITION_LIMIT_EXCEEDED` (`27`). One that would breach an open order size limit, `pm_max_future_open_order_size` or `pm_max_option_open_contracts`, is rejected with `ORDER_SIZE_LIMIT_EXCEEDED` (`28`). See [Rejection Reason Codes](https://docs.deribit.com/starbase/binary-api-reference.md#rejection-reason-codes).

The endpoint is capped at 1 request per minute per portfolio on each REST gateway. See [REST Gateway Limits](https://docs.deribit.com/starbase/api-rate-limits.md#rest-gateway-limits).

→ [`GET /api/v2/private/get_starbase_risk_limits`](https://docs.deribit.com/api-reference/portfolio-management/get-starbase-risk-limits)

## Relationship to Other Risk Controls

Portfolio management complements but does not replace other Starbase risk features:

| Control | Scope | Trigger |
| - | - | - |
| [Cancel on Disconnect](https://docs.deribit.com/starbase/cancel-on-disconnect.md) | Session | TCP disconnection or missed heartbeat |
| [Mass Cancel (binary)](https://docs.deribit.com/starbase/mass-cancel.md) | Portfolio, filtered | Explicit client request via SBE |
| Mass Cancel (REST) | Portfolio, unfiltered | Explicit client request via REST |
| [Portfolio lock](https://docs.deribit.com/starbase/portfolio-management.md#portfolio-lock-state) | Portfolio | Explicit client request via REST |
| [Position limits](https://docs.deribit.com/starbase/portfolio-management.md#position-limits) | Underlying, per portfolio | Read via REST; configured by Deribit |
| [MMP](https://docs.deribit.com/starbase/mmp.md) | Underlying, MMP-tagged orders | Exposure limit breach |


## Related topics

- [Starbase API Changelog](https://docs.deribit.com/changelogs/starbase.md)
- [Creating a Starbase API Key](https://docs.deribit.com/starbase/creating-api-key.md)
- [Starbase API Rate Limits](https://docs.deribit.com/starbase/api-rate-limits.md)
- [REST Order Gateway Authentication](https://docs.deribit.com/starbase/rest-authentication.md)
- [Order Management](https://docs.deribit.com/articles/order-management-best-practices.md)